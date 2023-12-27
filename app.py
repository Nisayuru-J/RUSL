# Sample usage in app.py
from modules.Home.HomeInterface import HomeInterface
from modules.Landing.LandingInterface import LandingInterface
from modules.Landing.LoginInterface import LoginInterface
from modules.history.historyInterface import History_Interface

from modules.titration.start_tritration_interface import Start_tritration_interface
import tkinter as tk
import customtkinter as ctk
from tkinter import font as tkfont
from tkinter import *
from CTkMessagebox import CTkMessagebox
from modules.Session.session import UserSession
from modules.user_accounts.user_accounts_interface import UserAccountInterface


class SampleApp(ctk.CTk):    
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        #keep whether the user is logged in or not
        self.logged_in = False
        self.user_session = UserSession()
        
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.mainImage = PhotoImage(file="./assets/images/main.png")
        self.homeIcon = PhotoImage(file="./assets/icons/home.png")
        self.servicesIcon = PhotoImage(file="./assets/icons/service.png")
        self.projectsIcon = PhotoImage(file="./assets/icons/projects.png")
        self.contactIcon = PhotoImage(file="./assets/icons/contact.png")
        self.logoutIcon = PhotoImage(file="./assets/icons/logout.png")
        self.loginIcon = PhotoImage(file="./assets/icons/login.png")

        self.leftPanel = ctk.CTkFrame(self,fg_color="white")
        self.leftPanel.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.leftPanel.columnconfigure(0, weight=2)
        
        self.container = ctk.CTkFrame(self , fg_color="white")
        self.container.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.container.columnconfigure(0, weight=2)

        

        #create a image label
        self.image_label = ctk.CTkButton(self.leftPanel, image=self.mainImage, height=150, width=150 ,
                                        command=self.open_landing_page,
                                        fg_color="transparent",
                                        bg_color="transparent",
                                        hover_color="#ffd4e8",
                                         text="", font=("Helvetica", 24, "bold"))
        self.image_label.grid(row=0, column=0, padx=20, pady=20)

        #create a label to show the app name
        # self.label = ctk.CTkLabel(self.leftPanel, text="Main Panel" , font=("Times New Roman", 24, "bold"))
        # self.label.grid(row=1, column=0, padx=20, pady=(3, 10))


   
        self.user_manage_button = ctk.CTkButton(self.leftPanel, text="  Home",
                                         font=("Times New Roman", 24, "bold"),
                                         width=200, height=52, border_width=0, corner_radius=10,
                                         image=self.homeIcon, compound="left",
                                         command=self.open_home,
                                         fg_color="#170b45", anchor="w")
                                         
        self.user_manage_button.grid(row=4, column=0, padx=20, pady=(10))

        self.services_button = ctk.CTkButton(self.leftPanel, text=" Titration",
                                                font=("Times New Roman", 24, "bold"),
                                               width=200, height=52, border_width=0,corner_radius=10, 
                                              command=self.open_start_tritration,
                                              image=self.servicesIcon, compound="left",
                                              fg_color="#170b45", anchor="w")
        self.services_button.grid(row=5, column=0, padx=20, pady=10)

        self.projects_button = ctk.CTkButton(self.leftPanel, text="  Projects",
                                            font=("Times New Roman", 24, "bold"),
                                               width=200, height=52, border_width=0,corner_radius=10, 
                                              #command=self.open_lectures,
                                              image=self.projectsIcon, compound="left",
                                              fg_color="#170b45" , anchor="w")
        self.projects_button.grid(row=6, column=0, padx=20, pady=10)

        self.contact_button = ctk.CTkButton(self.leftPanel, text="Contact Us",
                                                 font=("Times New Roman", 24, "bold"),
                                               width=200, height=52, border_width=0,corner_radius=10, 
                                              #command=self.open_lectures,
                                              image=self.contactIcon, compound="left",
                                              fg_color="#170b45" , anchor="w")
        self.contact_button.grid(row=7, column=0, padx=20, pady=10)

        self.logout_button = ctk.CTkButton(self.leftPanel, text="Logout",
                                             font=("Times New Roman", 24, "bold"),
                                               width=200, height=52, border_width=0,corner_radius=10, 
                                              command=self.logout_user,
                                              image=self.logoutIcon, compound="left",
                                                fg_color="#170b45" , anchor="w")
        self.logout_button.grid(row=8, column=0, padx=20, pady=10)

        self.id = tk.StringVar()
        self.id.set("001")


        self.listing = {}
        for F in (LandingInterface , LoginInterface, HomeInterface, Start_tritration_interface, UserAccountInterface, History_Interface ):
            page_name = F.__name__
            print('PAGE NAME --------->',page_name)
            frame = F(parent=self.container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.listing[page_name] = frame

        self.show_frame("LandingInterface") #chenge this to welcomepage later

    def set_login(self, value):
        self.logged_in = value

   
    


    def logout_user(self):
        #display the login page if the user is not logged in
        if self.logged_in:
            self.set_login(False)
            self.show_frame("HomeInterface")
            
            self.user_session.logout_user()
        else:
            #display a message box to the user -  Only the Admins can manage the Users
            CTkMessagebox(title="Error", message="You are not logged in")
  
    def open_home(self):
        self.show_frame("HomeInterface")
    
    def open_register(self , event):
        self.show_frame("UserAccountInterface")

    def open_users(self):
        self.show_frame("UserAccountInterface")
          
    def open_start_tritration(self):
        self.show_frame("Start_tritration_interface")

    def open_landing_page(self):
        self.show_frame("LandingInterface")

    def open_login(self):
        self.show_frame("LoginInterface")
    
    def open_history(self):
        self.show_frame("History_Interface")
        hs = History_Interface(parent=self.container, controller=self)
        hs.load_module_data()
        
    
    def show_frame(self, page_name):
        print(page_name)
        page = self.listing[page_name]
        page.tkraise()
        

if __name__ == "__main__":
    #ctk.set_appearance_mode("Dark")
    app = SampleApp()
    app.mainloop()

