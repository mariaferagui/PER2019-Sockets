import socket
import sys
IP = "127.0.0.1"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

def enviar_mensaje(serversocket, mensaje):
    send_bytes = str(mensaje).encode('utf-8')
    serversocket.send(send_bytes)

try:
    s.connect((IP, PORT))
    repetir = True
    while repetir:
        mensaje = input('>>')
        mensaje_cierre = ('salir','Salir', 'SALIR')
        if mensaje in mensaje_cierre:
            enviar_mensaje(s, mensaje)
            sys.exit(1)
        else:
            enviar_mensaje(s,mensaje)
            mensaje_servidor = s.recv(2048).decode('utf-8')
            if mensaje_servidor in mensaje_cierre:
                print ('El programa finalizará')
                repetir = False
                sys.exit(2)
            else:
                print ('El mensaje del servidor es:', mensaje_servidor)


except OSError:
    print("Socket already used")
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

except ConnectionRefusedError:
    print ('El servidor salió del chat')
    sys.exit(3)

except KeyboardInterrupt:
    print ('\nHa presionado CTRL+C. El programa finalizará')
