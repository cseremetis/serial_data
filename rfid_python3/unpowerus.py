import subprocess #to run bash commands

def usbon():
    bash = "sudo uhubctl -a on -p 2"
    process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)

def usboff():
    bash = "sudo uhubctl -a off -p 2"
    process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)

usboff()