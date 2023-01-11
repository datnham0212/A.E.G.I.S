import pyttsx3 as pt
import handling_date_time as dt
import datetime

class Aegis:
    def __init__(self):
        self.engine = pt.init()
        self.aegis_voice()
        self.aegis_greet()


    def run(self):
        while True: 
            user_input = input().strip().lower()
            if user_input == 'exit':
                self.aegis_stop()
                break

            if user_input.lower() == 'today':
                # print(dt.getCurrentDate())
                self.handle_date_request()
                

    def aegis_voice(self):    
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 150)
        

    def aegis_greet(self):
        now = datetime.datetime.now()
        hour = now.hour
        if hour in range(6, 12):
            temp = "Good Morning"
        elif hour in range(12, 19):
            temp = "Good Afternoon"
        elif hour in range(19, 24):
            temp = "Good Evening"

        self.engine.say(f"{temp} master Dat, how may I assist you?") if hour in range(6, 24) else self.engine.say("What concerns are you facing at this late hour, master Dat?")
        self.engine.runAndWait()

    def handle_date_request(self):
        self.engine.say(dt.getFullDateMessage())
        self.engine.runAndWait()


    def aegis_stop(self):
        self.engine.say(f"Very well sir.")
        self.engine.runAndWait()
    
    