import datetime

print("====================================")
print("📔 Personal Digital Diary Creator 📔")
print("====================================")

# 1. Fetch the exact current date and time
current_time = datetime.datetime.now()
formatted_date = current_time.strftime("%Y-%m-%d")  # Format: Year-Month-Day
formatted_time = current_time.strftime("%I:%M %p")  # Format: Hour:Minute AM/PM

print(f"Today's Date: {formatted_date}")
print(f"Current Time: {formatted_time}\n")

# 2. Get your journal entry text from the terminal
entry = input("What did you achieve or learn today, Pawan?\n> ")

# 3. Create a unique filename using today's date
filename = f"Diary_{formatted_date}.txt"

# 4. The Python magic to open a file and write into it
# 'a' stands for "append" which means it adds text without deleting old text
with open(filename, "a", encoding="utf-8") as file:
    file.write("====================================\n")
    file.write(f"Date: {formatted_date} | Time: {formatted_time}\n")
    file.write("====================================\n")
    file.write(f"{entry}\n\n")

print(f"\n🎉 Success! Your entry has been saved automatically to '{filename}'!")