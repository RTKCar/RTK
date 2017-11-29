import socket
from threading import Thread
import pynmea2
import logging
from SocketServer import ThreadingMixIn


# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New server socket thread started for " + ip + ":" + str(port)

    def run(self):
        while True:
            data = conn.recv(2048)
            #print "Server is received data:"
            #print(data)
            if data:
                nmea_list = str(data).split("\r\n")
                for nmea_data in nmea_list:
                    if nmea_data.startswith('$GPGGA'):
                        parse_msg = pynmea2.parse(nmea_data)
                        #print(parse_msg)
                        print('Lat: ' + parse_msg.data[1])
                        print('Lat_dir: ' + parse_msg.data[2])
                        print('Long: ' + parse_msg.data[3])
                        print('Long_dir: ' + parse_msg.data[4])
                        print('Altitude: ' + parse_msg.data[8])
                        print("************")
            #MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            #if MESSAGE == 'exit':
                #break
            #conn.send('GINI THE JEW')


# Multithreaded Python server : TCP Server Socket Program Stub
#HH-netlogin PI: 192.168.80.95
TCP_IP = '0.0.0.0'
#TCP_IP = 'localhost'
#TCP_IP = '192.168.81.191'
TCP_PORT = 2008
BUFFER_SIZE = 1024  # Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(4)
    print "Multithreaded Python server : Waiting for connections from TCP clients..."
    (conn, (ip, port)) = tcpServer.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()


print('DEBUGGZ')