from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A5,portrait,A4,landscape
from reportlab.lib.units import inch
from datetime import datetime

loginwindow = Tk()
loginwindow.title("Tailor Shop Management System in Python")
loginwindow.geometry("1366x768")
loginwindow.configure(bg="#f8d7ac")
loginwindow.rowconfigure(0, weight=1)
loginwindow.columnconfigure(0, weight=1)
loginwindow.state('zoomed')

#-----All Windows frame Declaration
login_page = Frame(loginwindow)
home_page = Frame(loginwindow)
register_page = Frame(loginwindow)
update_page = Frame(loginwindow)
measurement_page = Frame(loginwindow)
search_page = Frame(loginwindow)
payment_page = Frame(loginwindow)

for frame in (login_page, home_page, register_page, update_page, measurement_page, search_page, payment_page):
    frame.grid(row=0,column=0,sticky='nsew')

def show_frame(frame):
    frame.tkraise()

#---To Display the first Window
show_frame(login_page)

# ######################################################################################################
# #############################------LOGIN-PAGE-------###################################################

# -----------Image declaration of home-page-------------
lp_background_img = PhotoImage(file=f"lp_background.png")
lp_entry0_img = PhotoImage(file=f"lp_img_textBox0.png")
lp_entry1_img = PhotoImage(file=f"lp_img_textBox1.png")
lp_img0 = PhotoImage(file=f"lp_img0.png")


# -----------BG of login-page-------------
lp_label_of_bg=Label(login_page,image=lp_background_img)
lp_label_of_bg.place(x=0,y=0)

# -----------entry box bg of login-page-------------

lp_entry0_bg = Label(login_page,image=lp_entry0_img)
lp_entry0_bg.place( x=232.0, y=440.0)
# -----
lp_entry1_bg = Label(login_page,image=lp_entry1_img)
lp_entry1_bg.place( x=232.0, y=353.0)

# =========usename textbox code====

lp_username_textbox = Entry(login_page,
    bd=0, font=("arial", 15),
    bg="#ffffff",
    highlightthickness=0)

lp_username_textbox.place(
    x=237.0, y=355,
    width=321.0,
    height=38)
# =====password textbox code======
lp_password_textbox = Entry(login_page,
    bd=0, font=("arial", 15),
    bg="#ffffff", show="*",
    highlightthickness=0)

lp_password_textbox.place(
    x=237.0, y=442,
    width=321.0,
    height=38)


#####-----------User Credensial Validation Function-----##
def login():
    username = lp_username_textbox.get()
    password = lp_password_textbox.get()
    conn = sqlite3.connect("tailor_shop.db")

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    # Create a "users" table

    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("INSERT INTO users (username, password) VALUES ('san', '123')")
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    row = c.fetchone()
    if row:
        show_frame(home_page)
    else:
        tkinter.messagebox.showerror('Login Error', 'Invalid username or password.')
    conn.commit()
    conn.close()
    lp_username_textbox.delete(0,END)
    lp_password_textbox.delete(0,END)
#########################################################
# ==========login button code====

login_btn = Button(login_page,
    image=lp_img0,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat")

login_btn.place(
    x=227, y=541,
    width=331,
    height=40)
# -------------------

# ######################################################################################################
# #############################------HOME-PAGE-------####################################################

home_page.config()
hp_background_img = PhotoImage(file = f"hp_background.png")
hp_label=Label(home_page,image=hp_background_img)
hp_label.place(x=0, y=0)

# -----------Image declaration of home-page-------------

hp_img0 = PhotoImage(file = f"hp_img0.png")
hp_img1 = PhotoImage(file = f"hp_img1.png")
hp_img2 = PhotoImage(file = f"hp_img2.png")
hp_img3 = PhotoImage(file = f"hp_img3.png")
hp_img4 = PhotoImage(file = f"hp_img4.png")
#-----------------


#======buttons code========
new_cust_btn = Button(home_page,
    image = hp_img3,
    borderwidth = 0,
    highlightthickness = 0, command=lambda :show_frame(register_page),
    relief = "flat")

new_cust_btn.place(
    x = 144, y = 255,
    width = 316,
    height = 113)
#-------------
update_cust_btn = Button(home_page,
    image = hp_img2,
    borderwidth = 0,
    highlightthickness = 0, command = lambda: show_frame(update_page),
    relief = "flat")

update_cust_btn.place(
    x = 525, y = 255,
    width = 316,
    height = 113)
#-------------
search_cust_btn = Button(home_page,
    image = hp_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :show_frame(search_page),
    relief = "flat")

search_cust_btn.place(
    x = 144, y = 480,
    width = 316,
    height = 113)
#-------------
payment_details_btn = Button(home_page,
    image = hp_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :show_frame(payment_page),
    relief = "flat")

payment_details_btn.place(
    x = 525, y = 480,
    width = 316,
    height = 113)
#-----------
logout_btn = Button(home_page,
    image = hp_img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :show_frame(login_page),
    relief = "flat")

logout_btn.place(
    x = 1151, y = 43,
    width = 175,
    height = 61)
# -------------
# ######################################################################################################
# #############################------REGISTER-PAGE-------####################################################

# -----------Image declaration of register-page-------------
reg_cus_p_background_img = PhotoImage(file = f"reg_cus_p_background.png")
reg_cus_p_img0 = PhotoImage(file = f"reg_cus_p_img0.png")
reg_cus_p_entry0_img = PhotoImage(file = f"reg_cus_p_img_textBox0.png")
reg_cus_p_entry1_img = PhotoImage(file = f"reg_cus_p_img_textBox1.png")
reg_cus_p_entry2_img = PhotoImage(file = f"reg_cus_p_img_textBox2.png")
reg_cus_p_entry3_img = PhotoImage(file = f"reg_cus_p_img_textBox3.png")
reg_cus_p_entry4_img = PhotoImage(file = f"reg_cus_p_img_textBox4.png")
reg_cus_p_img1 = PhotoImage(file = f"reg_cus_p_img1.png")
reg_cus_p_img2 = PhotoImage(file = f"reg_cus_p_img2.png")

# -----------BG of register-page-------------
reg_cus_p_label_of_bg = Label(register_page,image=reg_cus_p_background_img)
reg_cus_p_label_of_bg.place(x=0,y=0)

# -----------entry box bg of register-page-------------

reg_cus_p_entry0_bg = Label(register_page,image=reg_cus_p_entry0_img)
reg_cus_p_entry0_bg.place( x = 330.0, y = 483)
# -----
reg_cus_p_entry1_bg = Label(register_page,image=reg_cus_p_entry1_img)
reg_cus_p_entry1_bg.place( x = 330.0, y = 413)
# -----
reg_cus_p_entry2_bg = Label(register_page,image=reg_cus_p_entry2_img)
reg_cus_p_entry2_bg.place( x = 330.0, y = 343)
# -----
reg_cus_p_entry3_bg = Label(register_page,image=reg_cus_p_entry3_img)
reg_cus_p_entry3_bg.place(x = 330.0, y = 273)
# -----
reg_cus_p_entry4_bg = Label(register_page,image=reg_cus_p_entry4_img)
reg_cus_p_entry4_bg.place(x = 330.0, y = 203)

# -----------entry boxes code of register-page-------------
#customer id entry
reg_cus_p_entry4 = Entry(register_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

reg_cus_p_entry4.place(
    x = 335.0, y = 205,
    width = 321.0,
    height = 38)

#---------
#customer name entry
reg_cus_p_entry3 = Entry(register_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

reg_cus_p_entry3.place(
    x = 335.0, y = 275,
    width = 321.0,
    height = 38)
#---
#---------
#customer mobile number
reg_cus_p_entry2 = Entry(register_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

reg_cus_p_entry2.place(
    x = 335.0, y = 345,
    width = 321.0,
    height = 38)

###-----------
#Customer Email
reg_cus_p_entry1 = Entry(register_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

reg_cus_p_entry1.place(
    x = 335.0, y = 415,
    width = 321.0,
    height = 38)
#------
#customer Address
reg_cus_p_entry0 = Entry(register_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

reg_cus_p_entry0.place(
    x = 335.0, y = 485,
    width = 321.0,
    height = 85)
############### DATA base Queries#####
def register_customer():
    # TO Fetch the entered data from entry boxes
    id = reg_cus_p_entry4.get()
    name = reg_cus_p_entry3.get()
    phone = reg_cus_p_entry2.get()
    email = reg_cus_p_entry1.get()
    address = reg_cus_p_entry0.get()

    # Validate the input
    if not id.isdigit():
        tkinter.messagebox.showerror("Error", "ID must be a number")
        return
    if not name.replace(" ", "").isalpha():
        tkinter.messagebox.showerror("Error", "Name must contain only letters and spaces")
        return
    if not phone.isdigit() or len(phone) != 10:
        tkinter.messagebox.showerror("Error", "Phone number must be a 10-digit number")
        return
    if email and not ("@" in email and "." in email):
        tkinter.messagebox.showerror("Error", "Invalid email address")
        return

    # Connect to the database
    conn = sqlite3.connect('tailor_shop.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS customers
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  phone TEXT,
                  email TEXT,
                  address TEXT)''')
    # Check if the ID already exists in the customers table
    c.execute("SELECT id FROM customers WHERE id=?", (id,))
    row = c.fetchone()
    if row is not None:
        tkinter.messagebox.showerror("Error", f"ID {id} is already assigned to another customer")
        conn.close()
        return

    # Insert the data into the customers table
    c.execute("INSERT INTO customers (id, name, phone, email, address) VALUES (?, ?, ?, ?, ?)",
              (id, name, phone, email, address))

    # Commit the changes and close the connection
    conn.commit()
    tkinter.messagebox.showinfo("Success", "Customer registered successfully")
    conn.close()

    # Clear the entry fields
    reg_cus_p_entry4.delete(0, 'end')
    reg_cus_p_entry3.delete(0, 'end')
    reg_cus_p_entry2.delete(0, 'end')
    reg_cus_p_entry1.delete(0, 'end')
    reg_cus_p_entry0.delete(0, 'end')
#---------------------------------------

####
def reg_p_clear_measurements():
    reg_cus_p_entry4.delete(0, 'end')
    reg_cus_p_entry3.delete(0, 'end')
    reg_cus_p_entry2.delete(0, 'end')
    reg_cus_p_entry1.delete(0, 'end')
    reg_cus_p_entry0.delete(0, 'end')

def reg_p_clear_and_back():
    # Call the clear page function
    reg_p_clear_measurements()

    # Call the second function using lambda function
    reg_pg_back_btn.after(0, lambda: show_frame(home_page))

#======buttons code========

register_btn = Button(register_page,
    image = reg_cus_p_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = register_customer,
    relief = "flat")

register_btn.place(
    x = 403, y = 605,
    width = 175,
    height = 61)

reg_cus_p_measurement_btn = Button(register_page,
    image = reg_cus_p_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :show_frame(measurement_page),
    relief = "flat")

reg_cus_p_measurement_btn.place(
    x = 600, y = 605,
    width = 175,
    height = 61)

reg_pg_back_btn = Button(register_page,
    image = reg_cus_p_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = reg_p_clear_and_back,
    # command = lambda :show_frame(home_page),
    relief = "flat")

reg_pg_back_btn.place(
    x = 1151, y = 43,
    width = 175,
    height = 61)



# ######################################################################################################
# #############################------UPDATE CUSTOMER DETAILS-PAGE-------####################################################


# -----------Image declaration of update-page-------------
up_cus_p_background_img = PhotoImage(file = f"up_cus_p_background.png")
up_cus_p_img0 = PhotoImage(file = f"up_cus_p_img0.png")
up_cus_p_entry0_img = PhotoImage(file = f"up_cus_p_img_textBox0.png")
up_cus_p_entry1_img = PhotoImage(file = f"up_cus_p_img_textBox1.png")
up_cus_p_entry2_img = PhotoImage(file = f"up_cus_p_img_textBox2.png")
up_cus_p_entry3_img = PhotoImage(file = f"up_cus_p_img_textBox3.png")
up_cus_p_entry4_img = PhotoImage(file = f"up_cus_p_img_textBox4.png")
up_cus_p_img1 = PhotoImage(file = f"up_cus_p_img1.png")
up_cus_p_img2 = PhotoImage(file = f"up_cus_p_img2.png")
up_cus_p_img4 = PhotoImage(file = f"up_cus_p_img4.png")
# -----------BG of update-page-------------
up_cus_p_label_of_bg = Label(update_page,image=up_cus_p_background_img)
up_cus_p_label_of_bg.place(x=0,y=0)

# -----------entry box bg of update-page-------------

up_cus_p_entry0_bg = Label(update_page,image=up_cus_p_entry0_img)
up_cus_p_entry0_bg.place( x = 330.0, y = 483)
# -----
up_cus_p_entry1_bg = Label(update_page,image=up_cus_p_entry1_img)
up_cus_p_entry1_bg.place( x = 330.0, y = 413)
# -----
up_cus_p_entry2_bg = Label(update_page,image=up_cus_p_entry2_img)
up_cus_p_entry2_bg.place( x = 330.0, y = 343)
# -----
up_cus_p_entry3_bg = Label(update_page,image=up_cus_p_entry3_img)
up_cus_p_entry3_bg.place(x = 330.0, y = 273)
# -----
up_cus_p_entry4_bg = Label(update_page,image=up_cus_p_entry4_img)
up_cus_p_entry4_bg.place(x = 330.0, y = 203)

# -----------entry boxes code of update-page-------------

up_cus_p_entry4 = Entry(update_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

up_cus_p_entry4.place(
    x = 335.0, y = 205,
    width = 321.0,
    height = 38)
#-------
up_cus_p_entry3 = Entry(update_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

up_cus_p_entry3.place(
    x = 335.0, y = 275,
    width = 321.0,
    height = 38)

##-----------

up_cus_p_entry2 = Entry(update_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

up_cus_p_entry2.place(
    x = 335.0, y = 345,
    width = 321.0,
    height = 38)

###-----------
up_cus_p_entry1 = Entry(update_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

up_cus_p_entry1.place(
    x = 335.0, y = 415,
    width = 321.0,
    height = 38)

#---------

up_cus_p_entry0 = Entry(update_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

up_cus_p_entry0.place(
    x = 335.0, y = 485,
    width = 321.0,
    height = 85)
####################  DATA BASE Quieries #########

def update_customer():
    # Fetch the entered data from entry boxes
    id = up_cus_p_entry4.get()
    name = up_cus_p_entry3.get()
    phone = up_cus_p_entry2.get()
    email = up_cus_p_entry1.get()
    address = up_cus_p_entry0.get()

    # Validate the input
    if not id.isdigit():
        tkinter.messagebox.showerror("Error", "ID must be a number")
        return
    if not name.replace(" ", "").isalpha():
        tkinter.messagebox.showerror("Error", "Name must contain only letters")
        return
    if not phone.isdigit() or len(phone) != 10:
        tkinter.messagebox.showerror("Error", "Phone number must be a 10-digit number")
        return
    if email and not ("@" in email and "." in email):
        tkinter.messagebox.showerror("Error", "Invalid email address")
        return


    # Connect to the database and update the data
    conn = sqlite3.connect('tailor_shop.db')
    c = conn.cursor()
    c.execute("UPDATE customers SET name=?, phone=?, email=?, address=? WHERE id=?",
              (name, phone, email, address, id))
    conn.commit()
    tkinter.messagebox.showinfo("Success", "Customer details updated successfully")
    conn.close()

def search_customer():
    # Fetch the entered data from entry boxes
    id = up_cus_p_entry4.get()

    # Connect to the database and search for the customer
    conn = sqlite3.connect('tailor_shop.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE id=?", (id,))
    customer = c.fetchone()

    # Display the customer details in the entry boxes
    if customer:
        up_cus_p_entry3.delete(0, 'end')
        up_cus_p_entry2.delete(0, 'end')
        up_cus_p_entry1.delete(0, 'end')
        up_cus_p_entry0.delete(0, 'end')
        up_cus_p_entry3.insert(0, customer[1])
        up_cus_p_entry2.insert(0, customer[2])
        up_cus_p_entry1.insert(0, customer[3])
        up_cus_p_entry0.insert(0, customer[4])
    else:
        tkinter.messagebox.showerror("Error", "Customer not found")

    conn.close()


def up_clear_measurements():
    up_cus_p_entry3.delete(0, 'end')
    up_cus_p_entry2.delete(0, 'end')
    up_cus_p_entry1.delete(0, 'end')
    up_cus_p_entry0.delete(0, 'end')


def up_clear_and_back():
    # Call the clear page function
    up_clear_measurements()

    # Call the second function using lambda function
    update_customer_pg_btn.after(0, lambda :show_frame(home_page) )


#======buttons code========

#search button--------
cus_up_p_search_with_cusID_btn = Button(update_page,
    image = up_cus_p_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = search_customer,
    relief = "flat")

cus_up_p_search_with_cusID_btn.place(
    x = 670, y = 205,
    width = 132,
    height = 41)

update_customer_pg_btn = Button(update_page,
    image = up_cus_p_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command=update_customer,
    # command = lambda :show_frame(measurement_page),
    relief = "flat")


update_customer_pg_btn.place(
    x = 403, y = 605,
    width = 175,
    height = 61)

up_cus_p_measurement_btn = Button(update_page,
    image = up_cus_p_img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :show_frame(measurement_page),
    relief = "flat")

up_cus_p_measurement_btn.place(
    x = 600, y = 605,
    width = 175,
    height = 61)

update_pg_back_btn = Button(update_page,
    image = up_cus_p_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = up_clear_and_back,
    relief = "flat")

update_pg_back_btn.place(
    x = 1151, y = 43,
    width = 175,
    height = 61)

# ######################################################################################################
# #############################------MEASUREMENT-PAGE-------####################################################

mp_background_img = PhotoImage(file = f"mp_background.png")
mp_label=Label(measurement_page,image=mp_background_img)
mp_label.place(x=0, y=0)

# -----------Image declaration of measurement-page-------------
mp_background_img = PhotoImage(file = f"mp_background.png")
mp_img0 = PhotoImage(file = f"mp_img0.png")
mp_entry0_img = PhotoImage(file = f"mp_img_textBox0.png")
mp_entry1_img = PhotoImage(file = f"mp_img_textBox1.png")
mp_entry2_img = PhotoImage(file = f"mp_img_textBox2.png")
mp_entry3_img = PhotoImage(file = f"mp_img_textBox3.png")
mp_entry4_img = PhotoImage(file = f"mp_img_textBox4.png")
mp_entry5_img = PhotoImage(file = f"mp_img_textBox5.png")
mp_entry6_img = PhotoImage(file = f"mp_img_textBox6.png")
mp_entry7_img = PhotoImage(file = f"mp_img_textBox7.png")
mp_entry8_img = PhotoImage(file = f"mp_img_textBox8.png")
mp_entry9_img = PhotoImage(file = f"mp_img_textBox9.png")
mp_entry10_img = PhotoImage(file = f"mp_img_textBox10.png")
mp_entry11_img = PhotoImage(file = f"mp_img_textBox11.png")
mp_entry12_img = PhotoImage(file = f"mp_img_textBox12.png")
mp_entry13_img = PhotoImage(file = f"mp_img_textBox13.png")
mp_entry14_img = PhotoImage(file = f"mp_img_textBox14.png")
mp_entry15_img = PhotoImage(file = f"mp_img_textBox15.png")
mp_entry16_img = PhotoImage(file = f"mp_img_textBox16.png")
mp_entry17_img = PhotoImage(file = f"mp_img_textBox17.png")
mp_entry18_img = PhotoImage(file = f"mp_img_textBox18.png")
mp_entry19_img = PhotoImage(file = f"mp_img_textBox19.png")
mp_entry20_img = PhotoImage(file = f"mp_img_textBox20.png")
mp_img1 = PhotoImage(file = f"mp_img1.png")
mp_img2 = PhotoImage(file = f"mp_img2.png")

# -----------BG of measurement-page-------------
mp_label_of_bg = Label(measurement_page,image=mp_background_img)
mp_label_of_bg.place(x=0,y=0)


# -----------entry box bg of measurement-page-------------

mp_entry0_bg = Label(measurement_page,image=mp_entry0_img)
mp_entry0_bg.place( x = 319.0, y = 281)
# -----
mp_entry1_bg = Label(measurement_page,image=mp_entry1_img)
mp_entry1_bg.place( x = 705.0, y = 281)
# -----
mp_entry2_bg = Label(measurement_page,image=mp_entry2_img)
mp_entry2_bg.place( x = 1107.0, y = 281)
# -----
mp_entry3_bg = Label(measurement_page,image=mp_entry3_img)
mp_entry3_bg.place(x = 319.0, y = 341)
# -----
mp_entry4_bg = Label(measurement_page,image=mp_entry4_img)
mp_entry4_bg.place(x = 705.0, y = 341)
#-----
mp_entry5_bg = Label(measurement_page,image=mp_entry5_img)
mp_entry5_bg.place( x = 1107.0, y = 341)
# -----
mp_entry6_bg = Label(measurement_page,image=mp_entry6_img)
mp_entry6_bg.place( x = 319.0, y = 401)
# -----
mp_entry7_bg = Label(measurement_page,image=mp_entry7_img)
mp_entry7_bg.place( x = 705.0, y = 401)
# -----
mp_entry8_bg = Label(measurement_page,image=mp_entry8_img)
mp_entry8_bg.place(x = 1107.0, y = 401)
# -----
mp_entry9_bg = Label(measurement_page,image=mp_entry9_img)
mp_entry9_bg.place(x = 319.0, y = 461)
#-----
mp_entry10_bg = Label(measurement_page,image=mp_entry10_img)
mp_entry10_bg.place( x = 705.0, y = 461)
# -----
mp_entry11_bg = Label(measurement_page,image=mp_entry11_img)
mp_entry11_bg.place( x = 1107.0, y = 461)
# -----
mp_entry12_bg = Label(measurement_page,image=mp_entry12_img)
mp_entry12_bg.place( x = 319.0, y = 521)
# -----
mp_entry13_bg = Label(measurement_page,image=mp_entry13_img)
mp_entry13_bg.place(x = 705.0, y = 521)
# -----
mp_entry14_bg = Label(measurement_page,image=mp_entry14_img)
mp_entry14_bg.place(x = 1107.0, y = 521)
#-----
mp_entry15_bg = Label(measurement_page,image=mp_entry15_img)
mp_entry15_bg.place( x = 319.0, y = 581)
# -----
mp_entry16_bg = Label(measurement_page,image=mp_entry16_img)
mp_entry16_bg.place( x = 705.0, y = 581)
# -----
mp_entry17_bg = Label(measurement_page,image=mp_entry17_img)
mp_entry17_bg.place( x = 1107.0, y = 581)
# -----
mp_entry18_bg = Label(measurement_page,image=mp_entry18_img)
mp_entry18_bg.place(x = 572.0, y = 177)
# -----
mp_entry19_bg = Label(measurement_page,image=mp_entry19_img)
mp_entry19_bg.place(x = 246.0, y = 175)
# -----
mp_entry20_bg = Label(measurement_page,image=mp_entry20_img)
mp_entry20_bg.place(x = 900.0, y = 641)

##---------Entry Box Code of Measurement-Page

mp_entry19 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry19.place(
    x = 251.0, y = 180,
    width = 96.0,
    height = 39)

mp_entry18 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry18.place(
    x = 577.0, y = 179,
    width = 434.0,
    height = 39)

###########----------Product Category Drop Down Menu Code---

measurement_pro_category_ddl=ttk.Combobox(measurement_page, values=["Shirt","Pant"],font=("arial",15))
measurement_pro_category_ddl.place(x=1135,y=180,
                                   width=150,
                                   height=38)

#############-----------------

mp_entry0 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry0.place(
    x = 324.0, y = 283,
    width = 113.0,
    height = 39)
#----
mp_entry1 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry1.place(
    x = 710.0, y = 283,
    width = 113.0,
    height = 39)
#------
mp_entry2 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry2.place(
    x = 1112.0, y = 283,
    width = 113.0,
    height = 39)
#----
mp_entry3 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry3.place(
    x = 324.0, y = 343,
    width = 113.0,
    height = 39)
#-----
mp_entry4 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry4.place(
    x = 710.0, y = 343,
    width = 113.0,
    height = 39)
#-----
mp_entry5 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry5.place(
    x = 1112.0, y = 343,
    width = 113.0,
    height = 39)
#-----
mp_entry6 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry6.place(
    x = 324.0, y = 403,
    width = 113.0,
    height = 39)
#----
mp_entry7 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry7.place(
    x = 710.0, y = 403,
    width = 113.0,
    height = 39)
#----
mp_entry8 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry8.place(
    x = 1112.0, y = 403,
    width = 113.0,
    height = 39)
#----
mp_entry9 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry9.place(
    x = 324.0, y = 463,
    width = 113.0,
    height = 39)
#-----
mp_entry10 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry10.place(
    x = 710.0, y = 463,
    width = 113.0,
    height = 39)
#----
mp_entry11 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry11.place(
    x = 1112.0, y = 463,
    width = 113.0,
    height = 39)
#-----
mp_entry12 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry12.place(
    x = 324.0, y = 523,
    width = 113.0,
    height = 39)
#-----
mp_entry13 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry13.place(
    x = 710.0, y = 523,
    width = 113.0,
    height = 39)
#----
mp_entry14 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry14.place(
    x = 1112.0, y = 523,
    width = 113.0,
    height = 39)
#------
mp_entry15 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry15.place(
    x = 324.0, y = 583,
    width = 113.0,
    height = 39)
#-----
mp_entry16 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry16.place(
    x = 710.0, y = 583,
    width = 113.0,
    height = 39)
#-----
mp_entry17 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry17.place(
    x = 1112.0, y = 583,
    width = 113.0,
    height = 39)
#-----
mp_entry20 = Entry(measurement_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

mp_entry20.place(
    x = 905.0, y = 643,
    width = 149.0,
    height = 39)

#########-----DATA BASE QUERIRES AND UPDATE FUNCTION------------##########

conn = sqlite3.connect('tailor_shop.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS measurements
                 (id INTEGER PRIMARY KEY,
                  customer_id INTEGER,
                  category TEXT,
                  shirt_length FLOAT,
                  sleeve_width FLOAT,
                  pant_length FLOAT,
                  collor_length FLOAT,
                  chest_width1 FLOAT,
                  waist FLOAT,
                  collor_width FLOAT,
                  chest_width2 FLOAT,
                  thigh_width FLOAT,
                  cuff_length FLOAT,
                  chest_width3 FLOAT,
                  knee FLOAT,
                  cuff_width FLOAT,
                  shoulder_type varchar(50),
                  bottom_width FLOAT,
                  sleeve_length FLOAT,
                  shoulder_length FLOAT,
                  underline FLOAT,
                  quantity FLOAT,
                  FOREIGN KEY (customer_id) REFERENCES customers(id))''')
# Connect to the database and create the measurements table
def save_measurements():
    # Fetch the entered data from the entry boxes and drop-down list
    customer_id=mp_entry19.get().strip()
    shirt_length = mp_entry0.get().strip()
    sleeve_width = mp_entry1.get().strip()
    pant_length = mp_entry2.get().strip()
    collor_length = mp_entry3.get().strip()
    chest_width1 = mp_entry4.get().strip()
    waist = mp_entry5.get().strip()
    collor_width = mp_entry6.get().strip()
    chest_width2 = mp_entry7.get().strip()
    thigh_width = mp_entry8.get().strip()
    cuff_length = mp_entry9.get().strip()
    chest_width3 = mp_entry10.get().strip()
    knee = mp_entry11.get().strip()
    cuff_width = mp_entry12.get().strip()
    shoulder_type = mp_entry13.get().strip()
    bottom_width = mp_entry14.get().strip()
    sleeve_length = mp_entry15.get().strip()
    shoulder_length = mp_entry16.get().strip()
    underline = mp_entry17.get().strip()
    quantity = mp_entry20.get().strip()
    category = measurement_pro_category_ddl.get().strip()

    # Validate the input

    if not shirt_length.isdigit():
        tkinter.messagebox.showerror("Error", "Shirt Length measurement must be a number")
        return
    if not sleeve_width.isdigit():
        tkinter.messagebox.showerror("Error", "Sleeve Width measurement must be a number")
        return
    if not pant_length.isdigit():
        tkinter.messagebox.showerror("Error", "pant length measurement must be a number")
        return
    if not collor_length.isdigit():
        tkinter.messagebox.showerror("Error", "collor length measurement must be a number")
        return
    if not chest_width1.isdigit():
        tkinter.messagebox.showerror("Error", "chest width measurement must be a number")
        return
    if not waist.isdigit():
        tkinter.messagebox.showerror("Error", "waist measurement must be a number")
        return
    if not collor_width.isdigit():
        tkinter.messagebox.showerror("Error", "collor width measurement must be a number")
        return
    if not chest_width2.isdigit():
        tkinter.messagebox.showerror("Error", "Chest width 2 measurement must be a number")
        return
    if not thigh_width.isdigit():
        tkinter.messagebox.showerror("Error", "thigh width measurement must be a number")
        return
    if not cuff_length.isdigit():
        tkinter.messagebox.showerror("Error", "cuff length measurement must be a number")
        return
    if not chest_width3.isdigit():
        tkinter.messagebox.showerror("Error", "Chest width 3 measurement must be a number")
        return
    if not knee.isdigit():
        tkinter.messagebox.showerror("Error", "knee measurement must be a number")
        return
    if not cuff_width.isdigit():
        tkinter.messagebox.showerror("Error", "cuff width measurement must be a number")
        return
    if not shoulder_type.isalpha():
        tkinter.messagebox.showerror("Error", "shoulder Type measurement must be a Letters")
        return
    if not bottom_width.isdigit():
        tkinter.messagebox.showerror("Error", "Bottom Width measurement must be a number")
        return
    if not sleeve_length.isdigit():
        tkinter.messagebox.showerror("Error", "Sleeve Length measurement must be a number")
        return
    if not shoulder_length.isdigit():
        tkinter.messagebox.showerror("Error", "Shoulder Length measurement must be a number")
        return
    if not underline.isdigit():
        tkinter.messagebox.showerror("Error", "Underline measurement must be a number")
        return
    if not quantity.isdigit():
        tkinter.messagebox.showerror("Error", "Quantity measurement must be a number")
        return

    # Connect to the database and save the measurements
    conn = sqlite3.connect('tailor_shop.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS measurements
                 (id INTEGER PRIMARY KEY,
                  customer_id INTEGER,
                  category TEXT,
                  shirt_length FLOAT,
                  sleeve_width FLOAT,
                  pant_length FLOAT,
                  collor_length FLOAT,
                  chest_width1 FLOAT,
                  waist FLOAT,
                  collor_width FLOAT,
                  chest_width2 FLOAT,
                  thigh_width FLOAT,
                  cuff_length FLOAT,
                  chest_width3 FLOAT,
                  knee FLOAT,
                  cuff_width FLOAT,
                  shoulder_type varchar(50),
                  bottom_width FLOAT,
                  sleeve_length FLOAT,
                  shoulder_length FLOAT,
                  underline FLOAT,
                  quantity INT,
                  FOREIGN KEY (customer_id) REFERENCES customers(id))''')

    c.execute("SELECT * FROM measurements WHERE customer_id = ?", (customer_id,))
    measuremets=c.fetchone()
    if measuremets:
        c.execute('''UPDATE measurements SET customer_id = ?, category = ?, shirt_length = ?, sleeve_width = ?, 
        pant_length = ?, 
        collor_length = ?, chest_width1 = ?, waist = ?, collor_width = ?, chest_width2 = ?, thigh_width = ?, 
        cuff_length = ?, chest_width3 = ?, 
        knee = ?, cuff_width = ?, shoulder_type = ?, bottom_width = ?, sleeve_length = ?, shoulder_length = ?, 
        underline = ?, quantity = ? ''', (customer_id, category, shirt_length,sleeve_width, pant_length,
                                                                                 collor_length, chest_width1, waist,
                                                                                 collor_width, chest_width2,
                                                                                 thigh_width, cuff_length, chest_width3,
                                                                                 knee, cuff_width, shoulder_type,
                                                                                 bottom_width, sleeve_length,
                                                                                 shoulder_length, underline, quantity))

    else:
        c.execute('''INSERT INTO measurements(customer_id, category, shirt_length, sleeve_width, pant_length, 
                collor_length, chest_width1, waist, collor_width, chest_width2, thigh_width, cuff_length, chest_width3, 
                knee, cuff_width, shoulder_type, bottom_width, sleeve_length, shoulder_length, underline, quantity) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (customer_id, category, shirt_length,
                   sleeve_width, pant_length,
                   collor_length, chest_width1, waist,
                   collor_width, chest_width2,
                   thigh_width, cuff_length, chest_width3,
                   knee, cuff_width, shoulder_type,
                   bottom_width, sleeve_length,
                   shoulder_length, underline, quantity))

    conn.commit()
    conn.close()

    # Show a success message
    tkinter.messagebox.showinfo("Success", "Measurements saved successfully")

#---fetch and update measuements

def search_customer_measurement():
    # Fetch the entered data from entry boxes
    customer_id = mp_entry19.get()

    # Connect to the database and search for the customer
    conn = sqlite3.connect('tailor_shop.db')
    c = conn.cursor()
    c.execute("SELECT * FROM measurements WHERE customer_id=?", (customer_id,))
    measurements = c.fetchone()

    # Fetch the customer name from the customers table
    c.execute("SELECT name FROM customers WHERE id = ?", (customer_id,))
    customer_name = c.fetchone()[0]
    mp_entry18.delete(0, 'end')
    mp_entry18.insert(0, customer_name)

    # Display the customer details in the entry boxes
    if measurements:
        mp_entry0.delete(0, 'end')
        mp_entry0.insert(0, int(measurements[3]))
        mp_entry1.delete(0, 'end')
        mp_entry1.insert(0, int(measurements[4]))
        mp_entry2.delete(0, 'end')
        mp_entry2.insert(0, int(measurements[5]))
        mp_entry3.delete(0, 'end')
        mp_entry3.insert(0, int(measurements[6]))
        mp_entry4.delete(0, 'end')
        mp_entry4.insert(0, int(measurements[7]))
        mp_entry5.delete(0, 'end')
        mp_entry5.insert(0, int(measurements[8]))
        mp_entry6.delete(0, 'end')
        mp_entry6.insert(0, int(measurements[9]))
        mp_entry7.delete(0, 'end')
        mp_entry7.insert(0, int(measurements[10]))
        mp_entry8.delete(0, 'end')
        mp_entry8.insert(0, int(measurements[11]))
        mp_entry9.delete(0, 'end')
        mp_entry9.insert(0, int(measurements[12]))
        mp_entry10.delete(0, 'end')
        mp_entry10.insert(0, int(measurements[13]))
        mp_entry11.delete(0, 'end')
        mp_entry11.insert(0, int(measurements[14]))
        mp_entry12.delete(0, 'end')
        mp_entry12.insert(0, int(measurements[15]))
        mp_entry13.delete(0, 'end')
        mp_entry13.insert(0, str(measurements[16]))
        mp_entry14.delete(0, 'end')
        mp_entry14.insert(0, int(measurements[17]))
        mp_entry15.delete(0, 'end')
        mp_entry15.insert(0, int(measurements[18]))
        mp_entry16.delete(0, 'end')
        mp_entry16.insert(0, int(measurements[19]))
        mp_entry17.delete(0, 'end')
        mp_entry17.insert(0, int(measurements[20]))
        mp_entry19.delete(0, 'end')
        mp_entry19.insert(0, int(measurements[1]))
        mp_entry20.delete(0, 'end')
        mp_entry20.insert(0, int(measurements[21]))
        measurement_pro_category_ddl.set(measurements[2])

    else:
        tkinter.messagebox.showerror("Error", "No measurements found for customer ID " + customer_id)
    conn.commit()
    conn.close()

def clear_measurements():
    mp_entry0.delete(0, 'end')
    mp_entry1.delete(0, 'end')
    mp_entry2.delete(0, 'end')
    mp_entry3.delete(0, 'end')
    mp_entry4.delete(0, 'end')
    mp_entry5.delete(0, 'end')
    mp_entry6.delete(0, 'end')
    mp_entry7.delete(0, 'end')
    mp_entry8.delete(0, 'end')
    mp_entry9.delete(0, 'end')
    mp_entry10.delete(0, 'end')
    mp_entry11.delete(0, 'end')
    mp_entry12.delete(0, 'end')
    mp_entry13.delete(0, 'end')
    mp_entry14.delete(0, 'end')
    mp_entry15.delete(0, 'end')
    mp_entry16.delete(0, 'end')
    mp_entry17.delete(0, 'end')
    mp_entry19.delete(0, 'end')
    mp_entry20.delete(0, 'end')
    measurement_pro_category_ddl.set("")
    mp_entry18.delete(0, 'end')


def mp_clear_and_back():
    # Call the clear page function
    clear_measurements()

    # Call the second function using lambda function
    mp_pg_back_btn.after(0, lambda :show_frame(search_page) )
#-------======measurement page-buttons code========

mp_update_btn = Button(measurement_page,
    image = mp_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = save_measurements,
    relief = "flat")

mp_update_btn.place(
    x = 1151, y = 632,
    width = 175,
    height = 61)
#---
mp_search_with_cusID_btn = Button(measurement_page,
    image = mp_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = search_customer_measurement,
    relief = "flat")

mp_search_with_cusID_btn.place(
    x = 100, y = 225,
    width = 132,
    height = 41)


mp_pg_back_btn = Button(measurement_page,
    image = mp_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = mp_clear_and_back,
    relief = "flat")

mp_pg_back_btn.place(
    x = 1151, y = 43,
    width = 175,
    height = 61)


# ######################################################################################################
# #############################------SEARCH-PAGE-------####################################################

sp_background_img = PhotoImage(file = f"sp_background.png")
sp_label=Label(search_page,image=sp_background_img)
sp_label.place(x=0, y=0)

# -----------Image declaration of update-page-------------
sp_background_img = PhotoImage(file = f"sp_background.png")
sp_img0 = PhotoImage(file = f"sp_img0.png")
sp_entry0_img = PhotoImage(file = f"sp_img_textBox0.png")
sp_entry1_img = PhotoImage(file = f"sp_img_textBox1.png")
sp_img1 = PhotoImage(file = f"sp_img1.png")
sp_img2 = PhotoImage(file = f"sp_img2.png")
sp_img3 = PhotoImage(file = f"sp_img3.png")


# -----------BG of update-page-------------
sp_label_of_bg = Label(search_page,image=sp_background_img)
sp_label_of_bg.place(x=0,y=0)

# -----------entry box bg of update-page-------------

sp_entry0_bg = Label(search_page,image=sp_entry0_img)
sp_entry0_bg.place(x = 239.0, y = 203)
# -----
sp_entry1_bg = Label(search_page,image=sp_entry1_img)
sp_entry1_bg.place( x = 558.0, y = 203)
# -----

# -----entry box code -search page---
sp_entry0 = Entry(search_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

sp_entry0.place(
    x = 244.0, y = 205,
    width = 88.0,
    height = 39)

#--------
sp_entry1 = Entry(search_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

sp_entry1.place(
    x = 563.0, y = 205,
    width = 397.0,
    height = 39)

##########----DATA BASE QUERIES and search functions

def sp_search_customer():
    # Fetch the entered data from the entry boxes
    id = sp_entry0.get().strip()
    name = sp_entry1.get().strip()

    # Validate the input
    if not id.isdigit() and id != "":
        tkinter.messagebox.showerror("Error", "ID must be a number")
        return
    if not name.isalpha() and name != "":
        tkinter.messagebox.showerror("Error", "Name must contain only letters")
        return

    # Connect to the database and search for the customer
    conn = sqlite3.connect('tailor_shop.db')
    c = conn.cursor()

    if id != "":
        c.execute("SELECT * FROM customers WHERE id=?", (id,))
    elif name != "":
        c.execute("SELECT * FROM customers WHERE name LIKE ?", ('%' + name + '%',))
    else:
        c.execute("SELECT * FROM customers")

    customers = c.fetchall()

    # Display the search results in the treeview
    tree.delete(*tree.get_children())
    if customers:
        for customer in customers:
            tree.insert("", "end", values=customer)
    else:
        tkinter.messagebox.showinfo("No Results Found", "No customers found for the given search query")

    conn.close()
#----Tree View

# Create the treeview to display the search results
tree = ttk.Treeview(search_page)
tree["columns"] = ("ID", "Name", "Phone", "Email", "Address")
tree.column("#0", width=0, stretch=tkinter.NO)
tree.column("ID", width=20)
tree.column("Name", width=150)
tree.column("Phone", width=100)
tree.column("Email", width=200)
tree.column("Address", width=200)
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")
tree.heading("Address", text="Address")

# Add the widgets to the window
tree.place(x=225,y=340)

#---
def sp_clear_measurements():
    sp_entry1.delete(0, 'end')
    sp_entry0.delete(0, 'end')

def sp_clear_and_back():
    # Call the clear page function
    sp_clear_measurements()

    # Call the second function using lambda function
    sp_back_btn.after(0, lambda: show_frame(home_page))

#======search page-buttons code========

search_with_cusID_btn = Button(search_page,
    image = sp_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = sp_search_customer,
    relief = "flat")

search_with_cusID_btn.place(
    x = 179, y = 260,
    width = 132,
    height = 41)
#----
sp_measurement_btn = Button(search_page,
    image = sp_img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :show_frame(measurement_page),
    relief = "flat")

sp_measurement_btn.place(
    x = 1151, y = 115,
    width = 175,
    height = 61)
# width = 175,
# height = 61)
#----
search_with_cusName_btn = Button(search_page,
    image = sp_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = sp_search_customer,
    relief = "flat")

search_with_cusName_btn.place(
    x = 631, y = 260,
    width = 132,
    height = 41)
#----
sp_back_btn = Button(search_page,
    image = sp_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = sp_clear_and_back,
    # command = lambda :show_frame(home_page),
    relief = "flat")

sp_back_btn.place(
    x = 1151, y = 43,
    width = 175,
    height = 61)


# ######################################################################################################
# #############################------PAYMENT-PAGE-------####################################################

# -----------Image declaration of payment-page-------------
pp_background_img = PhotoImage(file = f"pp_background.png")
pp_img0 = PhotoImage(file = f"pp_img0.png")
pp_entry0_img = PhotoImage(file = f"pp_img_textBox0.png")
pp_entry1_img = PhotoImage(file = f"pp_img_textBox1.png")
pp_entry2_img = PhotoImage(file = f"pp_img_textBox2.png")
pp_entry3_img = PhotoImage(file = f"pp_img_textBox3.png")
pp_entry4_img = PhotoImage(file = f"pp_img_textBox4.png")
pp_img1 = PhotoImage(file = f"pp_img1.png")
pp_img2 = PhotoImage(file = f"pp_img2.png")
pp_img3 = PhotoImage(file = f"pp_img3.png")

# -----------BG of payment-page-------------
pp_label_of_bg = Label(payment_page,image=pp_background_img)
pp_label_of_bg.place(x=0,y=0)

# -----------entry box bg of update-page-------------

pp_entry0_bg = Label(payment_page,image=pp_entry0_img)
pp_entry0_bg.place( x = 330.0, y = 483)
# -----
pp_entry1_bg = Label(payment_page,image=pp_entry1_img)
pp_entry1_bg.place( x = 330.0, y = 413)
# -----
pp_entry2_bg = Label(payment_page,image=pp_entry2_img)
pp_entry2_bg.place( x = 330.0, y = 343)
# -----
pp_entry3_bg = Label(payment_page,image=pp_entry3_img)
pp_entry3_bg.place(x = 330.0, y = 273)
# -----
pp_entry4_bg = Label(payment_page,image=pp_entry4_img)
pp_entry4_bg.place(x = 330.0, y = 203)

#-------Entry Box Code of Payment Page--

pp_entry4 = Entry(payment_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

pp_entry4.place(
    x = 335.0, y = 205,
    width = 321.0,
    height = 38)

pp_entry3 = Entry(payment_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

pp_entry3.place(
    x = 335.0, y = 275,
    width = 321.0,
    height = 38)

pp_entry2 = Entry(payment_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

pp_entry2.place(
    x = 335.0, y = 345,
    width = 321.0,
    height = 38)

pp_entry1 = Entry(payment_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

pp_entry1.place(
    x = 335.0, y = 415,
    width = 321.0,
    height = 38)

pp_entry0 = Entry(payment_page,
    bd = 0,font=("arial",15),
    bg = "#ffffff",
    highlightthickness = 0)

pp_entry0.place(
    x = 335.0, y = 486,
    width = 321.0,
    height = 38)
#################-----DATA-BASE QUERIES AND CALCULATIONS.-----######
#


# Connect to the payments database
conn = sqlite3.connect('tailor_shop.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS payments
             (id INTEGER PRIMARY KEY,
              cus_id INTEGER,
              cus_name TEXT,
              paid_amount REAL,
              balance_amount REAL,
              total_bill REAL)''')

# Function to search for a customer by id and return their name
def search_customer(cus_id):
    cus_id = int(pp_entry4.get())
    c.execute("SELECT name FROM customers WHERE id = ?", (cus_id,))
    customer = c.fetchone()
    if customer:
        pp_entry3.delete(0, END)
        pp_entry3.insert(0, customer[0])
        tkinter.messagebox.showinfo('Success',"Customer found: " + customer[0])
    else:
        tkinter.messagebox.showinfo('Error',"Customer not found for ID: " + str(cus_id))

# Function to search for a payment by cus_id and display the details in the entry boxes
def search_payment():
    cus_id = int(pp_entry4.get())
    cus_name = search_customer(cus_id)

    c.execute("SELECT * FROM payments WHERE cus_id = ?", (cus_id,))
    payment = c.fetchone()
    if payment:
            pp_entry2.delete(0, END)
            pp_entry2.insert(0, payment[3])
            pp_entry1.delete(0, END)
            pp_entry1.insert(0, payment[4])
            pp_entry0.delete(0, END)
            pp_entry0.insert(0, payment[5])
            tkinter.messagebox.showinfo('Success',"Payment found for customer ID: " + str(cus_id))
    else:
            tkinter.messagebox.showinfo('Error',"No Payment previous data found with Customer ID: " + str(cus_id))

#---------------------
def save_payment():
    cus_id = int(pp_entry4.get())
    cus_name = pp_entry3.get()
    paid_amount = pp_entry2.get()
    total_bill = pp_entry0.get()

    if total_bill=="":
        tkinter.messagebox.showerror('Error', 'Total bill Cannot Be Empty '
                                              '\nEnter Amount in Numbers.')
        return
    # Validate the total_bill input
    try:
        total_bill = float(total_bill)
    except ValueError:
        tkinter.messagebox.showerror('Error', 'Total bill must be entered in numbers.')
        return
    if paid_amount=="":
        tkinter.messagebox.showerror('Error', 'Paid Amount Cannot Be Empty '
                                              '\nEnter Amount in Numbers.')
        return

    try:
        paid_amount = float(paid_amount)
    except ValueError:
        pass
        # tkinter.messagebox.showerror('Error', 'Paid Amount must be entered in numbers.')
        return

    balance_amount = total_bill - paid_amount

    # Check if the payment already exists
    c.execute("SELECT * FROM payments WHERE cus_id = ?", (cus_id,))
    payment = c.fetchone()
    if payment:
        # Update the existing payment
        c.execute(
            "UPDATE payments SET cus_name = ?, paid_amount = ?, balance_amount = ?, total_bill = ? WHERE cus_id = ?",
            (cus_name, paid_amount, balance_amount, total_bill, cus_id))
        tkinter.messagebox.showinfo('Success', "Payment updated successfully.")

    else:
        # Insert a new payment
        c.execute(
            "INSERT INTO payments (cus_id, cus_name, paid_amount, balance_amount, total_bill) VALUES (?, ?, ?, ?, ?)",
            (cus_id, cus_name, paid_amount, balance_amount, total_bill))
        tkinter.messagebox.showinfo('Success', "Payment added successfully.")

    conn.commit()

    # Generate the PDF receipt
    filename = generate_receipt(cus_id, cus_name, paid_amount, balance_amount, total_bill)

    tkinter.messagebox.showinfo('Success', f"Payment added successfully.\nReceipt saved as: {filename}")
# #---------------------Generate Recipt Code Starts Here---

def generate_receipt(cus_id, cus_name, paid_amount, balance_amount, total_bill):
    # Create a new PDF file
    filename = f"receipt_{cus_id}_{cus_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=landscape(A5))

    # Set up the default font and size
    c.setFont("Helvetica", 12)

    # Draw the shop name and address
    c.setFont("Helvetica-Bold", 20)
    shop_name = "Patel Tailors"
    shop_name_width = c.stringWidth(shop_name)
    c.drawCentredString(300, 360, shop_name)
    c.setFont("Helvetica", 12)
    c.drawCentredString(300, 345, "Bale, Pune Road, Solapur")
    c.drawCentredString(300, 330, "Maharashtra, 413001")

    # Draw a horizontal line
    c.line(100, 320, 500, 320)

    # Draw the customer details and payment details
    c.setFont("Helvetica-Bold", 14)
    c.drawString(70, 280, "Customer Details")
    c.drawString(320, 280, "Payment Details")
    c.setFont("Helvetica", 12)
    c.drawString(70, 260, f"Customer ID: {cus_id}")
    c.drawString(70, 240, f"Customer Name: {cus_name}")
    c.drawString(320, 260, f"Total Bill: ₹{total_bill:.2f}")
    c.drawString(320, 240, f"Paid Amount: ₹{paid_amount:.2f}")
    c.drawString(320, 220, f"Balance Amount: ₹{balance_amount:.2f}")

    # Save and close the PDF file
    c.save()

    return filename
    #---

# Clear all the entry boxes
def clear_entries():
    pp_entry0.delete(0, END)
    pp_entry1.delete(0, END)
    pp_entry2.delete(0, END)
    pp_entry3.delete(0, END)
    pp_entry4.delete(0, END)

def pp_clear_and_back():
    # Call the clear page function
    clear_entries()

    # Call the second function using lambda function
    pp_b1.after(0, lambda: show_frame(home_page))
#-----------Buttons Code of payment Page
pp_b0 = Button(payment_page,
    image = pp_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = save_payment,
    relief = "flat")

pp_b0.place(
    x = 347, y = 581,
    width = 288,
    height = 61)
##-------
pp_b1 = Button(payment_page,
    image = pp_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = pp_clear_and_back,
    # command = lambda :show_frame(home_page),
    relief = "flat")

pp_b1.place(
    x = 1151, y = 43,
    width = 175,
    height = 61)
# #------
# pp_b2 = Button(payment_page,
#     image = pp_img2,
#     borderwidth = 0,
#     highlightthickness = 0,
#     # command = generate_receipt,
#     relief = "flat")
#
# pp_b2.place(
#     x = 913, y = 203,
#     width = 175,
#     height = 61)
#------
pp_b3 = Button(payment_page,
    image = pp_img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = search_payment,
    relief = "flat")

pp_b3.place(
    x = 713, y = 203,
    width = 132,
    height = 41)
#------
# ######################################################################################################
loginwindow.resizable(True, True)
loginwindow.mainloop()
