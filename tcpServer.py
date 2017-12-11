import socket
import pynmea2
import logging

def main():

    print('Init the server and TCP protocol')
    logging.basicConfig(filename='LogFile_27', level=logging.INFO, format='%(message)s')
    
    host = 'localhost'
    port = 5001
    
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    
    connection, addr = s.accept()
    print('Connection from: ' + str(addr))
    
    while True:
        client_data = connection.recv(1024)
        if not client_data:
            print('No data from Client was recived')
            break
        if client_data:
                #print('This is Data from Rtkrcv(NMEA-messages)')
                nmea_list = str(client_data).split("\r\n")
                for nmea_data in nmea_list:
                    if nmea_data.startswith('$GPGGA'):
                        parse_msg = pynmea2.parse(nmea_data)
                        print(parse_msg)
                        print('Lat: ' + parse_msg.data[1])
                        print('Lat_dir: ' + parse_msg.data[2])
                        print('Long: ' + parse_msg.data[3])
                        print('Long_dir: ' + parse_msg.data[4])
                        print('Altitude: ' + parse_msg.data[8])
                        logging.info('Latitude Data: {}'.format(str(parse_msg.data[1])))
                        logging.info('Longitude Data: {}'.format(str(parse_msg.data[3])))
                        logging.info('Altitude Data: {}'.format(str(parse_msg.data[8])))
                        print("************")
                print(str(client_data))
                print('Below this line is parsed NMEA-messages')
                parseMsg = pynmea2.parse(client_data)
                print(parseMsg)
    connection.close()
    debugg_function()

def debugg_function():
    print("DEBUGG")
    
if __name__ == '__main__':
    main()
