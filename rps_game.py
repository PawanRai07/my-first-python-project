import random

print("=== Rock, Paper, Scissors Game ===")

# A List of available choices (ordered slots)
choices = ["rock", "paper", "scissors"]

while True:
    # 1. Get player input
    player_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if player_choice == "quit":
        print("Thanks for playing! Goodbye.")
        break
        
    if player_choice not in choices:
        print("Invalid choice. Try again!")
        continue
        
    # 2. Let the computer choose randomly from our list
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # 3. Game Logic (Comparing choices)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You are a winner, pawan! 🎉")
    else:
        print("The machine is winning! 🤖")