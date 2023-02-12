# You must have these two modules in order for the script to run
import pyautogui
import time

# You can turn of the speed var by changing it into a comment
# If you want the speed var on,then dont change it to a comment
speed = 0.25
# You can change the (#) to what ever number you like.
# This determines when the script will start typing after excuting the script.
time.sleep(3)
# Create whatever txt file you want and make sure its in the same directory as the script.py
for line in open("", encoding= "utf-8"):
 
    pyautogui.typewrite(line, speed)
    # Once you execute the script you will have to then press "enter" for the script to completely run.
    # You can change the "enter" to whatever key you want. eg: "b"
    pyautogui.press("enter")
