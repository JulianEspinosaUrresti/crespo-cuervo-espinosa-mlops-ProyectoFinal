# Arquitectura

El proyecto implementa una API FastAPI desplegada en Railway con dos servicios:

- `mlops-api-dev`
- `mlops-api-prod`

## Flujo general

GitHub → GitHub Actions → Pruebas → Build Docker → Railway

## Artefactos externos

El pipeline descarga desde GitHub Releases:

- `train_data.csv`
- `test_data.json`
- `credit_model.onnx`

## Monitoreo

Las predicciones se almacenan externamente en GitHub Gist:

- `predicciones_dev.txt`
- `predicciones_prod.txt`