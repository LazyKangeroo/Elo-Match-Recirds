from tkinter import *
from handle import *

# Handle modules
new = New()
sort = Sort()

count = 0

#main window
win = Tk()

# Show Hide
def show_hide(widget1,widget2,widget3,widget4):
    widget1.pack()
    widget2.pack_forget()
    widget3.pack_forget()
    widget4.pack_forget()
    global count
    count += 1

# details
win.title('Chess Team Rankings')
win.geometry('950x700')

icon = PhotoImage(file='./icons/chess-board.png')
win.iconphoto(True,icon)

# all widgets will be here
# Head frame
frame_head = Frame(win)
frame_head.pack(side=TOP)
lblHead = Label(frame_head,text='Chess Game Records',font=('Arial',20,'bold'),fg='#5c5fff')
lblHead.pack()

# Home frame
frame_home = Frame(win)
frame_home.pack()

# New Game frame
frame_newgame = Frame(win)
frame_newgame.pack()

# New player frame
frame_newplayer = Frame(win)
frame_newplayer.pack()

innerFrame_new_name = Frame(frame_newplayer,pady=20)
innerFrame_new_name.pack()
innerFrame_new_surname = Frame(frame_newplayer,pady=20)
innerFrame_new_surname.pack()
innerFrame_new_grade = Frame(frame_newplayer,pady=20)
innerFrame_new_grade.pack()

    # lbl
lblName = Label(innerFrame_new_name,font=('Arial',13),text='First Name',padx=10)
lblSurname = Label(innerFrame_new_surname,font=('Arial',13),text='Last Name',padx=10)
lblGrade = Label(innerFrame_new_grade,font=('Arial',13),text='Grade',padx=12)
    # Textbox
entryName = Entry(innerFrame_new_name,font=('Arial',13),width=20)
entrySurname = Entry(innerFrame_new_surname,font=('Arial',13),width=20)
entryGrade = Entry(innerFrame_new_grade,font=('Arial',13),width=20)
    # btn
btnSubmitNewPlayer = Button(frame_newplayer,font=('Arial',15,'bold'),text='Submit',activebackground='#111d2e',activeforeground='#5b8fd9', bg='#5b8fd9', fg='#111d2e', command=lambda : new.player(entryName.get(),entrySurname.get(),entryGrade.get()))
    # Display
lblName.pack(side=LEFT)
lblSurname.pack(side=LEFT)
lblGrade.pack(side=LEFT)
entryName.pack(side=RIGHT)
entrySurname.pack(side=RIGHT)
entryGrade.pack(side=RIGHT)
btnSubmitNewPlayer.pack(side=BOTTOM)

# Player pf frame
frame_profile = Frame(win)
frame_profile.pack()

# menu
menubar = Menu(win)
win.config(menu=menubar)

# sort players by
sortMenu = Menu(menubar,tearoff=0, font=('Arial',10))
menubar.add_cascade(label='Sort',menu=sortMenu)
sortMenu.add_command(label='Name')
sortMenu.add_command(label='Grade')
sortMenu.add_command(label='Elo')
sortMenu.add_separator()
sortMenu.add_command(label='Wins')
sortMenu.add_command(label='Lost')
sortMenu.add_command(label='Draws')

# actions
viewMenu = Menu(menubar,tearoff=0,font=('Arial',10))
menubar.add_cascade(label='View',menu=viewMenu)
viewMenu.add_command(label='New Player',command=lambda : show_hide(frame_newplayer,frame_newgame,frame_home,frame_profile))
viewMenu.add_command(label='New Game',command=lambda : show_hide(frame_newgame,frame_newplayer,frame_home,frame_profile))
viewMenu.add_separator()
viewMenu.add_command(label='Home',command=lambda : show_hide(frame_home,frame_newgame,frame_newplayer,frame_profile))

if count < 1:
    show_hide(frame_home,frame_newgame,frame_newplayer,frame_profile)

# run main win
win.mainloop()