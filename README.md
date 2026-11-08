# Taller individual: scripts de prueba automatizados para servicios REST y formularios web

Asignatura: Pruebas y Calidad del Software, Universidad Tecnológica del Oriente.
Estudiante: Cristian Rodriguez Benitez.

Dos scripts automatizados con pytest:

| Script | Sistema bajo prueba | Herramientas | Contenido |
|---|---|---|---|
| `web/` | https://www.saucedemo.com (formulario de login) | Playwright, Page Object Model | 1 script (login: error y éxito) |
| `api/` | https://jsonplaceholder.typicode.com | requests, jsonschema | 1 script (GET y POST) |

## Estructura

```
api/
  schemas.py               esquema JSON del contrato
  test_api_rest.py         script de API (GET y POST)
web/
  pages/saucedemo.py       Page Objects (LoginPage, InventarioPage)
  tests/conftest.py        fixtures, capturas de evidencia y captura automática ante fallos
  tests/test_formularios_web.py   script web (login)
evidencias/                capturas y reportes generados
.github/workflows/qa.yml   pipeline de integración continua
```

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate          # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Ejecución

```bash
pytest api                                   # API REST
pytest web                                   # formularios web (headless)
pytest web --headed --slowmo 500             # navegador visible
pytest -m negativa                           # solo casos de error
pytest api web --html=evidencias/reporte.html --self-contained-html
```

Las capturas se guardan en `evidencias/`. Si una prueba web falla, se genera `FALLO__<prueba>.png`.

## Nota

Las pruebas dependen de servicios públicos de terceros (SauceDemo y JSONPlaceholder) y requieren conexión a internet.
