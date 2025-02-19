from tkinter import *
from handle import *

# Functions for sorting
def compile(type,dect):
    players = new.getDataToRead()
    if dect != 0:
        players.sort(key=lambda player: player[dect][type], reverse=True)
    else:
        players.sort(key=lambda player: player[type], reverse=True)
    display(players)
    # self.display

def display(sorted_data):
    for row_num,player in enumerate(sorted_data):
        col = 0
        for info in player:
            if info == "games":
                w = 10
                for item in player[info]:
                    if item == "result":
                        continue
                    Label(frame_grid,font=('Arial',10),text=player[info][item],padx=10,pady=10,anchor='center',width=5).grid(row=row_num,column=col, sticky="ew")
                    col += 1
            else:
                Label(frame_grid,font=('Arial',10),text=player[info],padx=30,pady=10,anchor='center').grid(row=row_num,column=col, sticky="ew")
                col += 1

# Handle modules
new = New()
screens = Screens()

#main window
win = Tk()

# details
win.title('Chess Team Rankings')
win.geometry('1150x700')
win.grid_columnconfigure(0, weight=1)

icon = PhotoImage(file='./icons/chess-board.png')
win.iconphoto(True,icon)

# all widgets will be here
# Head frame
frame_head = Frame(win).pack(side=TOP)
lblHead = Label(frame_head,text='Chess Game Records',font=('Arial',20,'bold'),fg='#5c5fff').pack()

## Home frame ##
frame_home = Frame(win)
frame_home.pack()

frame_grid_lbl = Frame(frame_home)
frame_grid_lbl.pack()
frame_grid = Frame(frame_home)
frame_grid.pack()

    # lbl
lblPlayer_names = Label(frame_grid_lbl,font=('Arial',10,'underline'),text='Name',padx=20,pady=10,anchor='center',fg='#a65505',width=20)
lblPlayer_surnames = Label(frame_grid_lbl,font=('Arial',10,'underline'),text='Surname',padx=20,pady=10,anchor='center',fg='#a65505')
lblPlayer_grade = Label(frame_grid_lbl,font=('Arial',10,'underline'),text='Grade',padx=20,pady=10,anchor='center',fg='#a65505')
lblPlayer_elo = Label(frame_grid_lbl,font=('Arial',10,'underline'),text='ELO',padx=20,pady=10,anchor='center',fg='#a65505')
lblPlayer_wins = Label(frame_grid_lbl,font=('Arial',10,'underline'),text='Wins',padx=20,pady=10,anchor='center',fg='#a65505')
lblPlayer_losses = Label(frame_grid_lbl,font=('Arial',10,'underline'),text='Losses',padx=20,pady=10,anchor='center',fg='#a65505')
lblPlayer_draws = Label(frame_grid_lbl,font=('Arial',10,'underline'),text='Draws',padx=20,pady=10,anchor='center',fg='#a65505')
lblPlayer_games = Label(frame_grid_lbl,font=('Arial',10,'underline'),text='Game Amount',padx=20,pady=10,anchor='center',fg='#a65505')

    # display
lblPlayer_names.grid(row=0,column=0, sticky="ew")
lblPlayer_surnames.grid(row=0,column=1, sticky="ew")
lblPlayer_grade.grid(row=0,column=2, sticky="ew")
lblPlayer_elo.grid(row=0,column=3, sticky="ew")
lblPlayer_wins.grid(row=0,column=4, sticky="ew")
lblPlayer_losses.grid(row=0,column=5, sticky="ew")
lblPlayer_draws.grid(row=0,column=6, sticky="ew")
lblPlayer_games.grid(row=0,column=7, sticky="ew")

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
newGame_Enteries = [entryPlayerA_name,entryPlayerA_surname,entryPlayerB_name,entryPlayerB_surname,entryResult]
btnSubmitNewPlayer = Button(frame_newgame,font=('Arial',15,'bold'),text='Submit',activebackground='#111d2e',activeforeground='#5b8fd9', bg='#5b8fd9', fg='#111d2e', command=lambda : new.game(newGame_Enteries))
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
newPlayer_Enteries = [entryName, entrySurname,entryGrade]
btnSubmitNewPlayer = Button(frame_newplayer,font=('Arial',15,'bold'),text='Submit',activebackground='#111d2e',activeforeground='#5b8fd9', bg='#5b8fd9', fg='#111d2e', command=lambda : new.player(newPlayer_Enteries))
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
sortMenu.add_command(label='Grade',command=lambda : compile('grade',0))
sortMenu.add_command(label='Elo', command=lambda : compile('elo',0))
sortMenu.add_separator()
sortMenu.add_command(label='Wins',command=lambda : compile('wins','games'))
sortMenu.add_command(label='Lost',command=lambda : compile('losses','games'))
sortMenu.add_command(label='Draws',command=lambda : compile('draws','games'))
sortMenu.add_command(label="Games' Amount",command=lambda : compile('amnt','games'))

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