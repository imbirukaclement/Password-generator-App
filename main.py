from tkinter import*
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json



def generate_password():
    letters=['a',"b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&',' ,','*','+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(numbers) for _ in range(randint(2,4))]
    password_numbers = [choice(symbols) for _ in range(randint(2,4))]
    password_list =password_numbers + password_symbols + password_letters
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="opps",message="Please make sure you havent left any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # json.dump(new_data, data_file,indent=4)
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:

            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists")
window = Tk()
window.title("Password")
window.minsize(height=300, width=300)
window.config(padx=2, pady=20)


canvas=Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label=Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="Email address:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry = Entry(width=21)
website_entry.grid(column=1,row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"clemo@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

password_generator = Button(text="Generate_password",command=generate_password)
password_generator.grid(column=2, row=3)
add_button = Button(text="add", width=36, command=save)
add_button.grid(row=5, column=1, columnspan=2)
search_button = Button(text="search", width=13, command=find_password)
search_button.grid(column=2, row=1)








window.mainloop()