import serial

ser = serial.Serial('/dev/ttyACM1')
print(ser.name)
ser.close()