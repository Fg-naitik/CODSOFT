import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        chars = ""

        if letters_var.get():
            chars += string.ascii_letters

        if numbers_var.get():
            chars += string.digits

        if symbols_var.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning(
                "Warning",
                "Select at least one character type!"
            )
            return

        password = ''.join(
            random.choice(chars)
            for _ in range(length)
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        if length < 8:
            strength_label.config(text="Weak Password")
        elif length < 12:
            strength_label.config(text="Medium Password")
        else:
            strength_label.config(text="Strong Password")

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid password length!"
        )

def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x450")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

# Length Input
tk.Label(
    root,
    text="Password Length:",
    font=("Arial", 12)
).pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 12)
)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Checkboxes
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Include Letters",
    variable=letters_var,
    font=("Arial", 11)
).pack()

tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=numbers_var,
    font=("Arial", 11)
).pack()

tk.Checkbutton(
    root,
    text="Include Symbols",
    variable=symbols_var,
    font=("Arial", 11)
).pack()

# Generate Button
tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12)
).pack(pady=15)

# Password Output
password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 14),
    justify="center"
)
password_entry.pack(pady=10)

# Copy Button
tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 12)
).pack(pady=5)

# Strength Label
strength_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold")
)
strength_label.pack(pady=10)

root.mainloop()