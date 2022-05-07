# ===============>EXCERCISE2<===============

# You have to build a "Number Guessing Game," in which a winning number is set to some integer value. The 
# Program should take input from the user, and if the entered number is less than the winning number, a 
# message should display that the number is smaller and vice versa.
# Instructions:
# 1. You are free to use anything we've studied till now.
# 2. The number of guesses should be limited, i.e (5 or 9).
# 3. Print the number of guesses left.
# 4. Print the number of guesses he took to win the game.
# 5. “Game Over” message should display if the number of guesses becomes equal to 0.

# ===============>SOLUTION<===============
import random
num = random.randrange(100)
print("Let's start the game Guess The Number\n You have 9 guesses .... Good Luck")
a = 9
while a > 0:
    a = a-1

    guess = int(input("enter your guess"))
    if num > guess :
        print("your guess is lesser")
    elif num == guess:
        print("You won the game by ",a, " guesses")
        break
    else:
        print("your guess is greater")
    print("guess remain: ",a)
    if a == 0:
        print("Game over")
    else:
        pass

