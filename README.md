# ✈️ Proyecto OpenSky – Seguimiento de Vuelos en Databricks

Este proyecto tiene como objetivo construir un pipeline completo de ingeniería de datos utilizando la arquitectura Medallion (Bronze → Silver → Gold) sobre **Databricks Free Edition**, consumiendo datos públicos de la red **OpenSky Network**.

El proyecto forma parte del portafolio profesional de **Renzo Hidalgo**, y está orientado a mostrar habilidades clave en procesamiento de datos, modelado, automatización y visualización.

---

## 🧰 Tecnologías utilizadas

- 🔷 **Databricks Free Edition**
- ⚙️ **PySpark + Delta Lake**
- 🌐 **OpenSky Network API**
- 🛠️ **VS Code + GitHub**
- 📋 **Notion** para gestión de tareas
- 📈 **Databricks Dashboards** para visualización final

---

## 🧱 Arquitectura Medallion

| Capa   | Descripción                                                        |
|--------|--------------------------------------------------------------------|
| Bronze | Ingesta cruda desde la API (estructura tipo JSON sin procesar)    |
| Silver | Datos limpios, estructurados y tipados para análisis               |
| Gold   | Datos agregados y enriquecidos listos para visualización y BI     |

---

## 📂 Estructura del proyecto

```
opensky/
├── notebooks/
│   ├── 00_ingestion/           # Ingesta desde Unity Catalog Volumes
│   ├── 02_silver/              # Limpieza y transformación (Bronze → Silver)
│   ├── 03_gold/                # Agregaciones y modelado analítico (Silver → Gold)
│   ├── 04_eda/                 # Análisis exploratorio (EDA)
│   └── 05_dashboards/          # Visualizaciones interactivas con display()
├── src/                        # Módulos Python: API client, transformación, utilidades
├── configs/                    # Configuración de rutas
├── tests/                      # Pruebas unitarias
├── data/                       # Archivos de datos locales (ej. JSON)
├── dags/ (opcional)            # DAGs de Airflow para automatización (si aplica)
└── README.md                   # Este archivo
```

---

## 🚀 ¿Cómo ejecutar el proyecto?

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/HCRenzo/opensky.git
   ```

2. **Obtener los datos desde la API de OpenSky:**
   Ejecuta el script:

   ```bash
   python data_ingest_local/fetch_and_save_opensky.py
   ```

3. **Subir el archivo JSON a Unity Catalog:**

   * Ve a `Data > Volumes` en Databricks
   * Crea o selecciona un volume y sube el archivo `.json`

4. **Ejecutar notebooks en Databricks:**

   * `00_ingestion/ingest_from_volume_to_bronze.ipynb`
   * `02_silver/bronze_to_silver_cleaning.ipynb`
   * `03_gold/create_gold_tables.ipynb`

5. **Explorar los datos y visualizaciones:**

   * `04_eda/exploracion_opensky.ipynb`: análisis exploratorio
   * `05_dashboards/opensky_viz.ipynb`: visualizaciones listas para dashboards

---

## 👤 Autor

**Renzo Hidalgo**
Portafolio de Ingeniería de Datos
📧 [renzo\_hc@outlook.com](mailto:renzo_hc@outlook.com)
🔗 [LinkedIn](https://www.linkedin.com/in/rhidalgoca/)
