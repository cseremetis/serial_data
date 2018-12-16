# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 17:58:33 2018

@author: chris
"""

import subprocess #to run bash commands
import time #for multithreading

def cut_power():
    #using uhubctl
    #if unavailable, run
    #sudo apt-get install libusb-1.0-0-dev
    bash = "sudo uhubctl -a off -p 2"
    process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    print(output)

cut_power()
time.sleep(10000)