from funciones import (
    leer_api_key,
    obtener_argumentos,
    consultar_brechas,
    obtener_detalles_brecha,
    generar_csv
)


def main():
    correo = obtener_argumentos()
    api_key = leer_api_key()

    brechas = consultar_brechas(correo, api_key)
    detalles = obtener_detalles_brecha(brechas)

    generar_csv(detalles)

    print("Proceso terminado. Revisa reporte.csv y registro.log")


if __name__ == "__main__":
    main()