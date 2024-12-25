import random

print("Welcome to the game!")


all_choices = ("r", "s", "p")
emoji = {"r": "🥌", "p": "📃", "s": "✂"}


def get_users_choice():
    while True:
        user_choice = input("Rock, Paper or Scissors? (r/p/s) ").lower()
        if user_choice in all_choices:
            return user_choice
        else:
            print("Invalid choice! ")


def display_choices(user_choice, computer_choice):
    print(f"you chose {emoji[user_choice]}")
    print(f"computer chose {emoji[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "p" and computer_choice == "r")
        or (user_choice == "s" and computer_choice == "p")
    ):
        print("You won!")
    else:
        print("You lost the game!")


def play_game():
    while True:
        user_choice = get_users_choice()

        computer_choice = random.choice(all_choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue?(y/n) ").lower()
        if should_continue == "n":
            print("Okay, bye!😊")
            break


play_game()
