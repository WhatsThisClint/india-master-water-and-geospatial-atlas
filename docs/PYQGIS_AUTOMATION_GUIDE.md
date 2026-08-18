# PyQGIS & Headless Automation Guide

The **India Master Water & Geospatial Atlas** comes with an embedded QGIS project (`India_Master_Hydrology_and_Infrastructure`) that can be loaded either interactively in the QGIS GUI or automated headlessly via Python.

---

## 1. Opening the Embedded Project in QGIS (Interactive)
1. Launch QGIS 3.28+ / 3.34+ LTR.
2. Select **Project $\rightarrow$ Open From $\rightarrow$ GeoPackage...**
3. Browse to `india_master_water_and_geospatial_atlas.gpkg`.
4. Select `India_Master_Hydrology_and_Infrastructure`.

---

## 2. Headless Python / PyQGIS Scripting

```python
from qgis.core import QgsApplication, QgsProject

# Initialize QGIS Application headlessly
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.34.0/apps/qgis-ltr", True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Load Embedded Project
project = QgsProject.instance()
gpkg_uri = "geopackage:F:/Antigravity/Hydrosheds and Basins/india_master_water_and_geospatial_atlas.gpkg?projectName=India_Master_Hydrology_and_Infrastructure"
project.read(gpkg_uri)

print(f"Loaded Project Title: {project.title()}")
print(f"Total Active Layers: {len(project.mapLayers())}")

# Iterate and inspect layers
for layer_id, layer in project.mapLayers().items():
    print(f"[{layer.type().name}] {layer.name()} -> CRS: {layer.crs().authid()}")

qgs.exitQgis()
```

---

## 3. High-Resolution Map Rendering to PDF / PNG

```python
from qgis.core import QgsMapSettings, QgsMapRendererParallelJob
from qgis.PyQt.QtCore import QSize
from qgis.PyQt.QtGui import QColor, QImage

settings = QgsMapSettings()
settings.setLayers([layer for layer in project.mapLayers().values() if layer.name() == 'State & UT Boundaries (All India)'])
settings.setBackgroundColor(QColor(255, 255, 255))
settings.setOutputSize(QSize(1920, 1080))
settings.setExtent(project.layerTreeRoot().findLayer(layer.id()).layer().extent())

job = QgsMapRendererParallelJob(settings)
job.start()
job.waitForFinished()

img = job.renderedImage()
img.save("india_master_atlas_render.png", "PNG")
print("Map rendered to india_master_atlas_render.png")
```
