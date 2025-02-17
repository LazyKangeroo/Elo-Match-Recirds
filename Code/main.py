from tkinter import *
from handle import *

# Handle modules
new = New()
sort = Sort()
screens = Screens()

#main window
win = Tk()

# details
win.title('Chess Team Rankings')
win.geometry('950x700')

icon = PhotoImage(file='./icons/chess-board.png')
win.iconphoto(True,icon)

# all widgets will be here
# Head frame
frame_head = Frame(win).pack(side=TOP)
lblHead = Label(frame_head,text='Chess Game Records',font=('Arial',20,'bold'),fg='#5c5fff').pack()

## Home frame ##
frame_home = Frame(win)
frame_home.pack()

## New Game frame ##
frame_newgame = Frame(win)
frame_newgame.pack()

innerFrame_playerA_name = Frame(frame_newgame,pady=20)
innerFrame_playerA_name.pack()
innerFrame_playerA_surname = Frame(frame_newgame,pady=20)
innerFrame_playerA_surname.pack()

innerFrame_game_result = Frame(frame_newgame,pady=20)
innerFrame_game_result.pack()

innerFrame_playerB_name = Frame(frame_newgame,pady=20)
innerFrame_playerB_name.pack()
innerFrame_playerB_surname = Frame(frame_newgame,pady=20)
innerFrame_playerB_surname.pack()

    # lbl
lblPlayerA_Head = Label(innerFrame_playerA_name,font=('Arial',15,'bold'),text='Player A',padx=10)
lblPlayerA_name = Label(innerFrame_playerA_name,font=('Arial',13),text='First Name',padx=10)
lblPlayerA_surname = Label(innerFrame_playerA_surname,font=('Arial',13),text='Last Name',padx=10)

lblPlayerB_Head = Label(innerFrame_playerB_name,font=('Arial',15,'bold'),text='Player B',padx=10)
lblPlayerB_name = Label(innerFrame_playerB_name,font=('Arial',13),text='First Name',padx=10)
lblPlayerB_surname = Label(innerFrame_playerB_surname,font=('Arial',13),text='Last Name',padx=10)

lblGameResult = Label(innerFrame_game_result,font=('Arial',13),text='Result',padx=12)
    # Textbox
entryPlayerA_name = Entry(innerFrame_playerA_name,font=('Arial',13),width=20)
entryPlayerA_surname = Entry(innerFrame_playerA_surname,font=('Arial',13),width=20)

entryPlayerB_name = Entry(innerFrame_playerB_name,font=('Arial',13),width=20)
entryPlayerB_surname = Entry(innerFrame_playerB_surname,font=('Arial',13),width=20)

entryResult = Entry(innerFrame_game_result,font=('Arial',13),width=10)
    # btn
btnSubmitNewPlayer = Button(frame_newgame,font=('Arial',15,'bold'),text='Submit',activebackground='#111d2e',activeforeground='#5b8fd9', bg='#5b8fd9', fg='#111d2e', command=lambda : new.game(entryPlayerA_name.get(),entryPlayerA_surname.get(),entryPlayerB_name.get(),entryPlayerB_surname.get(),entryResult.get()))
    # Display
lblPlayerA_Head.pack(side=TOP)
lblPlayerA_name.pack(side=LEFT)
lblPlayerA_surname.pack(side=LEFT)

lblPlayerB_Head.pack(side=TOP)
lblPlayerB_name.pack(side=LEFT)
lblPlayerB_surname.pack(side=LEFT)

lblGameResult.pack(side=LEFT)
entryResult.pack(side=RIGHT)

entryPlayerA_name.pack(side=RIGHT)
entryPlayerA_surname.pack(side=RIGHT)

entryPlayerB_name.pack(side=RIGHT)
entryPlayerB_surname.pack(side=RIGHT)

btnSubmitNewPlayer.pack(side=BOTTOM)

## New player frame ##
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
entryGrade = Entry(innerFrame_new_grade,font=('Arial',13),width=10)
    # btn
newPlayer_Enteries = [entryName,entrySurname,entryGrade]
btnSubmitNewPlayer = Button(frame_newplayer,font=('Arial',15,'bold'),text='Submit',activebackground='#111d2e',activeforeground='#5b8fd9', bg='#5b8fd9', fg='#111d2e', command=lambda : new.player(entryName.get(),entrySurname.get(),entryGrade.get(),newPlayer_Enteries))
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
viewMenu.add_command(label='New Player',command=lambda : screens.show_hide(frame_newplayer,frame_newgame,frame_home,frame_profile))
viewMenu.add_command(label='New Game',command=lambda : screens.show_hide(frame_newgame,frame_newplayer,frame_home,frame_profile))
viewMenu.add_separator()
viewMenu.add_command(label='Home',command=lambda : screens.show_hide(frame_home,frame_newgame,frame_newplayer,frame_profile))

if screens.count < 1:
    screens.show_hide(frame_home,frame_newgame,frame_newplayer,frame_profile)

# run main win
win.mainloop()