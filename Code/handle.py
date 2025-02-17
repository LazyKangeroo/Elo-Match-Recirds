import json
from tkinter import *
from tkinter import messagebox

class New:
    def __init__(self):
        self.val = Validation()
        self.screen = Screens()

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
            "games" : {
                "wins" : 0,
                "loses" : 0,
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
            print(type(players_details["playerA"]))
            print(players_details["playerA"])

        if self.val.nonExistingPlayer(self.getDataToRead(),players_details["playerB"]):
            print(type(players_details["playerB"]))
            print(players_details["playerB"])

        # Adding results to opponets records
        data = self.updateGamesRecords(players_details["playerA"],players_details["playerB"],self.getDataToRead())

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        # get new elo for both

        self.screen.clearEnterys(enteries)

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
        if result == '1':
            return "wins"
        if result == '0':
            return "loses"
        if result == '0.5' or result == '0,5' or  result == '1/2':
            return "draw"

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

    def clearEnterys(self,enteries):
        for item in enteries:
            item.delete(0,END)
        return

class Validation:
    def __init__(self):
        pass

    def ValidationInfoOmitted(self):
        messagebox.showerror(title='Values Ommitted', message='You have left out values which need to be entered for action to take place. Please input ALL values')

    def Submit(self):
        return messagebox.askyesno(title='Submit Values?', message='By clicking YES you are confirming that all entered values are correct and that you want to continue.')

    def intValidation(self,value):
        try:
            num = int(value)
        except:
            messagebox.showwarning('Invalid Value Entered', 'You can only enter NUMBERS not any letters,symbols,empty space')
            return False
        return True

    def grRandgeValidation(self,grade):
        if int(grade) > 12 or int(grade) < 8:
            messagebox.showwarning('Invalid Range', 'You can only enter Grade values from 8 to 12 (Highschool Levels)')
            return False
        return True

    def doubleEntery(self, data,player):
        for item in data:
            if item['name'] == player['name'] and item['surname'] == player['surname'] and item['grade'] == player['grade']:
                return messagebox.askyesno('Player Already Exists', 'The person you have entered already exists on the system. Do you want to overwrite the previous instince of this person.\nNOTE: Doing this will reset all this person past records and details.')
        return True

    def nonExistingPlayer(self, data, player):
        found = False
        for item in data:
            if item['name'] == player['name'] and item['surname'] == player['surname']:
                found = True
                messagebox.showinfo(title='Successful!',message='Game Successfully Added')

        if not found:
            messagebox.showerror(title='Non-Existing Player',message=f'Player entered ({player["name"]} {player["surname"]}) doesn`t exist in database.\nPossible reason could be that the name/surname was entered incorrectly OR you added unneeded space when typing the name/surname.\nOTHERWISE you will need to create a NEW PLAYER to continue')
            return True
        return False