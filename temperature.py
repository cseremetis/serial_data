import subprocess #to run bash commands
import time #for multithreading

#power supply functions use uhubctl
#if unavailable, run
#sudo apt-get install libusb-1.0-0-dev
#go to github.com/mvp/uhubctl and clone
#the directory

def cut_power():
    bash = "sudo uhubctl -a off -p 2"
    process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    print(output)

def enable_power():
    bash = "sudo uhubctl -a on -p 2"
    process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    print(output)


