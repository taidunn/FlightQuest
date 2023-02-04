import pyinputplus as pyip
import time

print("Hello my name is Pyotr I am your virtual travel assistant.")

name = pyip.inputStr(prompt = "What is your name? ", default="User", limit = 4)
print("Hello", name, ".")

def verify():
    print("Pytor is compiling your information please wait.")
    print()
    time.sleep(10)
    print("Let's make sure we have this right... \n{} I will need you to verify the information below.\n\n I have {} adult(s) in attendance. \n I have {} children in attendance. \n I have {} infants in attendance. \n Lastly I have your departure date as {} and your return date as {}.".format(name,numAdults,numChildren,numInfants,startTravel,endTravel))
    
    isCor = pyip.inputYesNo("Is all of this information correct? ", default="yes")
    if (isCor == "no"):
        travel_info()
    else:
        print("Moving onto questions.")

def start_over():
    print("{} we will need to start over please wait...".format(name))
    print()
    time.sleep(10)
    travel_info()

def travel_info():
    global numAdults
    numAdults = pyip.inputInt(prompt="%s how many adults are attending? " %name, default=1, limit=4)
    print()
    global numChildren
    numChildren = pyip.inputInt(prompt="{} alright so there are {} adult attending how many children aged 3 and up are attending? ".format(name, numAdults), default=0, limit=4)
    print()
    global numInfants
    numInfants = pyip.inputInt(prompt="{} currently I have {} adults and {} children how many infants aged 0-2 are attending? ".format(name,numAdults,numChildren), default=0, limit=4)
    print()
    global startTravel
    startTravel = pyip.inputDate(prompt="{} what is your planned departure date for your travel?".format(name))
    print()
    global endTravel
    endTravel = pyip.inputDate(prompt="{} what is your planned return date for your travel?".format(name))
    print()
    verify()

global numAdults 
global numChildren
global numInfants
global startTravel
global endTravel

travel_info()