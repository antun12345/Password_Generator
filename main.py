import tkinter as tk
from tkinter import END
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ---------------------------

capital_letters = list(range(65,91))
numbers = list(range(48,58))
def generate_password():
    global password_entry
    password_entry.delete(0, END)
    password = ""
    for x in range(8):
        random_char = random.choice(capital_letters + numbers)
        password += chr(random_char)
    password_entry.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    e_mail = email_entry.get()
    password = password_entry.get()
    
    with open("Passwords.txt", "a") as data_file:
        data_file.write(f"| {website} | {e_mail} | {password}\n")
        website_entry.delete(0,END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)    
        
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Generator")
window.config(padx=30, pady = 20)

canvas = tk.Canvas(height=200, width = 200)
logo = tk.PhotoImage(file = "Logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(row=0, column=1)

website_label = tk.Label(text = "Website:" )
website_label.grid(row = 1, column= 0)
email_label = tk.Label(text = "E-mail:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text = "Password:")
password_label.grid(row=3, column = 0)

#Entries
website_entry = tk.Entry(width=43)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "antun.ivic38@gmail.com")
password_entry = tk.Entry(width = 33)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = tk.Button(text = "Generate", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tk.Button(text = "Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()  



    