# Pre-Entrega 4: Extracción y Almacenamiento Seguro de Datos vía API

Este proyecto implementa un pipeline ETL funcional en Python (`extract_movies.py`) para la **extracción automatizada de datos desde una API externa (RapidAPI - IMDb Top 100)**, aplicando **transformaciones de datos con Pandas**, **persistencia estructurada (`data_extracted.csv` y `data_extracted.json`)**, **gestión segura de credenciales mediante variables de entorno (`.env`)** y **manejo robusto de excepciones (HTTP 404, 500, 401, 403, Timeout, ConnectionError)**.

---

## 📁 Estructura del Repositorio

```text
├── data/
│   ├── data_extracted.csv     # Archivo estructurado CSV generado con los datos extraídos
│   └── data_extracted.json    # Archivo estructurado JSON generado con los datos extraídos
├── data_extracted.csv         # Archivo CSV final en raíz requerido por la entrega
├── data_extracted.json        # Archivo JSON final en raíz requerido por la entrega
├── .env.example               # Plantilla segura para la configuración de variables de entorno
├── .gitignore                 # Exclusión de credenciales (.env) y archivos sensibles en Git
├── Objetivo de la Pre-Entrega.md # Consigna y requisitos oficiales de la actividad
├── README.md                  # Documentación completa del proyecto
├── extract_movies.py          # Script ejecutable en Python (Petición GET + ETL + Persistencia)
├── extract_movies.ipynb       # Notebook ejecutable en Google Colab / Jupyter
└── requirements.txt           # Lista de dependencias del proyecto (requests, pandas, python-dotenv)
```

---

## 🚀 Requisitos e Instalación Local

### 1. Requisitos Previos
- Python 3.8+ instalado.
- Cuenta en [RapidAPI](https://rapidapi.com/).

### 2. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd "Pre-Entrega 4- Extracción y Almacenamiento Seguro de Datos vía API"
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

---

## 🔐 Configuración de Seguridad (.env)

Crea tu archivo `.env` local copiando la plantilla `.env.example`:

```bash
# Copiar plantilla en Windows:
copy .env.example .env

# Copiar plantilla en Linux / macOS:
cp .env.example .env
```

Edita el archivo `.env` agregando tu API Key personal:

```env
RAPIDAPI_KEY=TU_RAPIDAPI_KEY_AQUI
RAPIDAPI_HOST=imdb-top-100-movies.p.rapidapi.com
```

> ⚠️ **Seguridad:** El archivo `.env` está expresamente excluido en `.gitignore` para prevenir la filtración de claves privadas o credenciales en GitHub.

---

## 💻 Ejecución del Script

Ejecuta el script principal en la terminal:

```bash
python extract_movies.py
```

### ⚙️ Lógica Implementada en `extract_movies.py`:
1. **Configuración de Seguridad:** Carga automática de variables de entorno desde `.env` usando `python-dotenv`.
2. **Petición HTTP GET:** Consulta a la API con cabeceras autenticadas (`X-RapidAPI-Key` y `X-RapidAPI-Host`).
3. **Manejo de Excepciones:** Evaluación de errores HTTP (`401`, `403`, `404`, `500`), tiempos de espera (`Timeout`) y errores de red (`ConnectionError`).
4. **Transformación y Limpieza con Pandas:** Filtrado de campos deseados (`rank`, `title`, `rating`, `year`, `genre`, `description`) y formateo de géneros.
5. **Persistencia Automatizada:** Exportación de resultados a `data_extracted.csv` y `data_extracted.json`.

---

## 👥 Autor
Proyecto desarrollado para la **Pre-Entrega 4: Extracción y Almacenamiento Seguro de Datos vía API** - Coderhouse (Data Science II).
