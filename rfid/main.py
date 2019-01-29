import serial
import datetime
import time
import subprocess
from temperature import cut_power, enable_power
from read_serial_data import reset_log, scan

enable_power() #allow power to flow to the reader
time.sleep(3) #buffering time for power to return to port

reset_log()
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
logfile=open("logfile.txt",'a')

while True:
    temp = scan(ser, logfile)
    if (temp >= 40):
        print("high temperature detected!")
        ser.close()
        cut_power()
        time.sleep(25) #must call python -u to enable this
        print("reloading reader")
        enable_power()
        time.sleep(3) #wait for power to return to the serial port
        ser = serial.Serial('/dev/ttyACM0')

cut_power() #shut down power to port on termination
logfile.close()
