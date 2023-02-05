import pyinputplus as pyip

# Categories
romantic = 0
thrillseeker = 0
explorer = 0
escapist = 0
foodie = 0
social = 0

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


categories = {romantic: "romantic", thrillseeker: "thrillseeker" , explorer: "explore", escapist: "escapist" , foodie: "foodie" , social: "social"}
# print(romantic, thrillseeker, explorer, escapist, foodie, social)

print(categories.get(max(categories)))
