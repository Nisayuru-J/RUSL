import customtkinter as tk
from CTkMessagebox import CTkMessagebox
from tkinter import PhotoImage
from modules.Session.session import UserSession

from modules.user_accounts.user_account import UserAccount
#from utils.utils import Utils



class LoginInterface(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.parent = parent
        self.controller = controller
        self.user_account = UserAccount()
        #self.current_session = UserSession()

        self.loginImage = PhotoImage(file="./assets/images/loginImage.png")
        self.logoImage = PhotoImage(file="./assets/images/main.png")
        self.landingImage02 = PhotoImage(file="./assets/images/landing02.png")
        self.landingImage03 = PhotoImage(file="./assets/images/landing03.png")
     
 
       
        self.loginImage = tk.CTkLabel(self, image=self.loginImage, height=700, width=600 , text="", font=("Helvetica", 24, "bold"))
        self.loginImage.grid(row=0, column=0, padx=0, pady=0)

        #pannel to keep the buttons
        self.right_panel = tk.CTkFrame(self , #fg_color="transparent"
                                       )
        self.right_panel.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.label = tk.CTkLabel(self.right_panel, text="          Login Account       " , 
                                 font=("Times New Roman", 34, "bold",),   text_color=("black", "black"))
        self.label.grid(row=0, column=0, padx=(20,20), pady=(20, 10))
     
        self.user_name_entry = tk.CTkEntry(self.right_panel , 
                                           placeholder_text="Username",
                                           font=("Times New Roman", 22,),
                                           width=400,
                                           height=50,
                                           corner_radius=35,                      
                                           )
        self.user_name_entry.grid(row=1, column=0, padx=10,  pady=(70,10) , sticky="ew")

        self.password_entry = tk.CTkEntry(self.right_panel , 
                                           placeholder_text="Password",
                                           font=("Times New Roman", 22,),
                                           width=400,
                                           height=50,
                                           corner_radius=35, 
                                           show='*'                     
                                           )
        self.password_entry.grid(row=2, column=0, padx=10, pady=(10,10) , sticky="ew")


        self.get_started_btn = tk.CTkButton(self.right_panel, text="LOGIN",
                                               font=("Times New Roman", 25,),
                                               text_color=("white", "#FFFFFF"),
                                               width=160, height=60, border_width=0,corner_radius=10, 
                                               compound="left",
                                               command=self.validate_login,
                                              fg_color="#b51863")
        self.get_started_btn.grid(row=3, column=0, padx=(20,20), pady=(100,10))

        #create a clickable text - to move to the register page
        self.clickable_text = tk.CTkLabel(self.right_panel, text="Register", font=("Times New Roman", 22,), text_color=("#b51863", "#b51863"))
        self.clickable_text.grid(row=4, column=0, padx=10, pady=(10,10), sticky="ew")
        self.clickable_text.bind("<Button-1>", self.controller.open_register)


    #a function to validate the login
    def validate_login(self):
        username = self.user_name_entry.get()
        password = self.password_entry.get()
        
        #check if the username and password are not empty
        if username == "" or password == "":
            CTkMessagebox(title="Login Error", message="Please provide both username and password")
        else:
            #get the password for the username
            pwd = self.user_account.get_password(username)[0][0]
            print("--- Password obtained from the database ---", pwd)
            if(pwd == None):
                CTkMessagebox(title="Login Error", message="Incorrect username or password"
                                             )  
            #check if the password is correct
            elif password == pwd:
                print("Login Successful")
                self.controller.user_session.set_current_user(username, 1)
                self.controller.open_home()
            else:
                CTkMessagebox(title="Login Error", message="Your Password is Incorrect"
                                             )  
               



        
        



       
        

     
       
    

    

     
        
     

      

        

        
        

       