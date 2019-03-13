import socket
import sys

IP = "127.0.0.1"
PORT = 8081

def introducir_numero():
    repetir = True
    while repetir:
        numero = input ('Introduzca un número: ')
        try:
            numero= int(numero)
            repetir = False
        except ValueError:
            repetir = True
    return numero

def enviar_mensaje(serversocket, mensaje):
    send_mensaje = str(mensaje)
    send_bytes = str(send_mensaje).encode('utf-8')
    serversocket.send(send_bytes)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))
    repetir = True
    while repetir:
        numero = introducir_numero()
        enviar_mensaje(s, numero)
        mensaje_servidor = s.recv(2048).decode('utf-8')
        print (mensaje_servidor)
        if mensaje_servidor == 'Enhorabuena, has acertado':
            repetir = False
            sys.exit(1)

except OSError:
    print("Socket already used")
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

except ConnectionRefusedError:
    print ('El servidor finalizó el programa')
    sys.exit(2)

except KeyboardInterrupt:
    print ('\nHa presionado CTRL+C. El programa finalizará')
