import datetime
from karen_functions_v2.Response import Speak
import webbrowser
import time
import psutil
import cv2


def Time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    Speak(f"Sir, the time is {strTime}")
    # print(f"Sir, the time is {strTime}")

def Date():
    date = datetime.date.today()
    # Speak(f"Its {date}")
    Speak(f"{date}")

def Google():
    webbrowser.open("google.com")

def Youtube():
    # Speak("Opening YouTube...")
    webbrowser.open("www.youtube.com")

def StackOverflow():
    # Speak("Opening Stackoverflow...")
    webbrowser.open("stackoverflow.com")

def Bye():
    time.sleep(2)
    exit()

def BatteryLevel():


    battery = psutil.sensors_battery()
    sec_left = battery.secsleft
    time_left = datetime.timedelta(seconds=sec_left)
    time_obj = str(time_left)
    time_obj = time_obj[8:]

    Speak(f"current Battery percentage is {battery.percent}")

    # print("Battery left : ", convertTime(battery.secsleft))

    Speak(f"Battery left for {time_obj[:2]} hours and {time_obj[3:5]} minutes")

    if battery.percent <= 33 and battery.power_plugged == False:
        # print("Requesting you to please plug in")
        Speak("Requesting you to please plug in")
    else:
        # print("Power is Plugged In")
        Speak("Power is Plugged In")


def activate_gesture_recognition():
    print(f"gesture recognition activated")
    with open(r"D:\vs code\python\DeepLearning\Projects\Karen\v2\external functions\gesture.py", "r") as file:
        script = file.read()
    exec(script)
    
def deactivate_gesture_recognition():
    print(f"gesture recognition deactivated")


#-----------------------------------------------------------------------------------------------------

def Battery_status():
    while True:
        battery = psutil.sensors_battery()
        if battery.percent <=33 and battery.power_plugged == False:
            Speak("Sir your battery is below 33 percent")
            Speak("Requesting you to please plug in")
        time.sleep(900)
#-----------------------------------------------------------------------------------------------------

def NonInputExecution(query):
    if 'date' in query:
        Date()

    elif 'time' in query:
        Time()

    elif 'google' in query:
        Google()

    elif 'youtube' in query:
        Youtube()
    elif 'stackoverflow' in query:
        StackOverflow()

    elif 'chatbot_goodbye' in query:
        Bye()

    elif 'battery_level' in query:
        BatteryLevel()

    elif 'gesture_recognition_deactivation' in query:
        deactivate_gesture_recognition()
    
    elif 'gesture_recognition_activation' in query:
        activate_gesture_recognition()