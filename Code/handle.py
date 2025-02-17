import json
from tkinter import *
from tkinter import messagebox

class New:
    def __init__(self):
        self.mess = Messages()
        self.screen = Screens()

    def player(self, enteries):
        # Validation
        if enteries["name"].get() == '' or enteries["surname"].get() == '' or enteries["grade"].get() == '':
            self.mess.ValidationInfoOmitted()
            return
        if self.mess.Submit() == False:
            return
        if self.mess.intValidation(enteries["grade"].get()) == False:
            return
        if self.mess.grRandgeValidation(enteries["grade"].get()) == False:
            return

        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []  # Create a new list if file doesn't exist

        # Append new data
        player = {
            "name" : enteries["name"].get().upper(),
            "surname" : enteries["surname"].get().upper(),
            "grade" : int(enteries["grade"].get()),
            "games" : {
                "wins" : 0,
                "loses" : 0,
                "draws" : 0,
                "amnt" : 0,
                "results" : []
                }
        }
        if self.mess.doubleEntery(data,player):
        # Write updated data back to the file
            data.append(player)
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        self.screen.clearEnterys(enteries)

    def game(self,playerA_name,playerA_surname,playerB_name,playerB_surnameresult,result):
        # add playerA as opponet for playerB vice versa
        # add game result by both
        # get new elo for both
        return

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

class Messages:
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