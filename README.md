# mini-lista-compras

Pequeña aplicación para gestionar una lista de la compra (CRUD de ítems). Esta plantilla está adaptada al repositorio HandrykM/mini-lista-compras (principalmente Python con frontend en JavaScript/CSS/HTML). Ajusta los comandos y nombres de archivo según el framework real (Flask/FastAPI/Django) que uses.

Estado: WIP

Badges:
- build: ![build](https://img.shields.io/badge/build-pendiente-lightgrey)
- license: ![license](https://img.shields.io/badge/license-MIT-blue)

Índice
- [Descripción](#descripción)
- [Características](#características)
- [Tecnologías](#tecnologías)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Variables de entorno](#variables-de-entorno)
- [Scripts útiles](#scripts-útiles)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Testing](#testing)
- [Docker](#docker)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Descripción
mini-lista-compras es una aplicación simple para crear, listar, editar y eliminar elementos de una lista de la compra. Está pensada como proyecto pequeño para aprender y desplegar fácilmente.

## Características
- Añadir / editar / eliminar ítems
- Marcar ítems como comprados
- Interfaz web ligera (HTML/CSS/JS)
- API REST (backend en Python)
- Persistencia simple (SQLite por defecto, opcionalmente PostgreSQL)

## Tecnologías
- Backend: Python (Flask / FastAPI / Django — ajustar según el repo)
- Frontend: JavaScript, HTML, CSS
- Base de datos por defecto: SQLite (configurable a PostgreSQL)
- Contenedores: Docker (opcional)
- Tests: pytest (recomendado)

## Requisitos
- Python 3.8+
- pip
- (opcional) Docker y docker-compose
- git

## Instalación (local, virtualenv)
1. Clona el repositorio:
   ```bash
   git clone https://github.com/HandrykM/mini-lista-compras.git
   cd mini-lista-compras
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / macOS
   .venv\Scripts\activate      # Windows
   ```
3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Copia el ejemplo de variables de entorno:
   ```bash
   cp .env.example .env
   ```
   Edita `.env` con las claves adecuadas.

5. Inicializa la base de datos (ejemplo SQLite):
   - Si usas Flask con Flask-Migrate:
     ```bash
     flask db upgrade
     ```
   - Si usas Django:
     ```bash
     python manage.py migrate
     ```
   - Si usas un script de inicialización:
     ```bash
     python scripts/init_db.py
     ```

## Uso (ejemplos)
- Flask (si el repo usa Flask):
  ```bash
  export FLASK_APP=app.py
  export FLASK_ENV=development
  flask run --reload
  ```
- FastAPI (si el repo usa FastAPI):
  ```bash
  uvicorn main:app --reload --port 8000
  ```
- Django:
  ```bash
  python manage.py runserver
  ```

Accede a: http://localhost:8000 (o puerto configurado).

Ejemplo de petición a la API:
```bash
curl -X GET http://localhost:8000/api/items
```

## Variables de entorno (ejemplo .env)
```
FLASK_ENV=development
SECRET_KEY=tu_secreto_aqui
DATABASE_URL=sqlite:///./data.db
PORT=8000
```

Incluye un archivo `.env.example` con los nombres de variables sin valores reales.

## Scripts útiles (ajusta según package)
- Iniciar en desarrollo:
  - Flask: `flask run`
  - FastAPI: `uvicorn main:app --reload`
- Tests: `pytest`
- Linter: `flake8` / `pylint`
- Formateo: `black`

## Estructura propuesta del proyecto
- app/ or src/
  - static/        # js, css, imágenes
  - templates/     # HTML (si aplica)
  - models.py
  - routes.py / views.py / api/
  - services/
  - config.py
- tests/
- requirements.txt
- Dockerfile
- docker-compose.yml
- .env.example
- README.md

Ajusta esta estructura a la real en el repo.

## Testing
- Ejecutar tests:
  ```bash
  pytest
  ```
- Para usar una DB de pruebas, configura `DATABASE_URL` a una DB separada o usa fixtures que aíslen la DB.

## Docker (opcional)
Ejemplo mínimo para desarrollo:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
Ejecutar:
```bash
docker build -t mini-lista-compras .
docker run --env-file .env -p 8000:8000 mini-lista-compras
```

## Contribuir
1. Haz fork
2. Crea rama feature: `git checkout -b feat/nueva-funcionalidad`
3. Escribe tests y documentación
4. Haz PR describiendo cambios

Sigue convenciones de commits y ejecuta linters/tests antes de enviar PR.

## Licencia
MIT. Cambia según corresponda.

## Contacto
Autor: Ju4nD13go
Repositorio: https://github.com/HandrykM/mini-lista-compras

Notas: reemplaza las secciones de comandos e inicialización con los archivos concretos del repo (por ejemplo, `app.py`, `main.py`, `manage.py`, `requirements.txt`) para que el README quede 1:1 con este repositorio.
