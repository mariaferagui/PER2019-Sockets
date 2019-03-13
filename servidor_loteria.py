import socket
from random import randint

PORT = 8085
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5


def numero_aleatorio():      # Elige aleatoriamente un número del 0 al 9
    numero = randint(0, 9)  
    return numero 

def suma_numeros (lista): # Suma los números de una lista
    suma = 0
    for item in lista: 
        numero = int (item)
        suma += numero 
    return suma

def resto_10(numero):       #Calcula el resto de dividir entre 10 un número
    resto = numero % 10
    return resto

def comparar_resto_aleatorio(resto, aleatorio): 
    if resto == aleatorio: 
        return 'TE HA TOCADO. EL NÚMERO ERA: ', aleatorio
    else: 
        return 'NO TE HA TOCADO. EL NÚMERO ERA: ', aleatorio

def process_client(clientsocket):
    aleatorio = numero_aleatorio()
    raddres_tuple = clientsocket.getpeername()
    raddres = raddres_tuple[0]    # Direccion IP remota
    lista_raddress = raddres.split('.') 
    resto = resto_10(suma_numeros(lista_raddress)) 
    send_message1,send_message2 = comparar_resto_aleatorio(resto,aleatorio)
    send_bytes1 = str.encode(send_message1)
    send_bytes2 = str.encode(str(send_message2))
    clientsocket.send(send_bytes1)
    clientsocket.send(send_bytes2)
    clientsocket.close()


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = IP

try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        process_client(clientsocket) #Envía al cliente la información necesaria

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
 
except KeyboardInterrupt:
    print ('\nHa presionado CTRL+C. El programa finalizará')
 
