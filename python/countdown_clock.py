from sys import exit
from time import sleep
from datetime import datetime
from datetime import timedelta

def not_in_past(current, alarm):
    time_remaining = alarm - current
    if time_remaining.days < 0:
        return False
    else:
        return True
    
def count_down(current, alarm):
    time_remaining = alarm - current
    days, seconds = time_remaining.days, time_remaining.seconds

    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    if seconds <= 0 or time_remaining.days < 0:
        print("BEEP BEEP! BEEP BEEP!\nIt is now {}".format(alarm))
        exit()
    else: 
        print("{} {} {} {} remaining".format(str(days) + " days" if days > 0 else "", str(hours) + " hours" if hours > 0 else "", str(minutes) + " minutes" if minutes > 0 else "", str(seconds) + " seconds" if seconds > 0 else ""))
    
current = datetime.now()
alarm = datetime(1984,8,27)

while not_in_past(current, alarm) == False:
    year, month, day = input("Enter the date for your alarm >> [YYYY-MM-DD] ").split("-")
    alarm = datetime(int(year), int(month), int(day))
    
    hour, minute = input("Enter the time for your alarm >> [16:34] ").split(":")
    alarm = datetime(int(year), int(month), int(day), int(hour), int(minute), 1)

alarm = datetime(int(year), int(month), int(day), int(hour), int(minute))      
    
while True:
    count_down(datetime.now(), alarm)
    sleep(1)
