# Usar una imagen base mínima de Python
FROM python:3.10-slim

RUN pip install keras-image-helper
RUN pip install "numpy<2"
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl


# Crear un directorio de trabajo
WORKDIR /app

COPY bcd_xception.tflite /app/

# Comando por defecto
CMD ["python"]
