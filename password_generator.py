import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# ---------------- Password Generation Logic ---------------- #
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 8:
            messagebox.showwarning("Invalid Length", "Password length must be at least 8 characters.")
            return

        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digit_var.get()
        use_special = special_var.get()

        if not (use_upper or use_lower or use_digits or use_special):
            messagebox.showwarning("Selection Error", "Select at least one character type.")
            return

        password_chars = []

        if use_upper:
            password_chars.append(random.choice(string.ascii_uppercase))
        if use_lower:
            password_chars.append(random.choice(string.ascii_lowercase))
        if use_digits:
            password_chars.append(random.choice(string.digits))
        if use_special:
            password_chars.append(random.choice(string.punctuation))

        all_chars = ""
        if use_upper:
            all_chars += string.ascii_uppercase
        if use_lower:
            all_chars += string.ascii_lowercase
        if use_digits:
            all_chars += string.digits
        if use_special:
            all_chars += string.punctuation

        while len(password_chars) < length:
            password_chars.append(random.choice(all_chars))

        random.shuffle(password_chars)
        password = "".join(password_chars)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        evaluate_strength(password)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# ---------------- Password Strength Evaluation ---------------- #
def evaluate_strength(password):
    strength = 0
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    if len(password) >= 12:
        strength += 1

    if strength <= 2:
        strength_label.config(text="Strength: Weak", fg="red")
    elif strength == 3:
        strength_label.config(text="Strength: Moderate", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="green")

# ---------------- Copy to Clipboard ---------------- #
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- GUI Setup ---------------- #
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("450x450")
root.resizable(False, False)

tk.Label(root, text="Advanced Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root, justify="center")
length_entry.insert(0, "12")
length_entry.pack(pady=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Numbers", variable=digit_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(anchor="w", padx=40)

tk.Button(root, text="Generate Password", command=generate_password, bg="#D472C3", fg="black").pack(pady=15)

password_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=30)
password_entry.pack(pady=5)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 11, "bold"))
strength_label.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#804F70", fg="black").pack(pady=10)

tk.Label(root, text="© Python Security Tool", font=("Arial", 9)).pack(side="bottom", pady=10)

root.mainloop()
