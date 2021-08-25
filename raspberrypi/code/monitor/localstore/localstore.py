import time


def writelocal(timestamp, reading):
    print(timestamp, reading)
    with open(f"/home/pi/Documents/readings/reading.txt", "a") as myfile:
        myfile.write(f"{time.time()},{reading},{timestamp}\n")
