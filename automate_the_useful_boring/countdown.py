# !python3
#  countdown.py --  A simple countdown script that opens a file(.mp3) here at the end

import time, subprocess

timeleft = 30
while timeleft > 0:
    print(timeleft, end = '')
    time.sleep(1)
    timeleft  -= 1

# At end of  countdown, play sound
subprocess.Popen(['start','背叛.mp3'], shell = True)
