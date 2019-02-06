import serial
import datetime
import time
import subprocess
import atexit  # make sure device shuts down properly
from .temperature import cut_power, enable_power
from .read_serial_data import reset_log, scan, start_led_thread, turn_reader_on, turn_reader_off

enable_power()  # allow power to flow to the reader
# time.sleep(5) #buffering time for power to return to port

reset_log()
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
logfile = open("logfile.txt", 'a')
cnt = 0
while True:
    turn_reader_on()
    time.sleep(1)
    turn_reader_off()
    time.sleep(2)

@atexit.register
def goodbye():
    ser.close() #shut down the com port
    cut_power() #shut down power to port on termination
    logfile.close()