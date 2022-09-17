import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5) ## Means the server is going to support a queue of 5 requests
while True:
    clientsocket, address = s.accept() ## Storing the client socket so that you can send information to it later
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server", "utf-8")) ## Sending information to the client socket
    clientsocket.close()