import socket
import sys
from random import randint

PORT = 8081
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

def numero_aleatorio():
    numero = randint(0, 99)  # El servidor elige un número aleatorio del 0 al 9
    return numero

def compara_numeros(aleatorio, numero):
    if numero == aleatorio:
        return 'Enhorabuena, has acertado'
    elif aleatorio-10<numero<aleatorio+10:
        return 'Caliente, caliente'
    elif numero>aleatorio:
        return 'Frío, frío por arriba'
    elif numero<aleatorio:
        return 'Frío, frío por abajo'

def main():
    random = numero_aleatorio()
    repetir = True
    while repetir:
        respuesta = compara_numeros(random, introducir_numero())
        print (respuesta)
        if respuesta == 'Enhorabuena, has acertado':
            repetir = False
            sys.exit(0)
        else:
            repetir = True

def process_client(clientsocket, send_message):
    send_bytes = str.encode(send_message)
    clientsocket.send(send_bytes)
    #clientsocket.close()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = IP

try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)
    random = numero_aleatorio()
    while True:
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        repetir = True
        while repetir:
            mensaje_cliente =  int(clientsocket.recv(2018).decode('utf-8'))
            mensaje_servidor = compara_numeros(random, mensaje_cliente)
            if mensaje_servidor == 'Enhorabuena, has acertado':
                repetir = False
                process_client(clientsocket,mensaje_servidor)
            else:
                process_client(clientsocket,mensaje_servidor)


except socket.error:
    print("Problems using port %i. Do you have permission?" % PORT)

except KeyboardInterrupt:
    print ('\nHa presionado CTRL+C. El programa finalizará')
