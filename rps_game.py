import random

print("=== Upgraded Rock, Paper, Scissors (Best of 3) ===")

choices = ["rock", "paper", "scissors"]

# 1. Variables to hold the scores (No quotes, because they are numbers!)
player_score = 0
computer_score = 0

# 2. The Loop keeps running until someone hits 3 points
while player_score < 3 and computer_score < 3:
    print(f"\n--- SCOREBOARD | You: {player_score} | Computer: {computer_score} ---")
    
    player_choice = input("Enter rock, paper, or scissors (or 'quit'): ").lower()
    
    if player_choice == "quit":
        print("Quitting game...")
        break
        
    if player_choice not in choices:
        print("❌ Invalid choice. Try again!")
        continue
        
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # 3. Game Logic & Score Updating
    if player_choice == computer_choice:
        print("It's a tie for this round!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win this round! 🎉")
        player_score += 1  # Adds 1 point to your score
    else:
        print("Computer wins this round! 🤖")
        computer_score += 1  # Adds 1 point to computer's score

# 4. Out of the loop! Check who won the tournament
print("\n===============================")
if player_score == 3:
    print("🏆 CONGRATULATIONS! You are the WINNER! 🏆")
elif computer_score == 3:
    print("🤖 GAME OVER! The machine won the Tournament. Better luck next time!")
print("===============================")