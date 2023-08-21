# Usa la imagen oficial de Python como base
FROM python:3.10.12-bookworm

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos a la imagen
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el contenido de tu proyecto a la imagen
COPY . /app/

# Expone el puerto en el que se ejecutará tu aplicación (por ejemplo, 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación (ajústalo según tu proyecto)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]