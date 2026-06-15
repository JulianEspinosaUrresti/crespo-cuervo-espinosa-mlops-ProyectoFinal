# Proyecto Final MLOps - Despliegue de Modelo ONNX

## Integrantes
- David Alfonso Crespo Razeg
- Jhon Jairo Cuervo Castillo
- Julián Andrés Espinosa Urresti

---

## Descripción

Este proyecto implementa un flujo completo de MLOps para el despliegue de un modelo de Machine Learning exportado a formato ONNX, incluyendo:

- Entrenamiento y exportación del modelo.
- Pruebas unitarias automatizadas.
- Integración Continua (CI).
- Despliegue Continuo (CD).
- Ambientes DEV y PROD.
- Despliegue en Railway.
- Monitoreo mediante registros de predicciones.
- Gestión externa del modelo y de los datos de prueba.

---

# Arquitectura de la Solución

```text
GitHub Repository
        │
        ▼
GitHub Actions
        │
        ├── Descarga modelo ONNX
        │
        ├── Descarga datos de prueba
        │
        ├── Ejecuta pruebas unitarias
        │
        ├── Build Docker
        │
        ▼
      Railway
      ├── DEV
      └── PROD
```

---

# Modelo Implementado

Se implementó un modelo de clasificación utilizando:

```python
DecisionTreeClassifier
```

El modelo fue exportado a formato:

```text
ONNX
```

para permitir inferencia independiente del framework utilizado durante el entrenamiento.

---

# Variables de Entrada

El modelo utiliza tres variables:

| Variable | Tipo |
|-----------|--------|
| edad | Numérica |
| ingresos | Numérica |
| deuda | Numérica |

---

# Variables de Salida

El modelo genera:

| Campo | Descripción |
|---------|-------------|
| prediction | approved / rejected |
| class | 1 o 0 |
| score | nivel de confianza |

---

# Gestión Externa del Modelo

El archivo ONNX no se encuentra almacenado dentro del repositorio.

Durante la ejecución del pipeline se descarga desde GitHub Releases.

Release utilizado:

```text
v1.0-model
```

Archivo:

```text
credit_model.zip
```

---

# Gestión Externa de Datos de Prueba

Los datos utilizados para las pruebas tampoco se almacenan dentro del repositorio.

Durante la ejecución del pipeline son descargados desde GitHub Releases.

Release utilizado:

```text
v1.0-model
```

Archivo:

```text
test_data.json
```

---

# Pruebas Unitarias

El proyecto contiene pruebas automatizadas para validar:

## Test 1

Validar que el modelo genere una respuesta válida.

Archivo:

```text
tests/test_prediction.py
```

---

## Test 2

Validar que la métrica mínima del modelo se mantenga sobre el umbral establecido.

Archivo:

```text
tests/test_metrics.py
```

---

# CI/CD

El proyecto utiliza GitHub Actions para automatizar:

1. Descarga del modelo ONNX.
2. Descarga de datos de prueba.
3. Ejecución de pruebas unitarias.
4. Construcción de imagen Docker.
5. Despliegue automático.

---

# Ambientes

## Ambiente DEV

Swagger:

```text
https://crespo-cuervo-espinosa-mlops-proyectofinal-production.up.railway.app/docs
```

Endpoint:

```text
POST /predict
```

---

## Ambiente PROD

Swagger:

```text
https://authentic-simplicity-production-5b90.up.railway.app/docs
```

Endpoint:

```text
POST /predict
```

---

# Ejemplo de Consumo

## Request

```json
{
  "edad": 35,
  "ingresos": 2500000,
  "deuda": 500000
}
```

## Response

```json
{
  "prediction": "approved",
  "class": 1,
  "score": 0.95
}
```

---

# Monitoreo de Predicciones

Todas las inferencias realizadas por los ambientes DEV y PROD son registradas para fines de monitoreo y trazabilidad.

Release utilizado:

```text
prediction-logs
```

Archivos:

```text
predicciones_dev.txt
predicciones_prod.txt
```

---

# Contenedorización

El proyecto utiliza Docker para empaquetar la aplicación.

Construcción local:

```bash
docker build -t mlops-final .
```

Ejecución local:

```bash
docker run -p 8000:8000 mlops-final
```

---

# Gestión de Ramas

## Rama Principal

```text
main
```

Características:

- Rama protegida.
- Requiere Pull Request.
- Requiere validación de checks.
- Requiere ramas actualizadas antes del merge.

---

# Tecnologías Utilizadas

- Python 3.11
- FastAPI
- ONNX Runtime
- Scikit-Learn
- Docker
- GitHub Actions
- Railway
- GitHub Releases

---

# Estado Final del Proyecto

| Componente | Estado |
|------------|---------|
| Modelo ONNX | ✅ |
| Datos externos | ✅ |
| Tests automatizados | ✅ |
| Docker | ✅ |
| GitHub Actions | ✅ |
| Ambiente DEV | ✅ |
| Ambiente PROD | ✅ |
| Monitoreo | ✅ |
| Rama protegida | ✅ |
| CI/CD | ✅ |

---

# Autor

Proyecto desarrollado como entrega final de la asignatura de MLOps.