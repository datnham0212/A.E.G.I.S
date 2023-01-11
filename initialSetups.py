import pyttsx3 as pt

engine = pt.init()

def run():
    aegis_voice()
    while True: 
        aegis_greet()
        engine.runAndWait()
        
        user_input = input("Type 'exit' to stop, or press Enter to continue: ")
        if user_input.lower() == 'exit':
            aegis_stop()
            break
            

def aegis_voice():    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    

def aegis_greet():
    import datetime
    now = datetime.datetime.now()
    hour = now.hour
    if hour in range(6, 12):
        temp = "Good Morning"
    elif hour in range(12, 19):
        temp = "Good Afternoon"
    elif hour in range(19, 24):
        temp = "Good Evening"

    engine.say(f"{temp} master Dat, how may I assist you?") if hour in range(6, 24) else engine.say("What concerns are you facing at this late hour, master Dat?")



def aegis_stop():
    engine.say(f"Very well sir.")
    engine.runAndWait()
    
    