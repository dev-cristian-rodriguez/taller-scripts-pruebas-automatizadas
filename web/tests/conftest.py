from pathlib import Path
import pytest
from playwright.sync_api import Page
from web.pages.saucedemo import LoginPage

EVIDENCIAS = Path(__file__).resolve().parents[2] / "evidencias"
EVIDENCIAS.mkdir(exist_ok=True)


@pytest.fixture
def login(page: Page) -> LoginPage:
    return LoginPage(page).abrir()


@pytest.fixture
def sesion_estandar(login: LoginPage, page: Page) -> Page:
    """Precondición reutilizable: usuario autenticado."""
    login.iniciar_sesion("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    return page


@pytest.fixture
def evidencia(page: Page, request):
    """Devuelve una función para guardar capturas nombradas de evidencia."""
    def _capturar(nombre: str):
        ruta = EVIDENCIAS / f"{request.node.name}__{nombre}.png"
        page.screenshot(path=str(ruta), full_page=True)
        return ruta
    return _capturar


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura automática de pantalla cuando un test web falla."""
    outcome = yield
    rep = outcome.get_result()
    page = item.funcargs.get("page") if hasattr(item, "funcargs") else None
    if rep.when == "call" and rep.failed and page:
        page.screenshot(path=str(EVIDENCIAS / f"FALLO__{item.name}.png"), full_page=True)
