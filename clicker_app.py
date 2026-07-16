import tkinter as tk

# 1. Create the main window machine
window = tk.Tk()
window.title("Pawan's First Desktop App")
window.geometry("400x300")  # Sets the size of the window (Width x Height)
window.configure(bg="#2c3e50")  # Dark blue/grey background color

# 2. Variable to keep track of the count number
count = 0

# 3. Logic: What happens when buttons are clicked
def increase_count():
    global count
    count += 1
    label_number.config(text=str(count))  # Update the text on screen

def reset_count():
    global count
    count = 0
    label_number.config(text=str(count))  # Reset the text on screen

# 4. Design the User Interface (UI) Elements

# Title Text
label_title = tk.Label(window, text="🚀 CLICKER COUNTER 🚀", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50")
label_title.pack(pady=20)  # pady adds space above and below the text

# The Big Number Display
label_number = tk.Label(window, text="0", font=("Arial", 48, "bold"), fg="#f1c40f", bg="#2c3e50")
label_number.pack(pady=10)

# The Click Button (Green)
button_click = tk.Button(window, text="Click Me!", font=("Arial", 12, "bold"), fg="white", bg="#2ecc71", width=15, command=increase_count)
button_click.pack(pady=10)

# The Reset Button (Red)
button_reset = tk.Button(window, text="Reset", font=("Arial", 10, "bold"), fg="white", bg="#e74c3c", width=10, command=reset_count)
button_reset.pack(pady=5)

# 5. Keep the window open and running until we click 'X'
window.mainloop()