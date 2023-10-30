# Dockerfile
# Imagen base a usar para la construccion de la imagen a trabajar
# Es una imagen de Ubuntu
FROM ubuntu

# Actualiza la lista local de paquetes de Ubuntu, dentro de la imagen
RUN apt-get update -y

# Instalacion de paquetes necesarios
RUN apt-get install -y python3 python-pip

# Incluye en la variable de entorno PATH la ruta /usr/local/bin que es
# la ruta en donde se instala pip. PATH incluye en los linux la ruta
# en donde se encuentran los binarios del sistema.
ENV PATH /usr/local/bin:$PATH

# Se instalan los modulos de python que se requieran
# RUN pip install nombre_modulo

# Copia el archivo clienteHTTP.py que se encuentra en el mismo
# directorio que el archivo Dockerfile al directorio /opt/ dentro de
# la imagen
ADD clienteHTTP.py /opt/ 