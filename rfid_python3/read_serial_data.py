import serial
import datetime
from . import temperature
from time import sleep
from threading import Thread

# RPI 3 B+
LEDPIN = 16
ENABLEPIN = 26

# RPI 2 B
# LEDPIN = 25
# ENABLEPIN = 27

"""
def turn_led_on():
    led = LED(LEDPIN)
    led.on()
    sleep(2)
    led.off()


def start_led_thread():
    t = Thread(target=turn_led_on)
    t.start()
"""


def turn_reader_on(readergpio):
    readergpio.on()


def turn_reader_off(readergpio):
    readergpio.off()


def reset_log():
    # OPEN LOG FILE
    # clear it
    logfile = open("logfile.txt", 'w')
    logfile.close()
    # open it for appending
    logfile = open("logfile.txt", 'a')
    logfile.close()


def scan(ser):
    temp2 = 0
    cnt = 0
    byteList = []
    currByte = b''
    # Read until we get the first 'ff' - marks start of data
    # TODO - could optimize by not comparing 'ff' string and direct byte instead
    while currByte.hex() != 'ff':
        currByte = ser.read(1)
    byteList.append(currByte)
    currByte = b''
    while currByte.hex() != 'ff':
        currByte = ser.read(1)
        byteList.append(currByte)
    # Printing the line
    for byte in byteList:
        print(byte.hex(), end=' ')
    listSize = len(byteList)
    print(": %d" % listSize)
    return byteList

def decodeBytes(byteList):
    listSize = len(byteList)
    # Case 1 - Temperature Data
    if listSize == 18:
        temperature = int(byteList[14].hex(), 16)
        print("Current Reader Temperature (Celsius): %d" % temperature)
    elif listSize == 42:
        tagid = []
        tagid = byteList[22:37]
        # Printing Tag ID
        print("Tag ID: ", end='')
        for i in tagid:
            print(i.hex(), end=' ')
        print('')


def scanOLD(ser, logfile):
    temp2 = 0
    cnt = 0
    # while True:
    # CASE 0: first time through loop
    if cnt == 0:  # need read until we get an ff
        current = ''  # initialize current to empty
        while current.encode('hex') != 'ff':  # keep reading until we get ff
            current = ser.read(1)
            cnt = 2

    # CASE 1: second time current will have 'ff' from previous packet

    # MAKE THE LIST: read the whole packet into list_tmp

    # step 1: add the first ff to the list
    list_tmp=[]
    list_tmp.append(current)
    # step 2: loop through until we hit the next ff adding to list
    current='00'
    while current.encode('hex')!='ff':
        current=ser.read(1)
        list_tmp.append(current)

    #COVERT LIST TO HEX: convert the list to hex and store it in converted list
    list_converted=[]
    print(len(list_tmp), end='')
    print(": ", end='')
    for i in range(len(list_tmp)):
        list_converted.append(list_tmp[i].encode('hex'))
        #print the list out
        print(list_converted[i],end='')
    print(" : ", end='')
    print(len(list_tmp))
    #print

    ###########################################################################
    ###########################################################################
    #DECODE DATA:
    #CASE 1: temperature data length = 18
    #Case 2: read data length = 42,10
    #CASE 3: read cycle keep alive

    #print out the whole line
    #print list_converted

    #CASE 1: temperature data
    if len(list_converted)==18:
        temp=list_converted[14]
        temp2=int(temp, 16)
        print("current reader temp Celcius: ", end='')
        print(temp2)
        logfile.write("current reader temp Celcius: ")
        logfile.write(str(temp2))
        logfile.write("\n")

    #CASE 2: read data
    #if len(list_converted)==10:
        #print "tag id: ",
        #logfile.write("tag read at: ")
        #logfile.write(str(datetime.datetime.now().time()))
        #logfile.write("\n")

    #CASE 2.5: read second part of data
    if len(list_converted) == 42:
        # start_led_thread()
        tagid=[]
        tagid=list_converted[22:37]
        print("tag id: ", end='')
        print(tagid,end='')
        print(" read")
        logfile.write("tag id: ")
        logfile.write(str(tagid))
        logfile.write("\n   -read at time= ")
        logfile.write(str(datetime.datetime.now().time()))
        logfile.write("\n")
    return temp2
