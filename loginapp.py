# Creator: Israel Showell
# Start Date: 3/29/2024
# End Date: 3/29/2024
# Project: Login Application
# Version: 1.00


# Description:
"""
This is a basic GUI login software that uses sqlite as its database system.
This project is a way for me to practice GUI development and database management.
"""

#Imports the libaries to the Python Script
import tkinter
import sqlite3
from tkinter import messagebox

#Connects to the database and gives it default values
db=sqlite3.connect('login.sqlite')

def startup():
    #This tells the database to make a table if necessary 
    db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')

    #This checks the database and makes sure we don't add in extra admin rows
    Admin_cursor = db.cursor()
    Admin_cursor.execute("SELECT * FROM login WHERE username='admin' AND password='admin'")
    if Admin_cursor.fetchone() is None:
        db.execute("INSERT INTO login(username, password) VALUES('admin','admin')")
        #Commit makes the data actually go into the database
        db.commit()

    
#Controls the login function
def login():
     
     cursor=db.cursor()
     #The ? mean that the user_input and the pass_input variables will be added there
     cursor.execute("SELECT * FROM login where username=? AND password=?",(user_input.get(),pass_input.get()))

     #This checks each row to see if the username and password entered by the
     #user exists.
     row=cursor.fetchone()
     
     if row:
         messagebox.showinfo('Info', 'Login Successful')
     else:
         messagebox.showinfo('Info', 'Login Failed')


#Main code area
startup()
main_window=tkinter.Tk()
main_window.title('Login Form')

#This controls the height and width, but it uses 'x' instead of '*'
#for multiplication 
main_window.geometry('400x300')

#Adds padding to x coord of the screen, thus pushing everything to the right
xpadding=20
main_window['padx']=xpadding

#This allows the inputs to be saved as Strings to be put into the database
user_input=tkinter.StringVar()
pass_input=tkinter.StringVar()


#Creates a message that says "Login Application"
info_label=tkinter.Label(main_window, text='Login Application')
info_label.grid(row=0,column=0,pady=5)

#Creates the username label and adds it to the main window
info_user=tkinter.Label(main_window, text='Username')
info_user.grid(row=1,column=0,pady=20)

#Creates the username Entry spot and adds it to the main window
userinput=tkinter.Entry(main_window, textvariable=user_input)
userinput.grid(row=1,column=1,pady=10)

#Creates the password label and adds it to the main window
info_pass=tkinter.Label(main_window, text='Password')
info_pass.grid(row=2,column=0)

#Creates the password Entry spot and adds it to the main window
passinput=tkinter.Entry(main_window, textvariable=pass_input)
passinput.grid(row=2,column=1,pady=10)

#Creates the login button and adds it to the main window
login_btn=tkinter.Button(text='Login',command=login)
login_btn.grid(row=3,column=1,pady=10)

#Brings the main window up on screen
main_window.mainloop()



