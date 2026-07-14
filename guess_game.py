import random

print("=========================================")
print("🎲 Smart Hint - Number Guessing Game 🎲")
print("=========================================")
print("I'm thinking of a number between 1 and 50.")
print("You have 5 lives. Let's see if you can beat me!")

# 1. Computer picks a secret number
secret_number = random.randint(1, 50)
lives = 5

# 2. Game Loop
while lives > 0:
    print(f"\n❤️ Lives remaining: {lives}")
    guess_input = input("Enter your guess: ")
    
    # Check if the user typed an actual number
    if not guess_input.isdigit():
        print("❌ That's not a valid number! Try again.")
        continue
        
    guess = int(guess_input)
    
    # 3. Check if guess is correct
    if guess == secret_number:
        print(f"\n🏆 🎉 AMAZING! You guessed it! The number was indeed {secret_number}!")
        break
    else:
        lives -= 1
        print("❌ Wrong guess!")
        
        # If no lives left, break out immediately
        if lives == 0:
            break
            
        # 4. Provide a dynamic mathematical hint instead of just higher/lower
        print("💡 HINT:")
        if secret_number % 2 == 0:
            print(" -> The secret number is EVEN.")
        else:
            print(" -> The secret number is ODD.")
            
        if secret_number % 5 == 0:
            print(" -> The secret number is a multiple of 5.")
            
        if guess > secret_number:
            print(" -> Your guess was too HIGH.")
        else:
            print(" -> Your guess was too LOW.")

# 5. Game Over check
if lives == 0:
    print(f"\n💀 GAME OVER! You ran out of lives. The secret number was {secret_number}.")