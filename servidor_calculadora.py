import socket
import sys

PORT = 8080
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

def suma(numero1,numero2):
    return numero1 + numero2
def resta(numero1,numero2):
    return numero1 - numero2
def multiplicacion(numero1,numero2):
    return numero1 * numero2
def division(numero1,numero2):
    try:
        resultado = numero1/numero2
        return resultado
    except ZeroDivisionError:
        return 'La división entre 0 no está permitida'
def main(opcion_menu, numero1, numero2):
    if opcion_menu == 1:
        resultado = suma(numero1,numero2)
    if opcion_menu == 2:
        resultado = resta(numero1,numero2)
    if opcion_menu == 3:
        resultado = multiplicacion(numero1,numero2)
    if opcion_menu == 4:
        resultado = division(numero1,numero2)
    return resultado


def process_client(clientsocket,mensaje):
    try:
        opcion, numero1, numero2 = mensaje.split('-')
        message = main (int(opcion),float(numero1),float(numero2))
        send_bytes = str.encode (str(message))
        clientsocket.send(send_bytes)
        return True
    except ValueError:
        return False




# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)
    while True:
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        repetir = True
        while repetir:
            mensaje = clientsocket.recv(2048).decode('utf-8')
            resultado = process_client(clientsocket,mensaje)
            if resultado == True:
                repetir = True
            else:
                repetir = False
                clientsocket.close()

except socket.error:
    print("Problems using port %i. Do you have permission?" % PORT)

except KeyboardInterrupt:
    print ('\nHa presionado CTRL+C. El programa finalizará')
    sys.exit(0)
