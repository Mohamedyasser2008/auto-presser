# Importing modules
from tkinter import *
from click import Clicker
# =================

# Setting up main window properies
app = Tk()
app.title("Keyboard clicker")
app.geometry("425x200")
app.resizable(False, False)
    # app.iconbitmap("")
# =================

label1 = Label(app, font="Arial 20 bold", text="Button: ")
label1.grid(row=1, column=1)

label2 = Label(app, font="Arial 20 bold", text="Time: ")
label2.grid(row=2, column=1)

label3 = Label(app, font="Arial 20 bold", text="Double: ")
label3.grid(row=3, column=1)

label4 = Label(app, font="Arial 20 bold", text="Mixed: ")
label4.grid(row=4, column=1)

entry1 = Entry(app, font="Arial 20 bold")
entry1.grid(row=1, column=2)

entry2 = Entry(app, font="Arial 20 bold", width=3)
entry2.grid(row=2, column=2)

entry3var = BooleanVar()
entry3 = Checkbutton(app, font="Arial 20 bold", variable=entry3var)
entry3.grid(row=3, column=2)

entry4 = Entry(app, font="Arial 20 bold")
entry4.grid(row=4, column=2)


# Defining clicking function
clicked = False
def click():
    global c
    global clicked
    if not clicked:
        if entry1.get() == "":
            print(entry4.get())
            ee = entry4.get().split()
            try:
                c = Clicker(ee[0], float(ee[1]), bool(ee[2][0].lower()=="y"  or  ee[2][0].lower()=="d"  or  ee[2][0].lower()=="t")) # checks if first leter of 3rd parameter is y,t,d
            except IndexError:
                c = Clicker(ee[0], float(ee[1]))
            finally:
                c.start()
        else:
            print(entry3var.get())
            try:
                c = Clicker(entry1.get(), float(entry2.get()), entry3var.get()) # checks if first leter of 3rd parameter is y,t,d
            except IndexError:
                c = Clicker(entry1.get(), float(entry2.get()))
            finally:
                c.start()
        clicked = True

# =================

# Defining stoping function
def stop():
    global c
    global clicked
    c.stop()
    clicked = False
# =================


button1 = Button(app, font="Arial 17 bold", text="Start",
                 command=click)
button1.grid(row=5, column=2)

button2 = Button(app, font="Arial 13 bold", text="Stop", 
                 fg="red", command=stop)
button2.grid(row=5, column=1)

# Looping the app
app.mainloop()
# =================