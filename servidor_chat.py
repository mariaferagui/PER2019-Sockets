import socket

PORT = 8080
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

def process_client(clientsocket, send_message):
    send_bytes = str.encode(send_message)
    clientsocket.send(send_bytes)
    #clientsocket.close()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = IP

try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        repetir = True
        while repetir:
            mensaje_cliente = clientsocket.recv(2018).decode('utf-8')
            if mensaje_cliente in ('salir','Salir', 'SALIR'):
                print ('El cliente salió')
                clientsocket.close()
                repetir = False
            else:
                print ('El mensaje del cliente es:', mensaje_cliente )
                mensaje_servidor = input('>>')
                if mensaje_servidor in ('salir','Salir', 'SALIR'):
                    process_client(clientsocket,mensaje_servidor)
                    clientsocket.close()
                    repetir = False
                else:
                    process_client(clientsocket,mensaje_servidor)



except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)

except KeyboardInterrupt:
    print ('\nHa presionado CTRL+C. El programa finalizará')
