from datetime import datetime, timedelta
import serial
import time
#create a python class that contains the utility functions
class Utils:
    def __init__(self):
        self.name = "utils"
        self.camera_01_ip ="http://192.168.43.90:8080/video"
        self.camera_02_ip ="http://192.168..100:8080/video"
    
    def calculate_hours(self, start_time, end_time):
        start = datetime.strptime(start_time, '%H.%M')
        end = datetime.strptime(end_time, '%H.%M')
        duration = end - start
        hours = duration.total_seconds() / 3600
        return hours
    
    def send_data_to_arduino(self, arduino_port, baud_rate , status_data):
        try:
            arduino = serial.Serial(arduino_port, baud_rate)
        except serial.SerialException:
            print(f"Failed to connect to {arduino_port}. Make sure the Arduino is connected.")
            return

        try:
            start_time = time.time()
            while True:
                data_to_send = status_data
                if data_to_send.lower() == 'exit':
                    break
                arduino.write(data_to_send.encode())
                arduino.flush()

                # Wait for a response from Arduino for a maximum of 5 seconds
                response = arduino.readline().decode().strip()
                print(f"Arduino says: {response}")

                if time.time() - start_time >= 5:  # Adjust the timeout value as needed
                    print("Timeout: Arduino did not respond.")
                    break
        except KeyboardInterrupt:
            pass  # Handle Ctrl+C to gracefully exit
            arduino.close()
            
            
    