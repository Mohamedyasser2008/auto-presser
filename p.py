from tkinter import *
app = Tk()
app.geometry("500x230")

entry3var = BooleanVar()
entry3 = Checkbutton(app, textvariable=entry3var)
entry3.grid(row=3, column=2)

app.mainloop()