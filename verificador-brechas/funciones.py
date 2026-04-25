import os
import csv
import logging
import argparse
import requests


# ---------------- CONFIGURACIÓN DE LOGGING ----------------
logging.basicConfig(
    filename="registro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------- LECTURA SEGURA DE API KEY ----------------
def leer_api_key(env_var="API_KEY"):
    """
    Lee la API key desde variables de entorno de forma segura.
    """
    api_key = os.getenv(env_var)

    if not api_key:
        logging.error("API Key no encontrada en variables de entorno")
        raise ValueError("API Key no encontrada")

    return api_key


# ---------------- ARGUMENTOS CLI ----------------
def obtener_argumentos():
    """
    Obtiene el correo a analizar desde línea de comandos.
    """
    parser = argparse.ArgumentParser(description="Verificador de brechas de seguridad")
    parser.add_argument("--correo", required=True, help="Correo a consultar")

    args = parser.parse_args()
    return args.correo


# ---------------- CONSULTA DE BRECHAS ----------------
def consultar_brechas(correo, api_key):
    """
    Consulta brechas de seguridad asociadas a un correo.
    """
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{correo}"

    headers = {
        "hibp-api-key": api_key,
        "user-agent": "python-app"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        logging.info(f"No se encontraron brechas para {correo}")
        return []

    if response.status_code != 200:
        logging.error(f"Error en consulta: {response.status_code}")
        return []

    logging.info(f"Brechas encontradas para {correo}")
    return response.json()


# ---------------- DETALLE DE BRECHAS ----------------
def obtener_detalles_brecha(brechas):
    """
    Extrae información relevante de las brechas.
    """
    detalles = []

    for b in brechas:
        detalles.append({
            "Nombre": b.get("Name"),
            "Dominio": b.get("Domain"),
            "Fecha": b.get("BreachDate"),
            "PwnCount": b.get("PwnCount")
        })

    return detalles


# ---------------- GENERAR CSV ----------------
def generar_csv(datos, archivo="reporte.csv"):
    """
    Genera archivo CSV con los resultados.
    """
    if not datos:
        logging.info("No hay datos para generar CSV")
        return

    keys = datos[0].keys()

    with open(archivo, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(datos)

    logging.info(f"Archivo CSV generado: {archivo}")