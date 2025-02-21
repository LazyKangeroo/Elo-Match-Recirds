import json
from tkinter import *
from tkinter import messagebox

from elo import Elo
from validation import Validation

#########################################################################################################################################################################

class New:
    def __init__(self):
        self.val = Validation()
        self.screen = Screens()
        self.elo = Elo()

    def player(self, enteries):
        # Validation
        for item in enteries:
            if item.get() == '':
                self.val.ValidationInfoOmitted()
                return
        if self.val.Submit() == False:
            return
        if self.val.intValidation(enteries[2].get()) == False:
            return
        if self.val.grRandgeValidation(enteries[2].get()) == False:
            return

        data = self.getDataToRead()

        # Append new data
        player = {
            "name" : enteries[0].get().upper(),
            "surname" : enteries[1].get().upper(),
            "grade" : int(enteries[2].get()),
            "elo" : 500,
            "games" : {
                "wins" : 0,
                "losses" : 0,
                "draws" : 0,
                "amnt" : 0,
                "results" : []
                }
        }
        if self.val.doubleEntery(data,player):
        # Write updated data back to the file
            data.append(player)
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        self.screen.clearEnterys(enteries)

    def game(self,enteries):
        # input validation
        for item in enteries:
            if item.get() == '':
                self.val.ValidationInfoOmitted()
                return

        result_A = 0
        result_B = 0
        # formatting Result
        if enteries[4].get() == '1':
            result_A = 1
            result_B = 0
        elif enteries[4].get() == '0.5' or enteries[4].get() == '0,5' or  enteries[4].get() == '1/2':
            result_A = 0.5
            result_B = 0.5
        elif enteries[4].get() == '0':
            result_A = 0
            result_B = 1
        else:
            messagebox.showwarning(title='Range Error',message='Invalid inputs for Game Results.\nMust be (1 or 0 or 1/2 or 0.5 or 0,5)')
            return

        players_details = {
            "playerA" : {
                "name" : enteries[0].get().upper(),
                "surname" : enteries[1].get().upper(),
                "result" : result_A
            },
            "playerB" : {
                "name" : enteries[2].get().upper(),
                "surname" : enteries[3].get().upper(),
                "result" : result_B
            }
        }
        # checking if Player exists
        if self.val.nonExistingPlayer(self.getDataToRead(),players_details["playerA"]):
            return
        if self.val.nonExistingPlayer(self.getDataToRead(),players_details["playerB"]):
            return

        # get new elo for both
        A_elo = self.sortPlayersForNewElo(players_details["playerA"],players_details['playerB'])
        B_elo = self.sortPlayersForNewElo(players_details["playerB"],players_details['playerA'])

        # Adding results to records
        data = self.updateGamesRecords(players_details["playerA"],A_elo,players_details["playerB"],B_elo,self.getDataToRead())

        self.writeData(data)
        self.screen.clearEnterys(enteries)
        messagebox.showinfo(title='Successful!',message='Game Successfully Added')

    def sortPlayersForNewElo(self,playerA,playerB):
        data = self.getDataToRead()
        for item in data:
            if item['name'] == playerA["name"] and item['surname'] == playerA["surname"]:
                A = item
        for item in data:
            if item['name'] == playerB['name'] and item['surname'] == playerB['surname']:
                B = item
        return self.elo.getNewElo(playerA['result'],A,B)

    def getDataToRead(self):
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []  # Create a new list if file doesn't exist
        return data

    def writeData(self,data):
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def updateGamesRecords(self,playerA,A_elo,playerB,B_elo,data):
        for player in data:
            # Getting Player A
            if player["name"] == playerA["name"] and player["surname"] and playerA["surname"]:
                # appending opponents to records
                player["games"]["results"].append([f"{playerB['name']} {playerB['surname']}",B_elo,playerB["result"]])
                # update total game records
                player["games"][self.getRecordsToUpdate(playerA["result"])] += 1
                player["games"]["amnt"] += 1
                # update elo
                player["elo"] = A_elo
            # Getting Player B
            if player["name"] == playerB["name"] and player["surname"] and playerB["surname"]:
                # appending opponents to records
                player["games"]["results"].append([f"{playerA['name']} {playerA['surname']}",A_elo,playerB["result"]])
                # update total game records
                player["games"][self.getRecordsToUpdate(playerB["result"])] += 1
                player["games"]["amnt"] += 1
                # Adding elo
                player["elo"] = B_elo
        return data

    def getRecordsToUpdate(self,result):
        if result == 1:
            return "wins"
        if result == 0:
            return "losses"
        if result == 0.5:
            return "draws"

#########################################################################################################################################################################

class Screens:
    def __init__(self):
        self.count = 0

    def screenChanges(self,i):
        return i + 1

    # Show Hide
    def show_hide(self,widget1,widget2,widget3,widget4):
        widget1.pack()
        widget2.pack_forget()
        widget3.pack_forget()
        widget4.pack_forget()
        self.count += 1
        return

    def delete_widgets(self,frame, index_skip):
        for index, widget in enumerate(frame.winfo_children()):
            if index_skip <= index:
                widget.destroy()

    def clearEnterys(self,enteries):
        for item in enteries:
            item.delete(0,END)
        return

#########################################################################################################################################################################

class Profile:
    def __init__(self):
        self.val = Validation()
        self.screen = Screens()
        self.new = New()

    def lblClicked(self,event,name,surname,grade,frames):
        #Handles label click and prints the row & column.
        clicked_label = event.widget  # Get the clicked label
        self.screen.show_hide(frames[0],frames[1],frames[2],frames[3])
        self.loadProfile([name,surname,grade],frames[0],frames)

    def loadProfile(self,details,frame,frames):
        for items in self.new.getDataToRead():
            if items["name"] == details[0] and items["surname"] == details[1] and items["grade"] == details[2]:
                player = items
                break
        frame_grid = Frame(frame)
        frame_grid.pack(side=TOP)
        # row 0
        Label(frame_grid,text=f'{player["name"]} {player["surname"]}',font=('Arial',15,'bold'),width=20,padx=50,pady=20).grid(row=0,column=0,columnspan=2)
        Label(frame_grid,text=f'Elo: {player["elo"]}',font=('Arial',15,'bold'),width=20,padx=50,pady=20).grid(row=0,column=4,columnspan=2)
        Label(frame_grid,text=f'Grade: {player["grade"]}',font=('Arial',15,'bold'),width=10,padx=50,pady=20).grid(row=0,column=2,columnspan=1,sticky=NSEW)
        # row 1
        Label(frame_grid,text=f'Opponent:',font=('Arial',13,'underline'),pady=20,fg='#a65505').grid(row=1,column=0,columnspan=2,sticky=NW)
        Label(frame_grid,text=f'Result:',font=('Arial',13,'underline'),pady=20,fg='#a65505').grid(row=1,column=3,columnspan=2,sticky=NE)
        # the rest
        for row_num, games in enumerate(player["games"]["results"]):
            Label(frame_grid,cursor= "hand2",font=('Arial',11),text=games[0],pady=5).grid(row=row_num + 2,column=0, sticky=NW)
            Label(frame_grid,cursor= "hand2",font=('Arial',11),text=games[1],pady=5).grid(row=row_num + 2,column=2, sticky=EW)
            Label(frame_grid,cursor= "hand2",font=('Arial',11),text=games[2],pady=5).grid(row=row_num + 2,column=4, sticky=NE)

        # Button del frame
        del_frame = Frame(frame)
        del_frame.pack(side=BOTTOM)
        Button(del_frame, font=('Arial', 15, 'bold'), text='Delete', activebackground='black', activeforeground='red', bg='red', fg='white', command=lambda: self.delete(player,frames)).pack()

    def delete(self,player,frames):
        data = self.new.getDataToRead()
        for index,items in enumerate(data):
            if items["name"] == player["name"] and items["surname"] == player["surname"] and items["grade"] == player["grade"]:
                data.pop(index)
                break
        self.new.writeData(data)
        self.screen.show_hide(frames[1],frames[0],frames[2],frames[3])

        for index,widget in enumerate(frames[1].winfo_children()):
            if isinstance(widget, Frame):  # Checks if it's a frame
                self.screen.delete_widgets(widget,7)
        self.screen.delete_widgets(frames[0],0)

        messagebox.showinfo(title='Successfully Deleted!',message="You'll have to reselect how to sort players to update list")
        return