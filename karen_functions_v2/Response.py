import pyttsx3

def Speak(audio):
    engine  = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    print(audio)
    engine.say(audio)
    engine.runAndWait()