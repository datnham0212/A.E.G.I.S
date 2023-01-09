import pyttsx3 as pt

engine = pt.init()

def run():
    aegis_voice()
    aegis_greet()
    engine.runAndWait()

def aegis_voice():    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    
def aegis_greet():
    engine.say(f"{getPartOfDay()} master Dat, how may I assist you?")

def getPartOfDay():
    import datetime
    now = datetime.datetime.now()
    hour = now.hour
    if hour < 12:
        return "Good Morning"
    elif hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

