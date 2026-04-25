# Evidencia-21
#  Verificador de Brechas de Seguridad

## Desarrollador
Irving Azael Muñoz Ochoa

---

## 📌 Descripción del repositorio
Este repositorio contiene un script en Python diseñado para consultar si un correo electrónico ha sido expuesto en brechas de seguridad mediante el uso de una API externa.

El proyecto fue refactorizado de forma modular, separando las funciones principales para mejorar la organización, mantenibilidad y buenas prácticas de programación.

---

##  Estructura del proyecto
- `funciones.py` → Contiene todas las funciones principales del sistema
- `verificar_correo.py` → Script principal que ejecuta el programa
- `requirements.txt` → Dependencias necesarias del proyecto
- `README.md` → Documentación del proyecto
- `registro.log` → Archivo de logs generado automáticamente
- `reporte.csv` → Archivo con los resultados de la consulta

---

##  Funcionalidades del sistema
- Lectura segura de API Key desde variables de entorno
- Obtención de argumentos desde línea de comandos
- Consulta de brechas de seguridad por correo electrónico
- Extracción y procesamiento de información relevante de las brechas
- Generación automática de reportes en formato CSV
- Registro de eventos y errores en un archivo de logging

---

##  Tareas de ciberseguridad que resuelve
Este proyecto permite:
- Identificar si un correo ha sido comprometido en filtraciones de datos
- Analizar la exposición de información en brechas conocidas
- Generar reportes para análisis posterior
- Automatizar consultas de seguridad digital

---

