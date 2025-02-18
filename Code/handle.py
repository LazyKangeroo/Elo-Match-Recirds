import json
from tkinter import *
from tkinter import messagebox

from elo import Elo
from validation import Validation

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
        self.sortPlayersForNewElo(players_details["playerA"],players_details['playerB'])

        # Adding results to opponets records
        data = self.updateGamesRecords(players_details["playerA"],players_details["playerB"],self.getDataToRead())

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
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
        self.elo.getNewElo(playerA['result'],A,B)
        self.elo.getNewElo(playerB['result'],B,A)
        return

    def getDataToRead(self):
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []  # Create a new list if file doesn't exist
        return data

    def updateGamesRecords(self,playerA,playerB,data):
        for player in data:
            # Getting Player A
            if player["name"] == playerA["name"] and player["surname"] and playerA["surname"]:
                # appending opponents to records
                player["games"]["results"].append([f"{playerB['name']} {playerB['surname']}",[playerA["result"]]])
                # update total game records
                player["games"][self.getRecordsToUpdate(playerA["result"])] += 1
                player["games"]["amnt"] += 1
            # Getting Player B
            if player["name"] == playerB["name"] and player["surname"] and playerB["surname"]:
                # appending opponents to records
                player["games"]["results"].append([f"{playerA['name']} {playerA['surname']}",[playerB["result"]]])
                # update total game records
                player["games"][self.getRecordsToUpdate(playerB["result"])] += 1
                player["games"]["amnt"] += 1
        return data

    def getRecordsToUpdate(self,result):
        if result == 1:
            return "wins"
        if result == 0:
            return "losses"
        if result == 0.5:
            return "draws"

class Sort:
    def __init__(self):
        pass

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

    def clearEnterys(self,enteries):
        for item in enteries:
            item.delete(0,END)
        return