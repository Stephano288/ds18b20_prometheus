def measure_temp():
    dir = '/sys/bus/w1/devices/'
    device = glob.glob(dir + '28*')[0]
    sensor = device + '/w1_slave'

    f = open(sensor, 'r')
    lines = f.readlines()
    f.close()
    splitlines=lines[0].split(' ')

    #check if temp is postitive or negative
    if splitlines[1].startswith("1",0,1):
        splitlines[1]=splitlines[1].replace("0","1",1)
        negative=True
    else:
        negative=False
    #first 2 bytes represents temperature
    hexvalue='0x'+splitlines[1]+splitlines[0]
    intvalue= int(hexvalue, 16)
    if negative==True:
        return (-intvalue/16)
    else:
        return (intvalue/16)
if __name__ == '__main__':
    measure_temp()