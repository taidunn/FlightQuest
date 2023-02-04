def augustau():
    # Insert picture of school here

    # Question to user
    question1 = "What school is this?"
    print(question1)

    # 3 tries
    value = 3
    input1 = str(input())
    while value >= 0:
        if input1 == "Augusta University":
            return True
        else:
            value -= 1


