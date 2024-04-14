import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 4:  # Ensure minimum length for complexity
        messagebox.showinfo("Info", "Length should be at least 4 characters.")
        return ""

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    if length > 4:
        all_characters = uppercase_letters + lowercase_letters + digits + symbols
        password += [random.choice(all_characters) for _ in range(length - 4)]

    random.shuffle(password)
    return ''.join(password)

def on_generate_clicked():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_entry.config(state='normal')
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state='readonly')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the password length.")

app = tk.Tk()
app.title("Password Generator")

# Frame for Entry
frame = tk.Frame(app)
frame.pack(pady=20)

# Entry for password length
tk.Label(frame, text="Enter Password Length:").pack(side=tk.LEFT)
length_entry = tk.Entry(frame, width=10)
length_entry.pack(side=tk.LEFT, padx=10)

# Button to generate password
generate_button = tk.Button(frame, text="Generate Password", command=on_generate_clicked)
generate_button.pack(side=tk.LEFT)

# Entry to display generated password
password_entry = tk.Entry(app, text="", width=40, readonlybackground='white', state='readonly')
password_entry.pack(pady=20)

# Run the application
app.mainloop()
