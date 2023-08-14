import random


def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
            (user == "paper" and computer == "rock") or \
            (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    print("Let's play Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


#play_game()

choice = "C"
while (choice=="C" or choice=="c"):
    choice = str(input("Enter C to continue"))
    if choice == 'C' or choice == 'c':
        play_game()
print("\nBye")
