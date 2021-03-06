import serial
import datetime
import time
import subprocess
import atexit #make sure device shuts down properly
from temperature import cut_power, enable_power
from read_serial_data import reset_log, scan

enable_power() #allow power to flow to the reader
time.sleep(5) #buffering time for power to return to port

reset_log()
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
logfile=open("logfile.txt",'a')
cnt=0
while True:
    if cnt!=30:
        scan(ser, logfile)
        cnt=cnt+1
    else:
        ser.close()
        cut_power()
        time.sleep(3) #must call python -u to enable this
        print("reloading reader")
        enable_power()
        time.sleep(3) #wait for power to return to the serial port
        ser = serial.Serial('/dev/ttyACM0')
        cnt=0

@atexit.register
def goodbye():
    ser.close() #shut down the com port
    cut_power() #shut down power to port on termination
    logfile.close()