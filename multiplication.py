#Angelo Talamonti
#8/1
#Multiplication quiz

#init
import random

#functions
def quiz():
    print("Welcome to the Multiplication Quiz!")
    print("You will answer 5 multiplication problems. Let's begin!")

    score = 0


    for i in range(5):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print(f"Question {i + 1}: What is {num1} x {num2}?")
        user_answer = int(input("Your answer: "))
        correct_answer = num1 * num2
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {correct_answer}.")

    print(f"Quiz complete! Your final score is {score} out of 5.")


#main
quiz()
