# Importing modules
from tkinter import *
from click import Click
from threading import Thread
# =================

# Setting up main window properies
app = Tk()
app.title("Keyboard clicker")
app.geometry("425x200")
app.resizable(False, False)
    # app.iconbitmap("")
# =================

# Defining clicking function
clicked = False

def clicky(inp):   #click + diff.thread => clicky
    global clicked
    if not clicked:
        global c
        c = Click

        Thread(target=c, args=(inp,)).start()
        clicked = True
# =================

# Defining stoping thread function
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

entry2 = Entry(app, font="Arial 20 bold")
entry2.grid(row=2, column=2)

entry3 = Entry(app, font="Arial 20 bold")
entry3.grid(row=3, column=2)

entry4 = Entry(app, font="Arial 20 bold")
entry4.grid(row=4, column=2)


button1 = Button(app, font="Arial 17 bold", text="Start", 
                 command=lambda: clicky(entry4.get()))
button1.grid(row=5, column=2)

button2 = Button(app, font="Arial 13 bold", text="Stop", 
                 fg="red",)
button2.grid(row=5, column=1)

# Looping the app
app.mainloop()
# =================