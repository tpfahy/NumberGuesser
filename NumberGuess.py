import random as r

print("Hello! Welcome to the number guessing game")
player = input("Please tell me what your name is?: ")
print(f"Excellent, thank you. {player} what range of numbers would you like to guess?")
number = 0
while number < 2:

    try:
        number = input("Please give a number greater than 2 (no decimals)")
    except Exception:
        print("Please try again to enter a valid number")

guesses = 0
while guesses < 1:
    try:
        guesses = int(input("Please tell me how many guesses you would like to have to get the number correct: "))
    except Exception:
        print("Please give a valid number")

randomNumber = r.randint(1, number)

for i in range(guesses):
    playerGuess = "Guess a number: "
    if playerGuess == randomNumber:
        print(f"You got it in {i + 1} guesse(s)!")
        break
    elif playerGuess > randomNumber:
        print("Lower")
    else:
        print("Higher")
