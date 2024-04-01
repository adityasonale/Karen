
from karen_functions_v2.chatbotV2 import Karen
from karen_functions_v2.Listen import Listen
from karen_functions_v2.Response import Speak
from karen_functions_v2.Tasks import NonInputExecution,Battery_status
import threading


# def Main():
#     try:
#         listen = Listen()
#         ChatBot(listen)
#     except Exception as e:
#         print(e)
# while True:
#     Main()

# initialising classes

chatbot = Karen()

def Main():
    chatbot = Karen()
    while True:
        # try:
        listen = Listen()
        chatbot.ChatBot(listen)
        # except Exception as e:
        #     print(e)

thread1 = threading.Thread(target=Battery_status)

thread1.start()
Main()