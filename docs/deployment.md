# Deployment

El despliegue se realiza mediante GitHub Actions y Railway.

## Ramas

- `dev`: despliega el ambiente DEV.
- `prod`: despliega el ambiente PROD.
- `main`: rama principal protegida.

## Pipeline

Cada rama ejecuta dos etapas:

1. `test`: descarga datos/modelo y ejecuta pruebas.
2. `build`: construye la imagen Docker.

## Ambientes Railway

DEV:
- Servicio: `mlops-api-dev`
- Variable: `ENVIRONMENT=dev`

PROD:
- Servicio: `mlops-api-prod`
- Variable: `ENVIRONMENT=prod`