# pip install pyautogui
import time
import pyautogui

'''
Automates mouse movement. 
Moves mouse to (1000, 400) and moves down 400 pixels, every 5 seconds
'''

while True:
    pyautogui.moveTo(1000, 200)
    pyautogui.moveRel(0, 400)  # move mouse 400 pixels down
    time.sleep(5)

    # pyautogui.click(100, 100)

    # pyautogui.dragTo(100, 150)
    # pyautogui.dragRel(0, 100)  # drag mouse 10 pixels down
