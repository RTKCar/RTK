import numpy
import numpy as np


def main():

    latitude_mean_value()
    longitude_mean_value()
    altitude_mean_value()

    base_station_mean_lat_long()

def longitude_mean_value():

    longitude_list = []
    long_var = 'Longitude Data'

    with open('LogFile_RTK_test') as f:
        f = f.readlines()
        # print(f)

    for line in f:
        if line.startswith(long_var):
            longitude_list.append(line)

    tmp_list = [i.split(':')[1] for i in longitude_list]
    tmp2_list = [i.split('\n')[0] for i in tmp_list]
    mean_list = [i.split(' ')[1] for i in tmp2_list]

    mean_float_list = map(float, mean_list)
    longitude_mean = float(sum(mean_float_list)) / max(len(mean_float_list), 1)
    # numpy_mean = numpy.mean(mean_float_list)
    longitude_var = np.std(mean_float_list, ddof=0)

    # print(mean_float_list)
    print('Longitude-mean')
    print(longitude_mean)
    #print(numpy_mean)

    print('Longitude-std')
    print(longitude_var)

def latitude_mean_value():

    latitude_list = []
    lat_var = 'Latitude Data'

    with open('LogFile_RTK_test') as f:
        f = f.readlines()
        #print(f)

    for line in f:
        if line.startswith(lat_var):
            latitude_list.append(line)


    tmp_list = [i.split(':')[1] for i in latitude_list]
    tmp2_list = [i.split('\n')[0] for i in tmp_list]
    mean_list = [i.split(' ')[1] for i in tmp2_list]

    mean_float_list = map(float, mean_list)
    latitude_mean = float(sum(mean_float_list)) / max(len(mean_float_list), 1)
    #numpy_mean = numpy.mean(mean_float_list)

    latitude_var = np.std(mean_float_list, ddof=0)

    #print(mean_float_list)
    print('Latitude-mean')
    print(latitude_mean)
    #print(numpy_mean)

    print('Latitude-std')
    print(latitude_var)




def altitude_mean_value():

    altitude_list = []
    alt_var = 'Altitude Data'

    with open('LogFile_RTK_test') as f:
        f = f.readlines()
        # print(f)

    for line in f:
        if line.startswith(alt_var):
            altitude_list.append(line)

    tmp_list = [i.split(':')[1] for i in altitude_list]
    tmp2_list = [i.split('\n')[0] for i in tmp_list]
    mean_list = [i.split(' ')[1] for i in tmp2_list]

    mean_float_list = map(float, mean_list)
    altitude_mean = float(sum(mean_float_list)) / max(len(mean_float_list), 1)
    # numpy_mean = numpy.mean(mean_float_list)

    altitude_var = np.std(mean_float_list, ddof=0)

    # print(mean_float_list)
    print('Altitude-mean')
    print(altitude_mean)
    # print(numpy_mean)

    print('Altitude-variance')
    print(altitude_var)


def debugg_function():
    print("JEEEEEEW")

def base_station_mean_lat_long():
    latitude_list = []
    lat_var = 'Latitude Data'

    with open('LogFile_RTK_test') as f:
        f = f.readlines()
        # print(f)

    for line in f:
        if line.startswith(lat_var):
            latitude_list.append(line)

    tmp_list = [i.split(':')[1] for i in latitude_list]
    tmp2_list = [i.split('\n')[0] for i in tmp_list]
    mean_list = [i.split(' ')[1] for i in tmp2_list]

    mean_float_list = map(float, mean_list)
    latitude_mean = float(sum(mean_float_list)) / max(len(mean_float_list), 1)
    # numpy_mean = numpy.mean(mean_float_list)

    latitude_var = np.std(mean_float_list, ddof=0)

    # print(mean_float_list)
    print('Latitude-mean')
    print(latitude_mean)
    # print(numpy_mean)

    print('Latitude-std')
    print(latitude_var)

    longitude_list = []
    long_var = 'Longitude Data'
    #----------------------------------------SEPARATOR-------------------------------------------------

    with open('LogFile_RTK_test') as f:
        f = f.readlines()
        # print(f)

    for line in f:
        if line.startswith(long_var):
            longitude_list.append(line)

    tmp_list = [i.split(':')[1] for i in longitude_list]
    tmp2_list = [i.split('\n')[0] for i in tmp_list]
    mean_list = [i.split(' ')[1] for i in tmp2_list]

    mean_float_list = map(float, mean_list)
    longitude_mean = float(sum(mean_float_list)) / max(len(mean_float_list), 1)
    # numpy_mean = numpy.mean(mean_float_list)
    longitude_var = np.std(mean_float_list, ddof=0)

    # print(mean_float_list)
    print('Longitude-mean')
    print(longitude_mean)
    # print(numpy_mean)

    print('Longitude-std')
    print(longitude_var)

    base_station_mean_pos_for_GUI(latitude_mean, longitude_mean)



def base_station_mean_pos_for_GUI(lat, long):
    print(lat)
    print(long)


if __name__ == '__main__':
    main()