# Proyecto Tienda Online

Este proyecto es un ejemplo de automatización de pruebas para una tienda online utilizando Selenium, Pytest y WebDriver Manager en Python.

## Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

2. **Crea un entorno virtual (opcional pero recomendado):**

1. **Clona el repositorio o descarga el proyecto.**

2. **Crea un entorno virtual (opcional pero recomendado):**

    - **En Windows (PowerShell):**
       ```powershell
       python -m venv .venv
       .\.venv\Scripts\activate
       ```

    - **En macOS/Linux (Terminal):**
       ```bash
       python3 -m venv .venv
       source .venv/bin/activate
       ```

3. **Instala las dependencias:**

    - **En Windows:**
       ```powershell
       pip install -r requirements.txt
       ```

    - **En macOS/Linux:**
       ```bash
       pip3 install -r requirements.txt
       ```
- `tests/` — Pruebas automatizadas
- `conftest.py` — Configuración de Pytest
- `requirements.txt` — Dependencias del proyecto

```powershell
pytest
Para ejecutar los tests, usa el siguiente comando según tu sistema operativo:

- **En Windows:**
   ```powershell
   pytest
   ```
- **En macOS/Linux:**
   ```bash
   pytest
   ```
- pytest

---

¡Listo! Ahora puedes comenzar a automatizar pruebas para tu tienda online.
