import os
import glob
import time

#credit to https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw(sensorindex):
    device_folder = glob.glob(base_dir + '28*')[sensorindex]
    device_file = device_folder + '/w1_slave'
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

