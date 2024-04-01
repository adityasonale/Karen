import speech_recognition as sr

def Listen():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognize.pause_threshold = 1
        recognize.energy_threshold = 1000
        audio = recognize.listen(source)

    try:
        print("Recognizing...")
        query = recognize.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query