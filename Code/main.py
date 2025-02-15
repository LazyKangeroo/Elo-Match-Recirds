from tkinter import *

#root window
root = Tk()
root.title('Chess Team Rankings')
root.geometry('950x700')

# adding lbl
lbl = Label(root,text="Hello")
lbl.grid()

# function to display text when
# button is clicked
def clicked():
    lbl.configure(text = "I just got clicked")

# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)


# all widgets will be here

# run main root
root.mainloop()