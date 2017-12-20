import socket
import pynmea2
import logging

def main():

    print('Init the server and TCP protocol')

    logging.basicConfig(filename='LogFile_RTK_test', level=logging.INFO, format='%(message)s')

    host = 'localhost'
    port = 2008

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    connection, addr = s.accept()

    streamreader = pynmea2.NMEAStreamReader()

    print('Connection from: ' + str(addr))

    while True:
        client_data = connection.recv(1024)
        #print(client_data)
        if not client_data:
            print('No data from Client was recived')
            break
        if client_data:
            for nmea_data in streamreader.next(client_data):
                #print(nmea_data)
                #GPGGA - essential fix data which provide 3D location and accuracy data.
                if str(nmea_data).startswith('$GPGGA'):

                    parse_msg = pynmea2.parse(str(nmea_data))
                    fix_state = parse_msg.data[4]
                    print(fix_state, " jalla")

                    print('-----DATA INFORMATION----')
                    print("Latitude: ", str(parse_msg.latitude))
                    print("Longitude: ", str(parse_msg.longitude))
                    print("Altitude: ", str(parse_msg.altitude))
                    print('-----      END     -----')

                    ##---------------Uncomment to logg the data--------------------------
                    logging.info('Latitude Data: {}'.format(str(parse_msg.latitude)))
                    logging.info('Longitude Data: {}'.format(str(parse_msg.longitude)))
                    logging.info('Altitude Data: {}'.format(str(parse_msg.altitude)))
                    logging.info('Fix State: {}'.format(str(fix_state)))


                    #---------------Send data back to client--------------------------
                    #client_data = str(client_data).upper()
                    #print('Sending data to client ' + str(client_data))
                    #connection.send(client_data)
    connection.close()
    debugg_function()


def debugg_function():
    print("DEBUGG")



if __name__ == '__main__':
    main()
