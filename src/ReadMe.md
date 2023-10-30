## Evaluación

# Local
* Forma de ejecuar el codigo:
Para ejecutar de manera local solo basta con hacer:
* py clienteHTTP.py www.fciencias.unam.mx GET / 1 identity close

# Docker
Para ejecutar usando Docker solo basta con hacer:
* python3 /opt/clienteHTTP.py www.fciencias.unam.mx GET / 1 identity close

# Ejemplos
* py clienteHTTP.py www.fciencias.unam.mx GET / 1 identity close
* py clienteHTTP_base.py mail7.unam.mx  GET / 2 identity close
* py clienteHTTP_base.py encomunicacionct.geociencias.unam.mx  GET / 3 identity close

## Preguntas
# ¿Cuál es la función de los métodos de HTTP HEAD, GET, POST, PUT y DELETE?

* Head: Se utiliza para solicitar únicamente los encabezados de una respuesta 
HTTP, sin incluir el cuerpo de la respuesta. Esto es útil para obtener información
sobre un recurso sin tener que descargar todo su contenido.

* GET: Se utiliza para recuperar datos de un recurso específico. Al realizar una 
solicitud GET, el servidor devuelve la representación del recurso solicitado. 
Esta representación puede ser en diferentes formatos, como HTML, XML, JSON, 
imágenes, JavaScript, CSS, etc.

* POST: se utiliza para enviar datos al servidor para que sean procesados. 
Por lo general, se utiliza para enviar información de un formulario o para 
crear un nuevo recurso en el servidor. La solicitud POST incluye los datos 
en el cuerpo de la solicitud HTTP.

* PUT: Se utiliza para actualizar completamente un recurso existente en el 
servidor. Al realizar una solicitud PUT, se envía una representación completa
del recurso actualizado al servidor. Esto significa que se deben incluir todos
los atributos del recurso, incluso si solo se desea actualizar uno de ellos. 
Si el recurso no existe, se crea uno nuevo.

* DELETE: Se utiliza para eliminar un recurso específico en el servidor. Al 
realizar una solicitud DELETE, se indica al servidor que elimine el recurso 
identificado en la URL de la solicitud. Si la eliminación es exitosa, el 
servidor devuelve una respuesta con un código de estado 
200 (OK) o 204 (No Content).

# ¿Investigue y enliste junto con su significado las categorías de códigos de estado que usa HTTP?

* 1xx - Respuestas informativas: Estos códigos indican que la solicitud ha 
sido recibida y el servidor está procesando la solicitud. Algunos ejemplos de códigos de 
esta categoría son:

- 100 - Continuar
- 101 - Cambio de Protocolo

* 2xx - Respuestas exitosas: Estos códigos indican que la solicitud ha sido 
procesada correctamente por el servidor. Algunos ejemplos de códigos de 
esta categoría son:

- 200 - OK
- 201 - Creado
- 204 - Sin contenido

* 3xx - Redirecciones: Estos códigos indican que el cliente debe realizar 
una acción adicional para completar la solicitud. Algunos ejemplos de códigos de 
esta categoría son:

- 301 - Movido permanentemente
- 302 - Encontrado
- 304 - No modificado

* 4xx - Errores del cliente: Estos códigos indican que ha ocurrido un error 
en la solicitud realizada por el cliente. Algunos ejemplos de códigos de 
esta categoría son:

- 400 - Solicitud incorrecta
- 403 - Prohibido
- 404 - No encontrado

* 5xx - Errores del servidor: Estos códigos indican que ha ocurrido un error
en el servidor al procesar la solicitud. Algunos ejemplos de códigos de 
esta categoría son:

- 500 - Error interno del servidor
- 502 - Puerta de enlace incorrecta
- 503 - Servicio no disponible


# ¿Para qué se usan los campos encoding y connection?

- El campo encoding se utiliza para especificar la codificación de caracteres 
utilizada en una solicitud o respuesta HTTP. La codificación de caracteres 
determina cómo se representan los caracteres en el texto. Al especificar la 
codificación de caracteres en el campo encoding, se asegura que el servidor 
y el cliente puedan interpretar correctamente los caracteres en la comunicación.

- El campo connection se utiliza para controlar la conexión entre el cliente 
y el servidor. Puede indicar si la conexión debe mantenerse abierta después 
de que se complete la solicitud o si debe cerrarse. También puede especificar 
si se debe utilizar una conexión segura, como TLS/SSL.