"""Script web: prueba del formulario de login de SauceDemo."""
import pytest
from playwright.sync_api import Page, expect
from web.pages.saucedemo import LoginPage, InventarioPage

pytestmark = pytest.mark.web


def test_formulario_login(login: LoginPage, page: Page, evidencia):
    # Paso 1: credenciales inválidas -> el formulario muestra el error y no avanza
    login.iniciar_sesion("standard_user", "clave_erronea")
    expect(login.error).to_contain_text("Username and password do not match")
    expect(page).to_have_url("https://www.saucedemo.com/")
    evidencia("error_credenciales")

    # Paso 2: credenciales válidas -> acceso al inventario
    login.iniciar_sesion("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(InventarioPage(page).titulo).to_have_text("Products")
    evidencia("login_ok")
