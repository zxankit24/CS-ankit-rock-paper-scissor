import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("Rock, Paper, Scissors")
        print("Enter your choice: ")
        user_choice = input().lower()

        while user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input().lower()

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print("User score:", user_score)
        print("Computer score:", computer_score)

        print("Do you want to play again? (yes/no)")
        play_again = input().lower()

        if play_again != "yes":
            break

play_game()
