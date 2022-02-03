import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("veggiebob.student.rit.edu", 8080))

bs = s.recv(6)
print(bs)