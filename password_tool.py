import random
import string

print("====================================")
print("🛡️ AI Password Strength & Generator 🛡️")
print("====================================")

while True:
    print("\n--- Test a New Password ---")
    password = input("Enter a password to test (or type 'quit'): ")
    
    if password.lower() == 'quit':
        print("Exiting Password Tool. Stay safe!")
        break
        
    # 1. Start checking conditions
    has_length = len(password) >= 8
    has_number = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # 2. Score evaluation logic using your IF/ELIF skills
    if has_length and has_number and has_special:
        print("🟢 STRENGTH: Strong! Your password is an absolute fortress.")
        break # Exit the loop because they successfully made a strong password!
        
    else:
        print("🔴 STRENGTH: Weak / Vulnerable!")
        print("Reasons your password failed:")
        if not has_length: 
            print("  ❌ Must be at least 8 characters long.")
        if not has_number: 
            print("  ❌ Missing a number (0-9).")
        if not has_special: 
            print("  ❌ Missing a special character (like !, @, #, $, etc.).")
            
        # 3. Offer to generate one if they are stuck
        choice = input("\nWould you like me to generate an unhackable password for you? (yes/no): ").lower()
        if choice == "yes":
            # Combine letters, numbers, and symbols into one huge pool
            pool = string.ascii_letters + string.digits + string.punctuation
            # Randomly grab 12 items out of the pool and glue them together
            generated_password = "".join(random.choice(pool) for i in range(12))
            
            print(f"\n🔮 GENERATED PASSWORD: {generated_password}")
            print("Copy this down! Exiting program.")
            break