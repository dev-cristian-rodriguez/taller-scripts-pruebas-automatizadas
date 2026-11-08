"""Page Objects (patrón POM) para https://www.saucedemo.com.
Cada clase encapsula selectores y acciones; los tests solo expresan intención."""
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.usuario = page.locator('[data-test="username"]')
        self.clave = page.locator('[data-test="password"]')
        self.boton = page.locator('[data-test="login-button"]')
        self.error = page.locator('[data-test="error"]')

    def abrir(self):
        self.page.goto(BASE_URL)
        expect(self.boton).to_be_visible()
        return self

    def iniciar_sesion(self, usuario: str, clave: str):
        self.usuario.fill(usuario)
        self.clave.fill(clave)
        self.boton.click()


class InventarioPage:
    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator('[data-test="title"]')
