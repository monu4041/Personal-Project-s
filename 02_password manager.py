import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="password_manager"
)

cursor = db.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        id INT AUTO_INCREMENT PRIMARY KEY,
        website VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")
db.commit()

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Insert data into the database
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (%s, %s, %s)",
                   (website, username, password))
    db.commit()

    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Password saved successfully!")

def show_passwords():
    cursor.execute("SELECT website, username, password FROM passwords")
    passwords = cursor.fetchall()

    passwords_window = tk.Toplevel(root)
    passwords_window.title("Saved Passwords")
    

    
    tk.Label(passwords_window, text="Website").grid(row=0, column=0)
    tk.Label(passwords_window, text="Username").grid(row=0, column=1)
    tk.Label(passwords_window, text="Password").grid(row=0, column=2)

    row_num = 1
    for password in passwords:
        tk.Label(passwords_window, text=password[0]).grid(row=row_num, column=1)
        tk.Label(passwords_window, text=password[1]).grid(row=row_num, column=2)
        tk.Label(passwords_window, text=password[2]).grid(row=row_num, column=3)
        row_num += 1

# GUI window...
root = tk.Tk()
root.geometry("800x400")
root.title("Password Manager")
root.iconbitmap('E:\\PNG\key_password_lock_800.ico')
root.resizable(0,0) # maximize button is off....

tk.Label(root,text=' 🔐 passwords Manager 🔐 ',font=("Algerian",40,"bold"),bg='black',fg='Chartreuse').pack(fill='both')
tk.Label(root,text="PASSWORD              MANAGER",fg="Teal",font=('Colonna MT',40)).place(x=50,y=140)                                                                               

tk.Label(root, text="Website:",font=("Constantia",20,"bold")).pack()
website_entry = tk.Entry(root)
website_entry.pack()

tk.Label(root, text="Username:",font=("Constantia",18,"bold")).pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:",font=("Constantia",19,"bold")).pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

save_button = tk.Button(root, text=" Save Password",font=("Constantia",15,"bold") ,command=save_password)
save_button.pack(padx=15,pady=10)

show_button = tk.Button(root, text="Show Passwords",font=("Constantia",15,"bold") , command=show_passwords)
show_button.pack()

root.mainloop()