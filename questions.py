import pyinputplus as pyip
import random 

# Categories
romantic = 0
thrillseeker = 0
explorer = 0
escapist = 0
foodie = 0
social = 0

#Array lists of countries

# Question One
input1 = pyip.inputYesNo("Do you like traveling with others? (Y/N) ", limit=4)

if input1 == "yes":
    social += 3
    explorer += 2
else:
    thrillseeker += 0

#Question Two
input1 = pyip.inputYesNo("Are you a foodie? (Y/N) ", limit=4)

if input1 == "yes":
    foodie+=2
else: 
    social+=1
    romantic+=1
    explorer+=1
    escapist+=1

#Question Three
input1 = pyip.inputYesNo("Would you like a romantic getaway? (Y/N) ", limit=4)

if input1 == "yes":
    romantic+=2
else:
    escapist+=1
    social+1

#Question Four
input1 = pyip.inputYesNo("Are you a risk taker? (Y/N) ", limit=4)

if input1 == "yes":
    thrillseeker += 2
else:
    explorer += 1

# Question Five
input1 = pyip.inputYesNo("Are you a geographic landmarks? (Y/N) ", limit=4)

if input1 == "yes":
    explorer += 2
else:
    thrillseeker += 1
    escapist += 1

# Question Six
input1 = pyip.inputYesNo("Would you enjoy minimal social interaction? (Y/N) ", limit=4)

if input1 == "yes":
    escapist += 2
else:
    explorer += 1
    thrillseeker += 1

# Question Seven
input1 = pyip.inputYesNo("Have you ever been abroad? (Y/N) ", limit=4)

if input1 == "yes":
    explorer += 3
    social += 1
else:
    thrillseeker += 1

# Question Seven
input1 = pyip.inputYesNo("Could you live in another country for the rest of your life? (Y/N) ", limit=4)

if input1 == "yes":
    escapist += 3
    explorer += 2
    thrillseeker += 1
else:
    foodie += 0

#value key
categories = {romantic: "romantic", thrillseeker: "thrillseeker" , explorer: "explorer", escapist: "escapist" , foodie: "foodie" , social: "social"}

# print(romantic, thrillseeker, explorer, escapist, foodie, social)


#state result of dictionary 
catResult = (categories.get(max(categories)))
print(f"You are a/an {catResult}!")
  
france = "CDG"
mexico = "CUN"
maldives = "MLE"
costaRica = "SJC"
southAfrica = "CPT"
brazil = "MAO"
greece = "JTR"
egypt = "SPX"
mexico2 = "MID"
aruba = "AUA"
america = "HML"
finland = "RVN"
america2 = "DCA"
mexico3 = "TPQ"
japan = "ITM"
spain = "IBZ"
america3 = "MSY"
australia = "SYD"

finalromantic = ["Paris, France", "Cancun, Mexico", "Vaadhoo Island, Maldives"]
finalthrillseeker = ["San Jose, Costa Rica", "Cape Town, South Africa", "Manaus, Brazil"]
finalexplorer = ["San Torini, Greece", "Giza, Egypt", "Chichen Itza, Mexico"]
finalescapist = ["Palm Beach, Aruba", "Hawaii, USA", "Rovaniemi, Finland"]
finalfoodie = ["DC, USA", "Bondares Bay, Mexico", "Kyoto, Japan"]
finalsocial = ["Ibiza, Spain", "New Orleans, USA", "Sydney, Australia"]

    

if catResult == "romantic": 
    #randInt=math.rand(0,2)
    result = random.choice(finalromantic)
    print(f"You should travel to {result}!")
elif catResult == "thrillseeker":
    result = random.choice(finalthrillseeker)
    print(f"You should travel to {result}!")

elif catResult == "explorer":
    result = random.choice(finalexplorer)
    print(f"You should travel to {result}!")

elif catResult == "escapist":
    result = random.choice(finalescapist)
    print(f"You should travel to {result}!")

elif catResult == "foodie":
    result = random.choice(finalfoodie)
    print(f"You should travel to {result}!")

elif catResult == "social":
    result = random.choice(finalsocial)
    print(f"You should travel to {result}!")
else:
    print() 






"""
france = "CDG"
mexico = "CUN"
maldives = "MLE"
costaRica = "SJC"
southAfrica = "CPT"
brazil = "MAO"
greece = "JTR"
egypt = "SPX"
mexico2 = "MID"
aruba = "AUA"
america = "HML"
finland = "RVN"
america2 = "DCA"
mexico3 = "TPQ"
japan = "ITM"
spain = "IBZ"
america3 = "MSY"
australia = "SYD"

finalromantic = {france: "Paris, France", mexico: "Cancun, Mexico", maldives: "Vaadhoo Island, Maldives"}
finalthrillseeker = {costaRica: "San Jose, Costa Rica", southAfrica: "Cape Town, South Africa", brazil:"Manaus, Brazil"}
finalexplorer = {greece: "San Torini, Greece", egypt: "Giza, Egypt", mexico2:"Chichen Itza, Mexico"}
finalescapist = {aruba: "Palm Beach, Aruba", america: "Hawaii, USA", finland: "Rovaniemi, Finland"}
finalfoodie = {america2: "DC, USA", mexico3: "Bondares Bay, Mexico", japan: "Kyoto, Japan"}
finalsocial = {spain: "Ibiza, Spain", america3: "New Orleans, USA", australia: "Sydney, Australia"}


"""

  