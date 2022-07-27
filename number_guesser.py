import random
play_again = "yes"
while play_again == "yes":
    random_number = random.randint(1, 100)
    guess = 0
    guess_tracker = 0

    while guess != random_number:
        guess = int(input("What is your guess? "))
        guess_tracker = guess_tracker + 1

        if guess > random_number:
            guess = print("Guess lower")
        elif guess < random_number:
            guess = print("Guess higher")
        else:
            guess = print("Congrats, you guessed it right! ")
            print(f"It took you {guess_tracker} guesses")
            play_again = input("Would you like to play again (YES / NO)? ")

print("Okay then, goodbye. ")
