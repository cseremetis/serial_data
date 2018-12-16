import serial
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
#ser.write(b'hello')
cnt=0;

while True:
    # using ser.readline() assumes each line contains a single reading
    # sent using Serial.println() on the Arduino

    #reading = ser.readline()#.decode('utf-8')
    
    #reading = ser.read(1)#number is the number of bytes

    #optionally could specify a specific number of bytes for specific decoding

    # reading is a string...do whatever you want from here

    #chop reading into substring and print char by char
    #for i in range(len(reading)):
        #print(reading(i))

    #print (''.join(r'\x{02:x}'.format(ord(c)) for c in reading))


    #print(int.from_bytes(reading))
    #format(ord("c"), "x")


    #if the first one read once
    if cnt == 0:
        reading=ser.read(1)#read one byte in initially
        cnt=cnt+1
    #read until we get an ff
    while reading.encode('hex')!="ff":
        reading=ser.read(1)


    reading = ser.read(1)
    
    #print reading
    tmp=reading.encode('hex')
    print tmp
    #print type(reading)
    #print len(reading)
ser.close()


