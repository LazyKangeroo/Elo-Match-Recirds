from tkinter import messagebox

class Validation:
    def __init__(self):
        pass

    def ValidationInfoOmitted(self):
        messagebox.showwarning(title='Values Omitted', message='You have left out values which need to be entered for action to take place. Please input ALL values')

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

        if not found:
            messagebox.showerror(title='Non-Existing Player',message=f'Player entered ({player["name"]} {player["surname"]}) doesn`t exist in database.\nPossible reason could be that the name/surname was entered incorrectly OR you added unneeded space when typing the name/surname.\nOTHERWISE you will need to create a NEW PLAYER to continue')
            return True
        return False

    def isData(self,data):
        if len(data) > 0:
            return True
        else:
            messagebox.showinfo(title='No Player Data',message='There seems to be no Players in the database.')
            return False

    def delWarning(self):
        return messagebox.askyesno(title='Deleting Player',message='Are you sure you want to delte this player?',icon=messagebox.WARNING)

    def formatStrInputs(self,text):
        text = text.upper()
        text = text.strip()
        return text