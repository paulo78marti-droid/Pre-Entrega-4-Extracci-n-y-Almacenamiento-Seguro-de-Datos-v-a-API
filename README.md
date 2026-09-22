# Pre-Entrega 4: Extracción y Almacenamiento Seguro de Datos vía API

**Curso:** Data Science II - Coderhouse  
**Tema:** Consumo de APIs, procesamiento con Pandas y seguridad de datos.

---

## 📌 Descripción del Proyecto

En este proyecto desarrollé un script en Python (`extract_movies.py`) que se conecta a una API pública (RapidAPI - IMDb Top 100) para extraer información sobre películas. 

El script realiza los siguientes pasos:
1. Lee las credenciales de forma segura desde un archivo de variables de entorno (`.env`).
2. Consulta la API mediante peticiones HTTP (`GET`).
3. Limpia y transforma los datos recibidos usando **Pandas**.
4. Guarda la información final en dos archivos estructurados: `data_extracted.csv` y `data_extracted.json`.
5. Maneja posibles errores de conexión mediante bloques `try / except`.

---

## 📂 Archivos del Repositorio

- `extract_movies.py`: Script principal de Python con el código de extracción y guardado.
- `data_extracted.csv`: Archivo en formato CSV con los datos limpios obtenidos de la API.
- `data_extracted.json`: Archivo en formato JSON con la misma información estructurada.
- `.gitignore`: Archivo para evitar subir datos sensibles o credenciales (`.env`) a GitHub.
- `README.md`: Explicación clara y sencilla del proyecto.

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Requisitos Previos
Tener instalado Python 3.x y las librerías necesarias:

```bash
pip install requests pandas python-dotenv
```

### 2. Configuración de Credenciales (`.env`)
Crear un archivo `.env` en la raíz del proyecto con la clave de acceso a la API:

```env
RAPIDAPI_KEY=tu_api_key_aqui
RAPIDAPI_HOST=imdb-top-100-movies.p.rapidapi.com
```

> 🔒 **Seguridad:** El archivo `.env` no se sube a GitHub gracias a las reglas configuradas en `.gitignore`.

### 3. Ejecución
Abrir la terminal en la carpeta del proyecto y correr:

```bash
python extract_movies.py
```

Al finalizar la ejecución, se mostrará una vista previa de las primeras filas en la consola y se generarán los archivos `data_extracted.csv` y `data_extracted.json`.
