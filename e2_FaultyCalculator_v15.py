# ===============>EXCERCISE2<===============

# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

# ===============>SOLUTION<===============
num1 = int(input("Enter 1st number:- "))
operatr = input("Enter your operator(+,-,*,/,%):- ")
num2 = int(input("Enter 2st number:- "))
if operatr == "+":
    if num1 == 56 and num2 ==9:
        print(77)
    else:
        print(num1 + num2)
elif operatr == "-":
    print(num1 - num2)
elif operatr == "*":
    if num1 == 45 and num2 ==3:
        print(555)
    else:
        print(num1 * num2)
elif operatr == "/":
    if num1 == 56 and num2 ==6:
        print(4)
    else:
        print(num1 / num2)
elif operatr == "%":
    print(num1 % num2)
else:
    print("Invalid input!")
