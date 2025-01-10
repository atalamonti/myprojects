#Angelo Talamonti
#1/6#
#Rock Paper Scissors

#init
import random
#Function
def rps():
    wins = 0
    losses = 0
    draws = 0
    while True:
        print("Welcome to Rock Paper Scissors! ")
        ans = input("Please select your input as rock paper or scissors!")
        comp = random.randint(1,3)
        if ans == "rock" and comp == 1:
            print("draw...")
            draws = draws + 1
            print("Wins:" + str(wins), "Losses:" + str(losses), "Draws:" + str(losses))
        elif ans == "rock" and comp == 2:
            print("You Lose. Paper Beats rock...")
            losses = losses + 1
            print("Wins:" + str(wins), "Losses:" + str(losses), "Draws:" + str(losses))
        elif ans == "rock" and comp == 3:
            print("You win! Rock beats scissors...")
            wins = wins + 1
            print("Wins:" + str(wins), "Losses:" + str(losses), "Draws:" + str(losses))
        elif ans == "paper" and comp == 1:
            print("You win! Paper beats rock...")
            wins = wins + 1
            print("Wins:" + str(wins), "Losses:" + str(losses), "Draws:" + str(losses))
        elif ans == "paper" and comp == 2:
            print("Draw...")
            draws = draws + 1
            print("Wins:" + str(wins), "Losses:" + str(losses), "Draws:" + str(losses))
        elif ans == "paper" and comp == 3:
            print("You lose. Scissors beats paper...")
            losses = losses + 1
            print("Wins:" + str(wins), "Losses:" + str(losses), "Draws:" + str(losses))
        elif ans == "scissors" and comp == 1:
            print("You lose. Rock beats scissors")
            losses = losses + 1
            print("Wins:" + str(wins), "Losses:" + str(losses), "Draws:" + str(losses))
        elif ans == "scissors" and comp == 2:
            print("You win! Scissors beats paper")
            wins = wins + 1
            print("Wins:" + str(wins), "Losses:" + str(losses), "Draws:" + str(losses))
        elif ans == "scissors" and comp == 3:
            print("Draw...")
            draws = draws + 1
            print("Wins:" + str(wins), "Losses:" + str(losses), "Draws:" + str(losses))
        game = input("Would you like to play again?")
        if game == "yes":
            "Print you are playing again"
        elif game == "no":
            break


#Main
rps()
