# This will create the UI elements of the Home screen
import customtkinter as tk
from tkinter import PhotoImage, ttk
from CTkMessagebox import CTkMessagebox

from utils.sample import Titrator
from modules.experiments.experiments import Experiment
from modules.titration.titration import Titration

from modules.user_accounts.user_account import UserAccount
from modules.Session.session import UserSession
#from utils.handle_titration import open_mobile_camera
import tensorflow as tf
import tensorflow_hub as hub
import cv2
import time
import numpy as np

from utils.utils import Utils


class Start_tritration_interface(tk.CTkFrame):

    def __init__(self, parent, controller):
        
        tk.CTkFrame.__init__(self, parent, fg_color="white")
        self.parent = parent
        self.experiment = Experiment()
        
        self.titration = Titration()
        
        self.titrator = Titrator()
        print("************")
        self.parent = parent
        self.controller = controller
        print("Image issue")
        self.bg_image = PhotoImage(file="./assets/images/get_started_main.png")
        self.captured_frame = None
        #self.user_session = UserSession()
        # self.current_session = UserSession()
        self.utils =Utils()
        self.titraion_details = None
        print("Loading model")
        self.model = tf.keras.models.load_model('./models/resnet_color_model.h5',custom_objects={'KerasLayer':hub.KerasLayer})
        print("Model Loaded Successfully")

        self.bg_image = tk.CTkLabel(
            self, image=self.bg_image, height=600, width=450, text="", font=("Helvetica", 24, "bold"))
        self.bg_image.grid(row=0, column=0, padx=40, pady=40)

        # create a panel to keep the form
        self.form_panel = tk.CTkFrame(self, fg_color="white")
        self.form_panel.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.reaction_text = tk.CTkLabel(self.form_panel,
                                         text="Select the Reaction Type",
                                         font=("Times New Roman", 18,),   text_color=("black", "white"))
        self.reaction_text.grid(row=0, column=0, padx=10,
                                pady=(10, 4), sticky="w")

        self.current_reaction = tk.StringVar()
        self.reaction_combobox = tk.CTkComboBox(self.form_panel,
                                                width=450,
                                                height=30,
                                                font=("Times New Roman", 22,),
                                                corner_radius=10,
                                                values=[""],
                                                variable=self.current_reaction
                                                )
        self.reaction_combobox.grid(
            row=1, column=0, padx=5, pady=10, sticky="w")
        self.reaction_combobox.configure(
            values=self.experiment.get_reactions() or ['OTHER'])
        self.current_reaction.trace_add('write', self.load_indicators)

        self.indicator_text = tk.CTkLabel(self.form_panel,
                                          text="Select the Indicator",
                                          font=("Times New Roman", 18,),   text_color=("black", "white"))
        self.indicator_text.grid(
            row=2, column=0, padx=5, pady=(10, 5), sticky="w")
        self.current_indicator = tk.StringVar()
        self.indicator_combobox = tk.CTkComboBox(self.form_panel,
                                                 width=450,
                                                 height=30,
                                                 font=("Times New Roman", 22,),
                                                 corner_radius=10,
                                                 values=[""],
                                                 variable=self.current_indicator
                                                 )
        self.indicator_combobox.grid(
            row=3, column=0, padx=5, pady=10, sticky="w")
        self.current_indicator.trace_add('write', self.load_analytes)

        self.current_analyte = tk.StringVar()
        self.analyte_combobox = tk.CTkComboBox(self.form_panel,
                                                 width=200,
                                                 height=30,
                                                 font=("Times New Roman", 22,),
                                                 corner_radius=10,
                                                 values=[""],
                                                 variable=self.current_analyte
                                                 )
        self.analyte_combobox.grid(
            row=4, column=0, padx=5, pady=10, sticky="w")

        self.description_panel = tk.CTkFrame(self.form_panel,
                                             fg_color="#FFBEDE",
                                             width=400,
                                             height=100
                                             )
        self.description_panel.grid(row=5, column=0, padx=(
            10, 10), pady=(40, 30), sticky="nsew")

        self.start_button = tk.CTkButton(self.form_panel, text="Start",
                                         width=450, height=52, border_width=0, corner_radius=10,
                                         font=("Times New Roman", 20,),
                                         text_color=("white", "#FFFFFF"),
                                         command=self.navigate_to_tit_process,
                                         fg_color="#4E11A8")
        self.start_button.grid(row=6, column=0, padx=10, pady=(30, 10))

    def navigate_to_tit_process(self):
        reaction = self.reaction_combobox.get()
        indicator = self.indicator_combobox.get()
        analyte = self.analyte_combobox.get()
        
        self.controller.user_session.set_current_titration(reaction, indicator, analyte)
        self.open_mobile_camera()

    def load_indicators(self, *args):
        selected_reaction = self.reaction_combobox.get()
        print("Selected Reaction:", selected_reaction)
        self.indicator_combobox.configure(
            values=self.experiment.get_indicators(selected_reaction) or ['OTHER'])

    def load_analytes(self, *args):
        selected_reaction = self.reaction_combobox.get()
        selected_indicator = self.indicator_combobox.get()
        print("Selected Reaction:", selected_reaction)
        print("Selected Indicator:", selected_indicator)
        self.analyte_combobox.configure(
            values=self.experiment.get_analyte(selected_reaction, selected_indicator) or ['OTHER'])
        

    def preprocess_image(self, image):
        image = cv2.resize(image, (224, 224)) 
        image = image / 255.0 
        return image
    

    def predict_with_model(self, image):
        preprocessed_image = self.preprocess_image(image)
        predictions = self.model.predict(np.expand_dims(preprocessed_image, axis=0))
        predicted_class = np.argmax(predictions[0])

        return predicted_class


    def open_mobile_camera(self,  window_width=640, window_height=480, capture_interval=5):
            camera_url=self.utils.camera_01_ip
            camera2_url=self.utils.camera_02_ip
            
            cap = cv2.VideoCapture(camera_url) #camera 01
            cap2 = cv2.VideoCapture(camera2_url) #camera 02
            print("-------> Opened Both Cameras-------") 
            last_capture_time = time.time()

            #Sending the Initial Data to Aurdino
            self.utils.send_data_to_arduino('COM4', 9600, 0)

            # Capture the initial predicted class
            initial_predicted_class = None
            while initial_predicted_class is None:
                ret, frame = cap.read()
                ret2, frame2 = cap2.read()
                if not ret:
                    break
                initial_predicted_class = self.predict_with_model(frame)

            while True:
                # print("loop started")
                ret, frame = cap.read()
                ret2, frame2 = cap2.read()
                if not ret:
                    break
                if not ret2:
                    break

                frame = cv2.resize(frame, (window_width, window_height))
                frame2 = cv2.resize(frame2, (window_width, window_height))
                print("start")

                cv2.imshow('Mobile Camera', frame)
                cv2.imshow('Web  Camera', frame2)
                print("end")

                # Capture an image every capture_interval seconds
                if time.time() - last_capture_time >= capture_interval:
                    timestamp = int(time.time())

                    # Perform prediction on the captured image
                    predicted_class = self.predict_with_model(frame)
                    self.captured_frame = frame2
                    print(f'Predicted Class: {predicted_class}')

                    # Check if the predicted class has changed
                    if predicted_class != initial_predicted_class:
                        print("predict class {} changed to {}".format(initial_predicted_class, predicted_class) )
                        end_time = time.time()
                        titration_dic = self.controller.user_session.get_current_titrations()
                        titration_dic['start_time'] = last_capture_time
                        titration_dic['end_time'] = end_time
                        titration_dic['start_pred_class'] = initial_predicted_class
                        titration_dic['changed_pred_class'] = predicted_class

    
                        self.titraion_details = titration_dic
                        self.store_titration_details()
                        break

                    last_capture_time = time.time()

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cap2.release()
            cv2.destroyAllWindows()

    def store_titration_details(self):
        #sending data to aurdino board
        self.utils.send_data_to_arduino('COM4', 9600, 1)

        #getting the burate readings
        volume, area = self.titrator.get_burette_readings(self.captured_frame)

        user_data = self.controller.user_session.get_current_user()
        print(user_data)
        #adding user data to titration dic
        self.titraion_details['user_id'] = user_data['user_id']
        self.titraion_details['user_name'] = user_data['username']
        self.titraion_details['volume'] = volume
        self.titraion_details['area'] = area
        summary_text = "Reaction --> "+self.titraion_details['reaction']+"\n"+"Indicator --> "
        +self.titraion_details['indicator']+"\n"+"Analyte --> "
        +self.titraion_details['analyte']+"\n"+"Start Pred Class --> "
        +str(self.titraion_details['start_pred_class'])+"\n"
        +"Changed Pred Class --> "+str(self.titraion_details['changed_pred_class'])
        +"\n"+"Volume --> "+str(self.titraion_details['volume'])+"\n"

        CTkMessagebox(title="Titration Summary", message=summary_text, icon="info")


        # print("titration details", self.titraion_details)
        self.titration.add(self.titraion_details)
        


