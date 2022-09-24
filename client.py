import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(), 1234))

# full_msg = ''
# while True:
#     msg = s.recv(1024) ## Deciding how big of chunks of data you want to receive at one point in time
#     if len(msg) <= 0:
#         break
#     full_msg += msg.decode("utf-8")
# print(full_msg)