import socket
import sys

IP = "127.0.0.1"
PORT = 8080

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print(s)
def menu():
    print ('Bienvenido a la calculadora')
    print ('0. Salir')
    print ('1. Suma')
    print ('2. Resta')
    print ('3. Multiplicación')
    print ('4. División')


def opcion():
    repetir = True
    while repetir:
        opcion = input ('Introduzca una opción: ')
        try:
            opcion = int(opcion)
            if opcion in [0,1,2,3,4]:
                repetir = False
        except ValueError:
            repetir = True
    return opcion

def introducir_numero():
    repetir = True
    while repetir:
        numero = input ('Introduzca un número: ')
        try:
            numero= float(numero)
            repetir = False
        except ValueError:
            repetir = True
    return numero

def mandar_mensaje(serversocket,opcion, numero1,numero2):
    message = str(opcion_menu)+'-'+str(numero1)+'-'+str(numero2)
    send_bytes = str(message).encode('utf-8')
    serversocket.send(send_bytes)


try:
    s.connect((IP, PORT))
    menu()
    repetir = True
    while repetir:
        opcion_menu = opcion()
        if opcion_menu != 0:
           mandar_mensaje(s,opcion_menu,introducir_numero(),introducir_numero())
           print('\nEl resultado es: ', s.recv(2048).decode("utf-8"),'\n')
        else:
           print ('Saliendo...')
           sys.exit(0)



except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))


except KeyboardInterrupt:
    print ('\nHa presionado CTRL+C. El programa finalizará')
    sys.exit(1)
