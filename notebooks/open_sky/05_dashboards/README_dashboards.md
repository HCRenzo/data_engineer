# 📊 Dashboards - Proyecto OpenSky (Capa Gold)

Este notebook contiene visualizaciones construidas a partir de las tablas Gold generadas en el proyecto OpenSky, bajo la arquitectura Medallion (Bronze → Silver → Gold). Las visualizaciones permiten interpretar datos de vuelos y países en tiempo real o snapshots históricos.

---

## 🧭 Objetivo

Permitir el análisis visual de métricas clave de vuelos por país, tales como altitud, velocidad, volumen de vuelos y estado (en el aire / en tierra).

---

## 📁 Notebook principal

* [`opensky_viz.ipynb`](opensky_viz.ipynb)

---

## 📊 Visualizaciones incluidas

| # | Métrica                                 | Tabla origen                         | Tipo sugerido        |
| - | --------------------------------------- | ------------------------------------ | -------------------- |
| 1 | Altitud promedio por país               | `default.gold_avg_altitude`          | Bar chart            |
| 2 | Velocidad promedio por país             | `default.gold_velocity_by_country`   | Horizontal bar chart |
| 3 | Total de vuelos por país                | `default.gold_total_flights`         | Pie / Column chart   |
| 4 | Vuelos en tierra vs en el aire por país | `default.gold_airborne_distribution` | Stacked bar chart    |
| 5 | Altitud y velocidad promedio en el aire | `default.gold_avg_airborne_stats`    | Dual column chart    |
| 6 | Top 10 vuelos con mayor altitud         | `default.gold_top_altitudes`         | Table / Column chart |

---

## 📌 Recomendaciones

* Puedes fijar visualizaciones en un Dashboard desde el botón 📊 de cada celda `display()`.
* Ideal para validaciones rápidas, reportes exploratorios o demo del portafolio.
* Puedes exportar resultados si deseas usarlos en Power BI o QuickSight.

---

## 🚀 Próximos pasos

* Crear visualizaciones en tiempo real si se programa la ingesta periódica.
* Incluir segmentación por región o agrupación personalizada (EU / LATAM).
* Publicar screenshots o links embed en tu portafolio personal.

---

**Autor:** Renzo Hidalgo
🔗 [LinkedIn](https://www.linkedin.com/in/rhidalgoca/)
