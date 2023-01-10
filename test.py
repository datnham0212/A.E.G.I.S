import pyttsx3 as pt

engine = pt.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 150)
engine.say("Good morning sir, how may I assist you?")
engine.runAndWait()

