# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from datetime import datetime

from localstore.localstore import writelocal
from reader.reader import read_temp
from remotestore.remotestore import writeremote,disconnect


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


temp0 = read_temp(0)
temp1 = read_temp(1)
timestamp = time.time()
writelocal(timestamp, temp0)
writelocal(timestamp, temp1)
writeremote(timestamp, [temp0, temp1])
disconnect()
