import serial
import datetime
import temperature
from gpiozero import LED
from time import sleep
from threading import Thread

def turn_led_on():
    led = LED(25)
    led.on()
    sleep(2)
    led.off()

def start_led_thread():
    t = Thread(target=turn_led_on)
    t.start()

def reset_log():
    #OPEN LOG FILE
    #clear it
    logfile=open("logfile.txt",'w')
    logfile.close()
    #open it for appending
    logfile=open("logfile.txt",'a')
    logfile.close()

def scan(ser, logfile):
    temp2 = 0
    cnt = 0
    #while True:
    #CASE 0: first time through loop
    if cnt == 0:#need read until we get an ff
        current=''#initialize current to empty
        while current.encode('hex')!='ff':#keep reading until we get ff
            current=ser.read(1)
            cnt=2

#CASE 1: second time current will have 'ff' from previous packet

#MAKE THE LIST: read the whole packet into list_tmp
#	step 1: add the first ff to the list
    list_tmp=[]
    list_tmp.append(current)
#	step 2: loop through until we hit the next ff adding to list
    current='00'
    while current.encode('hex')!='ff':
        current=ser.read(1)
        list_tmp.append(current)

    #COVERT LIST TO HEX: convert the list to hex and store it in converted list
    list_converted=[]
    print len(list_tmp),
    print ": ",
    for i in range(len(list_tmp)):
        list_converted.append(list_tmp[i].encode('hex'))
        #print the list out
        print list_converted[i],
    print " : ",
    print len(list_tmp)
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
        print "current reader temp Celcius: ",
        print temp2,
        print
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
    if len(list_converted)==42:
        start_led_thread()
        tagid=[]
        tagid=list_converted[22:37]
        print "tag id: ",
        print tagid,
        print " read"
        logfile.write("tag id: ")
        logfile.write(str(tagid))
        logfile.write("\n   -read at time= ")
        logfile.write(str(datetime.datetime.now().time()))
        logfile.write("\n")
    return temp2
