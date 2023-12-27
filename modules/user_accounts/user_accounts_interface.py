import customtkinter as tk
from tkinter import PhotoImage, ttk
from CTkMessagebox import CTkMessagebox
from modules.user_accounts.user_account import UserAccount


#create a class that inherits from tk.Frame and will be used to create the UI elements of the Home screen
class UserAccountInterface(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        self.addIcon = PhotoImage(file="./assets/icons/add_icon.png")
        self.clearIcon = PhotoImage(file="./assets/icons/clear_icon.png")
        self.updateIcon = PhotoImage(file="./assets/icons/update_icon.png")
        self.deleteIcon = PhotoImage(file="./assets/icons/delete_icon.png")

        #creating the models objects
        self.user_account = UserAccount()
        
        '''---------------- user interface -----------------'''
        self.label = tk.CTkLabel(self, text="Register Account" , font=("Helvetica", 24, "bold"))
        self.label.grid(row=0, column=1, padx=60, pady=20)

        self.frame = tk.CTkFrame(self)
        self.frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.frame.columnconfigure(0, weight=2)

        self.reg_frame = tk.CTkFrame(self)
        self.reg_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.reg_frame.columnconfigure(0, weight=1)

    
        #create labels and entry fields for username, password
        self.user_name_entry = tk.CTkEntry(self.reg_frame , 
                                           placeholder_text="Username",
                                           font=("Times New Roman", 22,),
                                           width=400,
                                           height=50,
                                           corner_radius=35,                      
                                           )
        self.user_name_entry.grid(row=0, column=0, padx=10,  pady=(70,10) , sticky="ew")

        self.password_entry = tk.CTkEntry(self.reg_frame , 
                                           placeholder_text="Password",
                                           font=("Times New Roman", 22,),
                                           width=400,
                                           height=50,
                                           corner_radius=35, 
                                           show='*'                     
                                           )
        self.password_entry.grid(row=1, column=0, padx=10, pady=(10,10) , sticky="ew")

        self.confirm_password_entry = tk.CTkEntry(self.reg_frame , 
                                           placeholder_text="Confirm Password",
                                           font=("Times New Roman", 22,),
                                           width=400,
                                           height=50,
                                           corner_radius=35, 
                                           show='*'                     
                                           )
        self.confirm_password_entry.grid(row=2, column=0, padx=10, pady=(10,10) , sticky="ew")



    
        self.add_user_button = tk.CTkButton(self.reg_frame, text="Create  Account",
                                               width=400, height=52, border_width=0,corner_radius=10, 
                                                font=("Times New Roman", 20,),
                                               text_color=("white", "#FFFFFF"),
                                            command=self.create_account, fg_color="#4E11A8")
        self.add_user_button.grid(row=3, column=0, padx=10, pady=(50,10))
        

    #a function to check the password and confirm password
    def check_password(self, password, confirm_password):
        if password == confirm_password:
            return True
        else:
            return False

    #a function to clear the form
    def clear_form(self):
        self.user_name_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.confirm_password_entry.delete(0, "end")
      
    def create_account(self):
        username = self.user_name_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if username and password and confirm_password:
            #check if the password and confirm password are the same
            if not self.check_password(password, confirm_password):
                CTkMessagebox(title="Error", message="Password and Confirm Password do not match")
                return
            
            self.user_account.add(username, password)
            #self.load_user_data()
            self.clear_form()
            CTkMessagebox(title="Info", message="User Added to the System")
        else:
            CTkMessagebox(title="Error", message="Please fill in all the fields")
