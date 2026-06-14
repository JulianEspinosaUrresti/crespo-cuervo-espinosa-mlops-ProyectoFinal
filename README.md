# Proyecto Final MLOps - Modelo ONNX para Scoring de Crédito

## Integrantes
- David Alfonso Crespo Razeg
- Jhon Jairo Cuervo Castillo
- Julián Andrés Espinosa Urresti

---

## Objetivo

Desarrollar una solución MLOps para desplegar un modelo de scoring de crédito utilizando FastAPI, Docker, GitHub Actions, Railway y formato ONNX.

---

## Arquitectura

```text
Cliente
   │
   ▼
FastAPI
   │
   ▼
Modelo ONNX
   │
   ▼
Predicción
   │
   ▼
Archivo de Logs
```

---

## Tecnologías Utilizadas

- Python 3.11
- FastAPI
- ONNX
- ONNX Runtime
- Docker
- GitHub Actions
- Railway
- Pytest

---

## Estructura del Proyecto

```text
.
├── .github/workflows
│   ├── dev.yml
│   └── prod.yml
│
├── app
│   ├── main.py
│   ├── predictor.py
│   ├── create_model.py
│   └── requirements.txt
│
├── models
│   └── credit_model.onnx
│
├── tests
│   ├── test_metrics.py
│   └── test_prediction.py
│
├── Dockerfile
├── README.md
└── .gitignore
```

---

## Estrategia de Ramas

### DEV

Rama utilizada para:

- Desarrollo
- Pruebas
- Integración continua

Pipeline:

```text
Test → Build
```

### PROD

Rama utilizada para:

- Producción
- Despliegue final

Pipeline:

```text
Test → Build → Deploy
```

---

## GitHub Actions

### DEV

Ejecuta:

- Instalación de dependencias
- Generación del modelo ONNX
- Ejecución de pruebas

### PROD

Ejecuta:

- Instalación de dependencias
- Generación del modelo ONNX
- Ejecución de pruebas
- Construcción para producción

---

## Despliegues

### Ambiente DEV

URL:

(Pegar URL DEV)

### Ambiente PROD

URL:

(Pegar URL PROD)

Swagger:

(Pegar URL PROD/docs)

---

## Endpoint de Predicción

POST

```text
/predict
```

Ejemplo:

```json
{
  "edad": 35,
  "ingresos": 2500000,
  "deuda": 500000
}
```

Respuesta:

```json
{
  "prediction": "approved",
  "class": 1,
  "score": 0.95
}
```

---

## Pruebas

Ejecutar:

```bash
python -m pytest tests
```

Resultado esperado:

```text
2 passed
```

---

## Docker

Construcción:

```bash
docker build -t credit-scoring .
```

Ejecución:

```bash
docker run -p 8000:8000 credit-scoring
```

---

## Modelo ONNX

El modelo ONNX se genera automáticamente durante el proceso de CI/CD mediante:

```python
create_model.py
```

---

## Evidencia de CI/CD

- GitHub Actions DEV
- GitHub Actions PROD
- Railway DEV
- Railway PROD
- Endpoint FastAPI
- Modelo ONNX