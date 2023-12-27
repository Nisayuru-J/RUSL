import random
from tkinter import ttk
import customtkinter as tk
from CTkMessagebox import CTkMessagebox
from tkinter import PhotoImage
#from utils.utils import Utils



class LandingInterface(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.parent = parent
        self.controller = controller

        self.landingImage01 = PhotoImage(file="./assets/images/landing01.png")
        self.logoImage = PhotoImage(file="./assets/images/main.png")
        self.landingImage02 = PhotoImage(file="./assets/images/landing02.png")
        self.landingImage03 = PhotoImage(file="./assets/images/landing03.png")
     
 
        self.label = tk.CTkLabel(self, text="Automated Titration System" , 
                                 font=("Times New Roman", 48, "bold",),   text_color=("#b51863", "#b51863"))
        self.label.grid(row=0, column=0, padx=30, pady=(10, 10))

        #create a panel to store the summary data
        self.main_image_panel = tk.CTkFrame(self , 
                                            fg_color="transparent"
                                            )
        self.main_image_panel.grid(row=2, column=0, padx=(90,20), pady=10, sticky="nsew")

        self.landingImage01 = tk.CTkLabel(self.main_image_panel, image=self.landingImage01, height=250, width=450 , text="", font=("Helvetica", 24, "bold"))
        self.landingImage01.grid(row=0, column=0, padx=30, pady=10)

        #pannel to keep the buttons
        self.btns_pannel = tk.CTkFrame(self , fg_color="transparent")
        self.btns_pannel.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")


        self.get_started_btn = tk.CTkButton(self.btns_pannel, text="Get Started",
                                               font=("Times New Roman", 25,),
                                               text_color=("white", "#FFFFFF"),
                                               width=160, height=60, border_width=0,corner_radius=10, 
                                               compound="left",
                                               command=self.controller.open_login,
                                              fg_color="#b51863")
        self.get_started_btn.grid(row=0, column=0, padx=(20,20), pady=(100,10))

        self.view_more_btn = tk.CTkButton(self.btns_pannel, text="View More",
                                               font=("Times New Roman", 25,),
                                               text_color=("white", "#FFFFFF"),
                                               width=160, height=60, border_width=0,corner_radius=10, 
                                               compound="left",
                                              #command=self.open_users,
                                              fg_color="#170b45")
        self.view_more_btn.grid(row=1, column=0, padx=(20,20), pady=(20,10))

        #pannel to store round images
        self.round_images_pannel01 = tk.CTkFrame(self , 
                                               fg_color="transparent"
                                               )
        self.round_images_pannel01.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

        self.round_images_pannel02 = tk.CTkFrame(self , 
                                               fg_color="transparent"
                                               )
        self.round_images_pannel02.grid(row=2, column=2, padx=10, pady=20, sticky="nsew")

        #makeing an image round
        self.round_image01 = tk.CTkLabel(self.round_images_pannel01, 
                                         image=self.landingImage02, height=150, width=150 ,
                                           text="")
        self.round_image01.grid(row=0, column=0, padx=20, pady=20)

        self.round_image02 = tk.CTkLabel(self.round_images_pannel02, 
                                         image=self.landingImage03, height=150, width=150 ,
                                           text="")
        self.round_image02.grid(row=0, column=0, padx=20, pady=20)




       
        

     
       
    

    

     
        
     

      

        

        
        

       