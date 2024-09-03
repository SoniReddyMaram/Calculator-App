import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for password length.")
        return
    
    if length <= 0:
        messagebox.showerror("Invalid input", "Password length must be greater than 0.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Set up the GUI window
root = tk.Tk()
root.title("Password Generator")

# Label for password length
length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=10)

# Entry field for password length
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Entry field to display the generated password
password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)

# Run the GUI loop
root.mainloop()
