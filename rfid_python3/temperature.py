import subprocess #to run bash commands
import time #for multithreading

#power supply functions use uhubctl
#if unavailable, run
#sudo apt-get install libusb-1.0-0-dev
#go to github.com/mvp/uhubctl and clone
#the directory

def cut_power():
    #location 1-1, port 4; "-a off" sends the command to cut power
    bash = "sudo uhubctl -l1-1 -p 4 -a off"
    process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    print(output)

def enable_power():
    #location 1-1, port 4; "-a on" sends the command to enable power
    bash = "sudo uhubctl -l1-1 -p 4 -a on"
    process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    print(output)


