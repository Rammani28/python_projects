from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_LABEL = ('Arial', 16, 'normal')
FONT_ENTRY = ('Arial', 16, 'normal')
FONT_BUTTON = ('Arial', 12, 'normal')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += ([choice(symbols) for _ in range(randint(2, 4))])
    password_list += ([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'username': username,
            'password': password,
        }
    }

    if len(website.strip()) == 0 or len(username.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Confirm",
                                       message=f"These are the details entered: \nWebsite: {website} \n"
                                               f"Username/email: {username} \npassword: {password}")
        if is_ok:
            try:
                with open('data.json', mode='r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', mode='w') as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


def find_password():
    website = website_entry.get().lower()
    try:
        with open('data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Username: {data[website]['username']} \n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showerror(title='Erro', message=f"No details exist for the provided website.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title(string="Password Manager")

canvas = Canvas()
canvas.config(width=200, height=200)

logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT_LABEL)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=FONT_LABEL)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=FONT_LABEL)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21, font=FONT_ENTRY)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()
username_entry = Entry(width=35, font=FONT_ENTRY)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "rammani@gmail.com")
password_entry = Entry(width=21, font=FONT_ENTRY)
password_entry.grid(column=1, row=3)

# Button
generate_password_button = Button(text="Generate Password", font=FONT_BUTTON, bg='white', command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, font=FONT_BUTTON, bg='white', command=save_data)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", font=FONT_BUTTON, command=find_password, bg='white', width=15)
search_button.grid(column=2, row=1)

window.mainloop()
