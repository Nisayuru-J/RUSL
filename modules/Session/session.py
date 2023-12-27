import tkinter as tk

class UserSession:
    def __init__(self):
        self.current_user = None
        self.current_titration = None

    def set_current_user(self, username, user_id):
        self.current_user = {
            'username': username,
            'user_id': user_id
        }
        print("Updated the Current USer to ", self.current_user)

    def get_current_user(self):
        return self.current_user
    
    def get_user_name(self):
        if(self.current_user == None):
            print("No user is logged in")
            return None
        else:
            return self.current_user['username']
    
    def logout(self):
        self.current_user = None

    def set_current_titration(self, reaction, indicator,analyte):
        self.current_titration = {
            'reaction': reaction,
            'indicator': indicator,
            'analyte':analyte
        }
        print("Updated the Current Titration to ", self.current_titration)
    
    def get_current_titrations(self):
        return self.current_titration

   