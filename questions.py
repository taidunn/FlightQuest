#categories

romantic = 0
thrillseeker = 0
explorer = 0
escapist = 0
foodie = 0
social = 0
kids = 0

#question 1
def question1():
    print("Who are you traveling with?")
    print("A) Adult")
    print("B) Kids")
    print("C) Alone")
    input1 = input()
    if input1 == "B":
        global kids
        kids+=1
    else:
        global romantic, thrillseeker, explorer, escapist, foodie, social
        romantic+=1
        thrillseeker+=1
        explorer+=1
        escapist+=1
        foodie+=1
        social+=1

#question 2
def question2():
    print("Are you a Foodie?")
    print("A) Yes")
    print("B) No")
    input1 = input()
    global romantic, thrillseeker, explorer, escapist, foodie, social
    if input1 == "A":
        romantic+=1
        explorer+=1
        escapist+=1
        foodie+=2
        social+=1

#question 3
def question3():
    print("Would you like a romantic getaway?")
    print("A) Yes")
    print("B) No")
    input1 = input()
    global romantic, thrillseeker, explorer, escapist, foodie, social
    if input1 == "A":
        romantic+=2
        escapist+=1
        social+=1

#question 4
def question4():
    print("Are you a risk taker?")
    print("A) Yes")
    print("B) No")
    input1 = input()
    global romantic, thrillseeker, explorer, escapist, foodie, social
    if input1 == "A":
        thrillseeker += 2
        explorer += 1

#question 5
def question5():
    print("Would you like to see geographic landmarks?")
    print("A) Yes")
    print("B) No")
    input1 = input()
    global romantic, thrillseeker, explorer, escapist, foodie, social
    if input1 == "A":
        explorer += 2
        thrillseeker += 1
        escapist += 1

def question6():
    print("Would you enjoy minimal social interaction?")
    print("A) Yes")
    print("B) No")
    input1 = input()
    global romantic, thrillseeker, explorer, escapist, foodie, social
    if input1 == "A":
        escapist += 2
    else:
        social += 2

def category():
    #global romantic, thrillseeker, explorer, escapist, foodie, social
    #categories = [romantic, thrillseeker, explorer, escapist, foodie, social]
    #for i in categories:
     #   largest = 0
      #  if i>largest:
            #largest=i
    #chosencategory = categories.index(largest)
    #print(chosencategory)
    categories = {romantic: "romantic", thrillseeker: "thrillseeker" , explorer: "explore", escapist: "escapist" , foodie: "foodie" , social: "social"}
    print(romantic, thrillseeker, explorer, escapist, foodie, social)
    #categories.sort(reverse=True)
    #print(categories[0])

    max(categories)
    print(categories)




question1()
question2()
question3()
question4()
question5()
question6()
category()


