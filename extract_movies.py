import os
import sys

# Comprobar importación de librerías requeridas
try:
    import requests
    import pandas as pd
    from dotenv import load_dotenv
except ImportError as e:
    print("❌ Error: Falta instalar una librería requerida.")
    print(f"Detalle: {e}\n\n👉 Para instalarlas, ejecuta en tu terminal:\npip install -r requirements.txt")
    sys.exit(1)


def main():
    print("=== INICIANDO PIPELINE DE EXTRACCIÓN Y ALMACENAMIENTO DE DATOS VÍA API ===")
    
    # 1. Cargar Variables de Entorno desde el archivo .env (Seguridad)
    load_dotenv(override=True)

    api_key = os.getenv("RAPIDAPI_KEY")
    api_host = os.getenv("RAPIDAPI_HOST", "imdb-top-100-movies.p.rapidapi.com")

    # Validación de seguridad: no comprometer llaves ni hardcodear credenciales
    if not api_key or api_key.strip() in ("", "TU_RAPIDAPI_KEY_AQUI", "tu_api_key_de_rapidapi_aqui"):
        print("\n⚠️ AVISO DE SEGURIDAD:")
        print("No se detectó una RAPIDAPI_KEY activa en tu archivo local '.env'.")
        print("👉 Crea un archivo '.env' basado en '.env.example' e ingresa tu API Key personal.\n")
        api_key = None

    datos_json = None

    # 2. Extracción de datos si existe una API Key válida
    if api_key:
        url = f"https://{api_host}/"
        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": api_host,
        }

        print("🔄 Conectando con la API de RapidAPI...")

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            datos_json = response.json()
            cant = len(datos_json) if isinstance(datos_json, list) else "varios"
            print(f"✅ ¡Petición exitosa! Registros recuperados desde la API: {cant}")

        except requests.exceptions.HTTPError as error:
            status = getattr(error.response, 'status_code', 'Desconocido')
            print(f"❌ Error en la API (HTTP {status}): {error}")
            if status in (401, 403):
                print("💡 Verifica que tu RAPIDAPI_KEY en el archivo .env sea válida y esté activa.")
        except requests.exceptions.Timeout:
            print("❌ Error: Tiempo de espera agotado al conectar con la API.")
        except requests.exceptions.ConnectionError:
            print("❌ Error de red: No se pudo conectar al servidor de la API.")
        except requests.exceptions.RequestException as error:
            print(f"❌ Error en la petición HTTP: {error}")
        except Exception as error:
            print(f"❌ Error inesperado durante la extracción: {error}")

    # Si no se obtuvieron datos de la API, interrumpir la ejecución sin guardar archivos defectuosos
    if not datos_json:
        print("❌ Error: No se pudieron obtener datos de la API. El proceso ha finalizado.")
        sys.exit(1)


    # 3. Transformación y Limpieza de Datos con Pandas
    df = pd.DataFrame(datos_json)
    columnas_deseadas = ["rank", "title", "rating", "year", "genre", "description"]
    columnas_existentes = [c for c in columnas_deseadas if c in df.columns]

    df_limpio = df[columnas_existentes].copy()

    # Formatear lista de géneros a texto separado por comas
    if "genre" in df_limpio.columns:
        df_limpio["genre"] = df_limpio["genre"].apply(
            lambda g: ", ".join(g) if isinstance(g, list) else g
        )

    # 4. Persistencia / Guardado en CSV y JSON
    df_limpio.to_csv("data_extracted.csv", index=False, encoding="utf-8")
    df_limpio.to_json("data_extracted.json", orient="records", indent=4, force_ascii=False)

    # Guardar también en la carpeta data/
    os.makedirs("data", exist_ok=True)
    df_limpio.to_csv("data/data_extracted.csv", index=False, encoding="utf-8")
    df_limpio.to_json("data/data_extracted.json", orient="records", indent=4, force_ascii=False)

    print("\n💾 ¡Datos guardados exitosamente!")
    print(" Archivos de salida generados:")
    print("  - data_extracted.csv")
    print("  - data_extracted.json")

    print("\n--- VISTA PREVIA DE LOS DATOS EXTRAÍDOS (PRIMERAS 5 FILAS) ---")
    print(df_limpio.head())


if __name__ == "__main__":
    main()