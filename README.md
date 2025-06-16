# ✈️ Proyecto OpenSky - Seguimiento de Vuelos en Databricks

Este proyecto tiene como objetivo construir un pipeline de ingeniería de datos utilizando la arquitectura Medallion (Bronze, Silver, Gold) sobre Databricks, aprovechando datos públicos de la red OpenSky.

---

## 🔧 Tecnologías utilizadas

- 🧠 **Databricks Free Edition**
- 🔁 **PySpark + Delta Lake**
- 🌐 **OpenSky Network API**
- 🛠 **VS Code + GitHub**
- 📋 **Notion** para gestión de tareas

---

## 📂 Estructura del proyecto
opensky/
├── notebooks/ # Notebooks organizados por capas (00 - 04)
├── src/ # Código fuente Python
├── configs/ # Configuración de rutas
├── tests/ # Tests unitarios
├── data/ # Datos de prueba local
├── dags/ (opcional) # DAGs si se usa Airflow
└── README.md

---

## 🧱 Arquitectura Medallion

- **Bronze**: Datos crudos desde la API de OpenSky (`/states/all`)
- **Silver**: Datos limpios con columnas estructuradas y tipos adecuados
- **Gold**: Agregaciones por país, aerolínea, tiempo, etc.

---

## 🚀 Instrucciones para ejecutar

1. Clona el repositorio:
    git clone https://github.com/tu_usuario/opensky.git
2. Ejecuta el notebook 00_ingestion/ingest_opensky_raw.ipynb en Databricks
3. Explora las capas siguientes y desarrolla el análisis

Renzo Hidalgo - Portafolio de Ingeniería de Datos
