import speech_recognition as sr

# Create a recognizer instance
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Please say something:")
    audio = recognizer.listen(source)  # Listen for audio input

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
