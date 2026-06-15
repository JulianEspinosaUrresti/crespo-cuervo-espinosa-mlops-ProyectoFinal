# Pipeline MLOps

El pipeline automatiza la validación y construcción del proyecto.

## Etapa test

Durante esta etapa se ejecutan:

- Descarga del dataset de prueba externo.
- Descarga del modelo ONNX externo.
- Ejecución de pruebas unitarias.
- Validación de accuracy mínimo.

## Etapa build

Si las pruebas son exitosas, se construye la imagen Docker.

## Pruebas

- `test_prediction.py`: valida que el modelo responda correctamente.
- `test_metrics.py`: calcula accuracy y valida que sea mayor o igual a 0.80.

## Resultado esperado

Si las pruebas fallan, el pipeline se detiene y no ejecuta la etapa build.