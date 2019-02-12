import serial
import datetime
import time
import subprocess
import atexit  # make sure device shuts down properly
try:  # Works w/ Python 3.6 onwards
    # from .temperature import cut_power, enable_power
    from .read_serial_data import reset_log, scan, decodeBytes
except SystemError:  # Works w/ Python 3.5 and below
    from read_serial_data import reset_log, scan, decodeBytes
from gpiozero import OutputDevice, LED


# @atexit.register
def goodbye():
    print("goodbye")
    ser.close() #shut down the com port
    reader.off()
    led.off()
    cut_power() #shut down power to port on termination
    logfile.close()


# Instancing GPIO pins for LED (read indicator) and reader enable
readerPin = 26
ledPin = 16
reader = OutputDevice(readerPin)
led = LED(ledPin)
time.sleep(3)
reset_log()
# Turn on reader - enable current flow through device via MOSFET
reader.on()
enable_power()
# time.sleep(2)
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
logfile = open("logfile.txt", 'a')
cnt = 0

while True:
    # Get 30 chunks of data from the RFID reader
    if cnt != 30:
        try:
            byteList = scan(ser)
            decodeBytes(byteList, led)
        except:
            goodbye()
            exit()
        cnt = cnt+1
    else:
        ser.close()
        reader.off()
        led.on()
        time.sleep(5)  # must call python -u to enable this
        print("reloading reader")
        reader.on()
        led.off()
        time.sleep(1)  # wait for power to return to the serial port
        ser = serial.Serial('/dev/ttyACM0')
        cnt = 0
