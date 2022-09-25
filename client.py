import socket
import select

"""
Steps to create a new socket program that receives a message from the server:
1. create the client socket -> socket.socket(socket_family, socket_type)
2. connect to the server socket by connecting to the same host/port -> host.connect( (host, port) )
3. receive the data being sent by the server -> client.recv(amount of data in bytes)
4. assign this received data to a var
5. close the connection
6. print the var
"""

IP = socket.gethostname()
port = 1234

# 1. Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to the server socket
client_socket.connect( (IP, port) )

# 3. Need to RECEIVE the message and bind this message to a variable
temp_msg_holder = client_socket.recv(1024)
print(temp_msg_holder.decode())

# 4. Then close the connection to (for now) ensure the server doesn't run forever
client_socket.close()

