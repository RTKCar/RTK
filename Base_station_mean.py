import numpy


def main():

    #debugg_function()
    latitude_mean_value()
    longitude_mean_value()
    altitude_mean_value()

def longitude_mean_value():

    longitude_list = []
    long_var = 'Longitude Data'

    with open('LogFile_04') as f:
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

    # print(mean_float_list)
    print('Longitude-mean')
    print(longitude_mean)
    #print(numpy_mean)

def latitude_mean_value():

    latitude_list = []
    lat_var = 'Latitude Data'

    with open('LogFile_04') as f:
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

    #print(mean_float_list)
    print('Latitude-mean')
    print(latitude_mean)
    #print(numpy_mean)


def altitude_mean_value():

    altitude_list = []
    alt_var = 'Altitude Data'

    with open('LogFile_04') as f:
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

    # print(mean_float_list)
    print('Altitude-mean')
    print(altitude_mean)
    # print(numpy_mean)


def debugg_function():
    print("JEEEEEEW")

if __name__ == '__main__':
    main()