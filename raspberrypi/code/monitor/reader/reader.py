import time

#credit to https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/
from reader.ds18b20client import read_temp_raw


def read_temp(sensorindex):
    lines = read_temp_raw(sensorindex)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(sensorindex)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
