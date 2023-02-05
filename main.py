import pyinputplus as pyip
import time
import requests
import random 
import colorama
from colorama import Fore

print("Hello my name is Pyotr I am your virtual travel assistant.")

name = pyip.inputStr(prompt = "What is your name? ", default="User", limit = 4)
print("Hello", name, ".")

def questions():
    # Categories
    romantic = 0
    thrillseeker = 0
    explorer = 0
    escapist = 0
    foodie = 0
    social = 0
    
    #Array lists of countries

    # Question One 
    input1 = pyip.inputYesNo(Fore.YELLOW +"Do you like traveling with others? (Y/N)", limit=4)
    
    if input1 == "yes":
        social += 2
        explorer += 1
    else:
        thrillseeker += 0
        
    #Question Two
    input1 = pyip.inputYesNo(Fore.YELLOW +"Are you a foodie? (Y/N) ", limit=4)
    
    if input1 == "yes":
        foodie+=2
    else: 
        social+=1
        romantic+=1
        explorer+=1
        escapist+=1

    #Question Three
    input1 = pyip.inputYesNo(Fore.YELLOW +"Would you like a romantic getaway? (Y/N) ", limit=4)

    if input1 == "yes":
        romantic+=2
    else:
        escapist+=1
        social+1

    #Question Four
    input1 = pyip.inputYesNo(Fore.YELLOW +"Are you a risk taker? (Y/N) ", limit=4)

    if input1 == "yes":
        thrillseeker += 2
    else:
        explorer += 1

    # Question Five
    input1 = pyip.inputYesNo(Fore.YELLOW +"Are you interested in geographic landmarks? (Y/N) ", limit=4)

    if input1 == "yes":
        explorer += 2
    else:
        thrillseeker += 1
        escapist += 1

    # Question Six
    input1 = pyip.inputYesNo(Fore.YELLOW +"Would you enjoy minimal social interaction? (Y/N) ", limit=4)

    if input1 == "yes":
        escapist += 2
    else:
        explorer += 1
        thrillseeker += 1

    # Question Seven
    input1 = pyip.inputYesNo(Fore.YELLOW +"Have you ever been abroad? (Y/N) ", limit=4)

    if input1 == "yes":
        explorer += 2
        social += 1
    else:
        thrillseeker += 1

    # Question Seven
    input1 = pyip.inputYesNo(Fore.YELLOW +"Could you live in another country for the rest of your life? (Y/N) ", limit=4)

    if input1 == "yes":
        escapist += 2
        explorer += 2
        thrillseeker += 1
    else:
        foodie += 0

    #value key
    categories = {romantic: "romantic", thrillseeker: "thrillseeker" , explorer: "explorer", escapist: "escapist" , foodie: "foodie" , social: "social"}

    #state result of dictionary 
    catResult = (categories.get(max(categories)))
    print(f"You're travel personality is {catResult}!")
    

    countries = ["Paris, France", "Cancun, Mexico", "Vaadhoo Island, Maldives", "San Jose, Costa Rica","Cape Town, South Africa", "Manaus, Brazil", "SanTorini, Greece", "Giza, Egypt", "Chichen Itza, Mexico", "Palm Beach, Aruba", "Hawaii, America", "Ravanieni, Finland", "Washington DC, America","Bondores Bay, Mexico","Kyoto, Japan", "Ibiza, Spain", "New Orleans, America", "Sydney, Australia"]
    airport = ["CDG", "CUN", "MLE", "SJC", "CPT", "MAO", "JTR", "SPX", "MID", "AUA", "HML", "RVN", "DCA", "TPQ", "ITM", "IBZ", "MSY", "SYD" ]

    #API stuff
    global desCode
    if catResult == "romantic":
        randnum = random.randint(0,2)
        #global descountry
        descountry = countries[randnum]
        # global desCode
        desCode = airport[randnum]
        print(f"Your country is {descountry}, and your airport is {desCode}\n\n")

    elif catResult == "thrillseeker":
        randnum = random.randint(3,5)
        #global descountry
        descountry = countries[randnum]
        # global desCode
        desCode = [randnum]
        print(f"Your country is {descountry}, and your airport is {desCode}\n\n")
                
    elif catResult == "explorer":
        randnum = random.randint(6,8)
        #global descountry
        descountry = countries[randnum]
        # global desCode
        desCode = airport[randnum]
        print(f"Your country is {descountry}, and your airport is {desCode}\n\n")
            
    elif catResult == "escapist":
        randnum = random.randint(9,11)
        #global descountry
        descountry = countries[randnum]
        # global desCode
        desCode = airport[randnum]
        print(f"Your country is {descountry}, and your airport is {desCode}\n\n")
            
    elif catResult == "foodie":
        randnum = random.randint(12,14)
        #global descountry
        descountry = countries[randnum]
        # global desCode
        desCode = airport[randnum]
        print(f"Your country is {descountry}, and your airport is {desCode}\n\n")
            
    elif catResult == "social":
        randnum = random.randint(15,17)
        #global descountry
        descountry = countries[randnum]
        # global desCode
        desCode = airport[randnum]   
        print(f"Your country is {descountry}, and your airport is {desCode}\n\n")

def verify():
    print("Pytor is compiling your information please wait.")
    print()
    print("Let's make sure we have this right... \n{} I will need you to verify the information below.\n\n I have {} adult(s) in attendance. \n I have {} children in attendance. \n I have {} infants in attendance. \n Lastly I have your departure date as {} and your return date as {}.".format(name,numAdults,numChildren,numInfants,startTravel,endTravel))
    
    isCor = pyip.inputYesNo("Is all of this information correct? ", default="yes")
    if (isCor == "no"):
        travel_info()
    else:
        print("Moving onto questions.")
        questions()

def start_over():
    print("{} we will need to start over please wait...".format(name))
    print()
    travel_info()

def travel_info():
    global codeAirport
    codeAirport = pyip.inputStr(prompt="%s What is your 3 letter airport code " %name, default='ATL')
    print()
    global numAdults
    numAdults = pyip.inputInt(prompt="%s how many adults are attending? " %name, default=1, limit=4)
    print()
    global numChildren
    numChildren = pyip.inputInt(prompt="{} alright so there are {} adult attending how many children aged 2 and up are attending? ".format(name, numAdults), default=0, limit=4)
    print()
    global numInfants
    numInfants = pyip.inputInt(prompt="{} currently I have {} adults and {} children how many infants aged 0-1 are attending? ".format(name,numAdults,numChildren), default=0, limit=4)
    print()
    global startTravel
    startTravel = pyip.inputDate(prompt="{} what is your planned departure date for your travel? (MM/DD/YY)".format(name))
    startTravel = startTravel.strftime("%Y-%m-%d")
    print()
    global endTravel
    endTravel = pyip.inputDate(prompt="{} what is your planned return date for your travel? (MM/DD/YY)".format(name))
    endTravel = endTravel.strftime("%Y-%m-%d")
    print()
    verify()

global desCode
global codeAirport
global numAdults 
global numChildren
global numInfants
global startTravel
global endTravel


travel_info()

API = '63de932205f059ece5d77f5f'

print("Checking for flights between {} and {}".format(codeAirport, desCode))
print("If there is no response we couldn't find any matches.\n\n")

response = requests.get("https://api.flightapi.io/roundtrip/{}/{}/{}/{}/{}/{}/{}/{}/Economy/USD".format(API,codeAirport,desCode,startTravel,endTravel,numAdults,numChildren,numInfants))
flight = response.json()
totalAmount = (flight['fares'][0]['price']['totalAmountUsd'])
APIadults = (flight['search']['adultsCount'])
APIchild = (flight['search']['childrenCount'])
APIinfants = (flight['search']['infantsCount'])
APIcabin = (flight['search']['cabin'])
APIflighttime = (flight['legs'][0]['duration'])
APItype = (flight['legs'][0]['stopoverCode'])
totAnC = numAdults + numChildren
totSouls = numAdults + numChildren + numInfants

print("{} you have a total of {} on this trip. \n {} of them are under the age of two. Two and under fly free! \n Calculating prices please wait...\n".format(name,numChildren,numInfants))


#Total Price From API
totalAmount=(flight['fares'][0]['price']['totalAmountUsd'])
print()
print(totalAmount)
print()
perPerson=(totalAmount/totAnC)

totAdult = (perPerson * APIadults)
totChildren = (perPerson * APIchild)

print("Summary of Results Generating")
print("The price per person is {} for a total of {}. \n Children under the age of two fly free you have {} in this category.".format(perPerson,totalAmount,APIinfants))
print("It will cost ${} for all of the adults and ${} for all of the children.".format(totAdult,totChildren))
print("You will be flying on a {} flight and the flight time is {}. This flight is a {} flight.".format(APIcabin,APIflighttime,APItype))
print("The total number of people you're scheduling a flight for is {}".format(totSouls))


print("\n\n View your flight here:")
print(flight['fares'][0]['handoffUrl'])

