import socket
import sys

def printArguments():
    print("\n\nEl script debe ejecutarse con al menos seis argumentos con el siguiente formato:\n ")
    print("''py clientHTTP.py host http_method url user_agent encoding connection'' \n")
    print("Las opciones de User-Agent disponibles son: ")
    print("1. Mozilla Firefox")
    print("2. Google Chrome")
    print("3. Microsoft Edge \n\n")

def proccessArguments():
    # Recibe de la linea de comandos los argumentos
    try:
        host_server = sys.argv[1]
        http_method = sys.argv[2]
        url = sys.argv[3]
        user_agent_choice = int(sys.argv[4])
        encoding = sys.argv[5]
        connection = sys.argv[6]

        arguments = [host_server, http_method, url, user_agent_choice, encoding, connection]

        return arguments
    except IndexError:
        print("Error: Faltan argumentos.")
        printArguments()
        sys.exit(1)
    except ValueError:
        print("Error: El argumento user_agent debe ser un número entero.")
        printArguments()
        sys.exit(1)

def constructHTTPRequest(host_server, http_method, url, user_agent_choice, encoding, connection):
    # Construccion de HTTP request line
    version = "HTTP/1.1"
    request_line = http_method + " " + url + " " + version + "\r\n"

    # Construccion de HTTP header lines
    # cada parametro debe terminar con un retorno de carro
    # y un salto de linea
    host = "Host: " + host_server
    
    # User agents a escoger

    # User agent FireFox
    if user_agent_choice == 1:
        user_agent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
    # User agent Chrome
    elif user_agent_choice == 2:
        user_agent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    # User agent Microsoft Edge
    elif user_agent_choice == 3:
        user_agent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50"
    # User agent FireFox
    else:
        user_agent = "User-Agent: User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
    
    accept_encoding = "Accept-Encoding: " + encoding
    connection_header = "Connection: " + connection

    header_lines = host + "\r\n" + \
                   user_agent + "\r\n" + \
                   accept_encoding + "\r\n" + \
                   connection_header + "\r\n"
    

    # La peticion de HTTP debe terminar con un retorno de carro y
    # un salto de linea
    blank_line = "\r\n"

    # Concatenacion de cada parametro para construir la peticion de HTTP
    HTTP_request = request_line + \
                   header_lines + \
                   blank_line
    
    return HTTP_request

def TCPconnection(host_server, HTTP_request):
    # Crea un socket de TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conexion del cliente al servidor dado,
    # en el puerto 80 para HTTP
    s.connect((host_server, 80))

    # Envia la peticion HTTP al servidor
    s.send(HTTP_request.encode())

    # Mientras reciba informacion del servidor la guarda
    # en HTTP_response, e imprimira en pantalla
    while True:
        HTTP_response = s.recv(1024)
        if not HTTP_response: break
        print(HTTP_response.decode())
        
    # Una vez que la recepcion de informacion ha terminado
    # se cierra la conexion con el servidor
    s.close()

    print("\n\nConexion con el servidor finalizada\n")

printArguments()
arguments = proccessArguments()
HTTP_request = constructHTTPRequest(*arguments)
TCPconnection(arguments[0], HTTP_request)

# Para probar en Docker
#python3 /opt/clienteHTTP.py www.fciencias.unam.mx GET / 4 identity close