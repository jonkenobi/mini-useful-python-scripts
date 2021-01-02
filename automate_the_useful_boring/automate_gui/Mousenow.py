# ! python3
# Mousenow.py -- shows the current coordinates for the mouse cursor
import pyautogui, time

# setup
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1
# print("My screen size is ", pyautogui.size())
# width, height = pyautogui.size()

print("Press ctrl-c to quit.")



x, y = pyautogui.position()
# try:
#     for i in range(10):
positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
print(positionStr, end = ' ')
print("\b"*len(EpositionStr), end = '', flush = True )
# except KeyboardInterrupt:
#     print('\ndone')