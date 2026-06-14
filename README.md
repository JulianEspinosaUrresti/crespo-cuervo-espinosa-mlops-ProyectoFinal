# Proyecto Final MLOps

## Integrantes
- David Alfonso Crespo Razeg
- Jhon Jairo Cuervo Castillo
- Julián Andrés Espinosa Urresti

## Arquitectura

Cliente → FastAPI → Modelo ONNX → Predicción

## Tecnologías
- Python
- FastAPI
- ONNX
- Docker
- GitHub Actions
- Railway

## Ejecución local

```bash
docker build -t proyecto-final .
docker run -p 8000:8000 proyecto-final