import tkinter as tk
from tkinter import END
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ---------------------------

capital_letters = list(range(65,91))
numbers = list(range(48,58))
def generate_password():
    global password_entry
    password_entry.delete(0, END)
    password_list = [chr(random.choice(capital_letters + numbers)) for _ in range(8)]
    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    with open("Passwords.json", "r") as data_file:
            data = json.load(data_file)
    
    website = website_entry.get()
    for key, value in data.items():
        if key == website:
            password = value["Password:"]
    try:   
        password_entry.insert(0, password) 
    except:
        print("Invalid input!")
        pass
    
        




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    e_mail = email_entry.get()
    password = password_entry.get()
    new_data = {website:{"e-mail" : e_mail,
                        "Password:": password}}
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please fill all the empty spaces!")
    else:     
        is_ok = messagebox.askokcancel(title=website, 
                                   message = f"e-mail: {e_mail}\nPassword: {password}")
    if is_ok == True:
        try:
            with open("Passwords.json", "r") as data_file:
                data = json.load(data_file)
                for key in new_data.keys():
                    if key in data:
                        del data[key]
                data.update(new_data)
                
            
        except FileNotFoundError as err:
            print(f"File {err} not found!")
            with open("Passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)   
        else:
            with open("Passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)    
                
        finally:        
            website_entry.delete(0,END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)    
            pyperclip.copy(password)
          
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
website_entry = tk.Entry(width=38)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = tk.Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "antun.ivic38@gmail.com")
password_entry = tk.Entry(width = 38)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = tk.Button(text = "Generate", command=generate_password, width=7)
generate_password_button.grid(row=3, column=2)
add_button = tk.Button(text = "Add", command=save, width=40)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tk.Button(text = "Search", width=7, command=search_password)
search_button.grid(row=1, column=2)
window.mainloop()  



    