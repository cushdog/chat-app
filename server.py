import socket
import select

"""
Steps to create a new socket program that sends a message to the client:
1. create the server socket -> socket.socket(socket_family, socket_type)
2. bind the socket to a specified host/port (declare a string that stores the host before hand) -> server socket.bind( (host, port) )
    PORT NEEDS TO BE AN INT
3. listen for connections to the server socket -> server_socket.listen( maximum number of connections)
    puts the socket in a "ready to accept connections" state
4. accept incoming connections -> socket
5. send custom messages to incoming connections
"""

IP = socket.gethostname()
port = 1234
# 1. Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind the socket to a specific address, in the format: (host, port)
server_socket.bind( (IP, port ) )

# 3. Listen for connections
server_socket.listen()
while True:
    # 4. Accept incoming connections, general convention is to say it like this
    client_sock, client_address = server_socket.accept()

    # 5. Send message with CLIENT . send (message.encode())
    client_sock.send("gahdayum".encode())
