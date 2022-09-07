import random

player_hand = ""
computer_hand = ""
play_again = "y"

CHOICES = ["rock", "paper", "scissors"]

print("\nWelcome to Rock Paper Scissors!")

while play_again == "y":
    choice = input("\nENTER YOUR CHOICE (rock, paper, or scissors): ").lower()
    if choice not in CHOICES:
        print("Invalid selection, try again.")
    else:
        player_hand = choice
        computer_hand = random.choice(CHOICES)
        if player_hand == "rock":
            if computer_hand == "paper":
                print(f"\nComputer chooses {computer_hand}.")
                print("Paper covers rock, you lose!")
            elif computer_hand == "scissors":
                print(f"\nComputer chooses {computer_hand}.")
                print("Rock smashes scissors, you win!")
            else:
                print(f"\nComputer chooses {computer_hand}.")
                print("You both chose rock, you tied!")
        elif player_hand == "paper":
            if computer_hand == "scissors":
                print(f"\nComputer chooses {computer_hand}.")
                print("Scissors cut paper, you lose!")
            elif computer_hand == "rock":
                print(f"\nComputer chooses {computer_hand}.")
                print("Paper covers rock, you win!")
            else:
                print(f"\nComputer chooses {computer_hand}.")
                print("You both chose paper, you tied!")
        elif player_hand == "scissors":
            if computer_hand == "rock":
                print(f"\nComputer chooses {computer_hand}.")
                print("Rock smashes scissors, you lose!")
            elif computer_hand == "paper":
                print(f"\nComputer chooses {computer_hand}.")
                print("Scissors cut paper, you win!")
            else:
                print(f"\nComputer chooses {computer_hand}.")
                print("You both chose scissors, you tied!")
    play_again = input("\nPlay again? (y/n): ")