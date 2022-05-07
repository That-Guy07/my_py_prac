# Quiz2-> creat a python program to declare user if he/ she can drive or not(Take input from user)
age = int(input("How old are you?"))
if age >= 125 or age <= 5 :
    print("Not a valid age")
else:
    if age > 18 :
        print("You can drive")
    elif age == 18 :
        print("Apply for Driving Licence")
    else:
        print("You can't drive")