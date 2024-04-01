import time
import psutil
import datetime

battery = psutil.sensors_battery()
sec_left = battery.secsleft
time_left = datetime.timedelta(seconds=sec_left)
time_obj = str(time_left)
time_obj = time_obj[8:]
print(time_obj[:2],time_obj[3:5])