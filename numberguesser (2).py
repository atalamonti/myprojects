#Number guessing game
#Angelo Talamonti
11/11
#Init
import random
#functions
def guessing_game():
    print("In this game you must guess the same number as the computer. The number is between 0 and 10")
    number = random.randint(0,10)
    ans = int(input("Guess the number!"))
    if number == ans:
        print("You guessed the correct number!")
    else:
        print("Incorrect, the correct number was:")
        print(number)
#main
guessing_game()
