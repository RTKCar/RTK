import socket

def main():

    host = '192.168.82.34'
    port = 5000

    s = socket.socket()
    s.connect((host, port))


    message = raw_input("--> ")

    while message != 'q':
        s.send(message)
        server_data = s.recv(1024)
        print('Recived from Server ' + str(server_data))
        message = raw_input("--> ")
    s.close()


if __name__ == '__main__':
    main()