from tkinter import ttk
import customtkinter as tk
from CTkMessagebox import CTkMessagebox
from PIL import ImageTk, Image
from modules.Session.session import UserSession
from modules.titration.titration import Titration


class History_Interface(tk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        
        self.titration_details = Titration()
        
        self.label = tk.CTkLabel(self, text="Titration History" , font=("Helvetica", 24, "bold"))
        self.label.grid(row=0, column=0, padx=60, pady=20)

    
        self.treeview_frame = tk.CTkFrame(self)
        self.treeview_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.treeview_frame.columnconfigure(0, weight=1)

      

        self.button_frame = tk.CTkFrame(self)
        self.button_frame.grid(row=2, column=0, padx=10, pady=20 )
       

        style = ttk.Style()
       # Configure the style for the Treeview rows
        style.configure("Custom.Treeview",
                        background="gray",
                        foreground="#ffffff",
                        fieldbackground="#333333",
                        rowheight=35,
                        theadbackground="blue",
                        theme="dark",
                        font=("Arial", 14))

        # Configure the style for the Treeview headings
        style.configure("Custom.Treeview.Heading",
                        background="blue",
                        foreground="black",
                        font=("Arial", 14, "bold"))


        self.treeview = ttk.Treeview(self.treeview_frame, columns=("Reaction","indicator", "analyte", "start_pred_class", "changed_pred_class", "volume"), 
                                     padding=10, show="headings" ,style="Custom.Treeview" )
        self.treeview.grid(row=0, column=0, padx=(10,60) , pady=10 , sticky="nsew" )

        #create headings for the treeview
        self.treeview.heading("Reaction", text="Reaction")
        self.treeview.column("Reaction", stretch=tk.YES, width=200) 
        self.treeview.heading("indicator", text="indicator")
        self.treeview.column("indicator", stretch=tk.YES, width=200) 
        self.treeview.heading("analyte", text="analyte")
        self.treeview.column("analyte", stretch=tk.YES, width=200) 
        self.treeview.heading("start_pred_class", text="start_pred_class")
        self.treeview.column("start_pred_class", stretch=tk.YES, width=200) 
        self.treeview.heading("changed_pred_class", text="changed_pred_class")
        self.treeview.column("changed_pred_class", stretch=tk.YES, width=200) 
        self.treeview.heading("volume", text="volume")
        self.treeview.column("volume", stretch=tk.YES, width=200)

        #create a scrollbar for the treeview
        scroll_style = ttk.Style()
        scroll_style.configure("Custom.Vertical.TScrollbar",
                gripcount=0,
                background="#333333",
                darkcolor="#666666",
                lightcolor="red",
                troughcolor="#333333",
                bordercolor="#333333")
        
        self.treeview_scrollbar = ttk.Scrollbar(self.treeview_frame, orient="vertical", command=self.treeview.yview , style="Custom.Vertical.TScrollbar")
        self.treeview_scrollbar.grid(row=0, column=1, sticky="ns")

        #configure the treeview scrollbar
     
        self.treeview.configure(yscrollcommand=self.treeview_scrollbar.set)

        #create a button  to refresh the treeview
        self.refresh_button = tk.CTkButton(self.button_frame, text="Refresh", command=self.load_module_data)
        self.refresh_button.grid(row=1, column=0, padx=10, pady=10)

        self.load_module_data()

    

    def load_module_data(self):
        #delete the data before loading
        self.treeview.delete(*self.treeview.get_children())
        #load the data from the database
        user_name = self.controller.user_session.get_user_name()
        print("user name is ", user_name)
        for row in self.titration_details.get_titrations(user_name):
            self.treeview.insert("", "end", values=row)
    
    

    #create a function to display the modules
    def display_modules(self):
     
        #create columns for the treeview
        self.treeview.column("Reaction", width=100)
        self.treeview.column("indicator", width=100)
        self.treeview.column("analyte", width=100)
        self.treeview.column("start_pred_class", width=100)
        self.treeview.column("changed_pred_class", width=100)
        self.treeview.column("volume", width=100)


        #add the treeview to the frame
        self.treeview.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

        #create a scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=7, column=4, sticky="NSE")

        #configure the treeview
        self.treeview.configure(yscrollcommand=self.scrollbar.set)

        #create a button to close the window
        self.close_button = tk.CTkButton(self.frame, text="Close", command=self.close_window)
        self.close_button.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

     










      




  