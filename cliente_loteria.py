import socket

IP = "127.0.0.1"
PORT = 8085

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))
    print('\n',s.recv(2048).decode("utf-8"),'\n')

except OSError:
    print("Socket already used")
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

except KeyboardInterrupt:
    print ('\nHa presionado CTRL+C. El programa finalizará')


