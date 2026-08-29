import random

def guessing_game():
    print("====================================")
    print("      WELCOME TO NUMBER GUESS GAME  ")
    print("====================================")
    print("Guess the number between 1 to 100")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too LOW! Try again ⬆️")
            elif guess > secret_number:
                print("Too HIGH! Try again ⬇️")
            else:
                print("====================================")
                print(f" CONGRATS! You guessed it in {attempts} attempts 🎉")
                print("====================================")
                break
        except ValueError:
            print("Please enter a valid number!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        guessing_game()
    else:
        print("Thanks for playing! Bye 👋")

guessing_game()
