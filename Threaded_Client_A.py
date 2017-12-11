# Python TCP Client A
import socket

#host = socket.gethostname()
host = '0.0.0.0'
port = 2009
BUFFER_SIZE = 2000
#MESSAGE = raw_input("tcpClientA: Enter message/ Enter exit:")
print("Client A Connected")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

while True:
    data = tcpClientA.recv(BUFFER_SIZE).decode("UTF-8")
    print(data)
    #if data is None:
    #    print("NoneType")
    #elif data:
    #    print(" Client1 received data: " + data)
    #    num = int(data) + 1
    #    print(str(num))
    #    tcpClientA.send(str(num).encode("UTF-8"))
    #MESSAGE = raw_input("tcpClientA: Enter message to continue/ Enter exit:")

#tcpClientA.close()