import serial
import datetime
import time
import subprocess
import read_serial_data
import temperature

reset_log()
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
temp
logfile=open("logfile.txt",'a')

while True:
    temp = scan(ser, logfile)
    if (temp >= 50):
        cut_power()
        time.sleep(15000) #probably have to call python -u to enable this
        enable_power()

logfile.close()
