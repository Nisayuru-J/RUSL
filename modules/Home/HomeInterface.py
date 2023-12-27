#This will create the UI elements of the Home screen
import customtkinter as tk
from tkinter import PhotoImage, ttk
from modules.titration.titration import Titration

from modules.user_accounts.user_account import UserAccount
from modules.Session.session import UserSession


class HomeInterface(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent , fg_color="white")
        self.parent = parent
        self.toplevel_window = None
        self.parent = parent
        self.controller = controller
        self.titration_details = Titration()
        self.welcomeImg = PhotoImage(file="./assets/images/welcome.png")
        

        self.label = tk.CTkLabel(self, text="To Automate the Titration Process" , 
                                 font=("Times New Roman", 48,),   text_color=("black", "black"))
        self.label.grid(row=0, column=0,columnspan=2, padx=(200,10), pady=(50, 10))

        #create a panel - get_started_panel
        self.get_started_panel = tk.CTkFrame(self , 
                                            fg_color="#FFBEDE",
                                            width=400,
                                            height=300
                                            )
        self.get_started_panel.grid(row=1, column=0, padx=(180,10), pady=(80,20), sticky="nsew")

        #panel01 title
        self.get_started_panel_title = tk.CTkLabel(self.get_started_panel, text="Start Titration Process", 
                                 font=("Times New Roman", 26,),   text_color=("black", "white"))
        self.get_started_panel_title.grid(row=0, column=0, padx=80, pady=(20, 20))

        self.get_started_panel_text = tk.CTkLabel(self.get_started_panel, 
                                    text="Through this you can access to\na  do a new titration experiment", 
                                   font=("Times New Roman", 18,),   text_color=("black", "white"))
        self.get_started_panel_text.grid(row=1, column=0, padx=80, pady=(20, 70))

        self.get_started_button = tk.CTkButton(self.get_started_panel, text="Get Started",
                                               width=400, height=52, border_width=0,corner_radius=10, 
                                                font=("Times New Roman", 20,),
                                               text_color=("white", "#FFFFFF"),
                                               command=self.controller.open_start_tritration, 
                                            fg_color="#8F3C64")
        self.get_started_button.grid(row=2, column=0, padx=10, pady=(70,10))

        #---------------------------------------------------------------
        self.view_details_panel = tk.CTkFrame(self , 
                                            fg_color="#D7CFFF",
                                            width=400,
                                            height=300
                                            )
        self.view_details_panel.grid(row=1, column=1, padx=(20,90), pady=(80,20), sticky="nsew")



     
        self.view_details_panel_title = tk.CTkLabel(self.view_details_panel, text="View Previous Titration Details", 
                                 font=("Times New Roman", 26,),   text_color=("black", "white"))
        self.view_details_panel_title.grid(row=0, column=0, padx=20, pady=(20, 20))

        self.view_details_panel_text = tk.CTkLabel(self.view_details_panel, 
                                    text="Here You can see the Complete\na details of the tritrations you\na have already Done", 
                                   font=("Times New Roman", 18,),   text_color=("black", "white"))
        self.view_details_panel_text.grid(row=1, column=0, padx=80, pady=(20, 70))



        self.view_details_button = tk.CTkButton(self.view_details_panel, text="View Details",
                                               width=400, height=52, border_width=0,corner_radius=10, 
                                                font=("Times New Roman", 20,),
                                               text_color=("white", "#FFFFFF"),
                                                command=self.controller.open_history, 
                                            fg_color="#47397E")
        self.view_details_button.grid(row=2, column=0, padx=10, pady=(50,10))

   

