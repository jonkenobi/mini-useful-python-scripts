# !python3
#stopwatch.py -- A simple stopwatch program

import time

#Display the program's instructions
print('''Press ENTER to begin. Afterward, press ENTER to "click" on the stopwatch.
      press ctrl + c to quit. ''')
input()
print('Started')
startTime = time.time()
lastTime = startTime
numlaps = 1

#loop and exit with ctrl+ c
try:
    while True:
            input()
            
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time()-startTime,2)
            print( 'Lap #{}, Total Time {} secs,  Lap Time {} secs'.format(numlaps, totalTime, lapTime, end =''))
            numlaps += 1
            lastTime = time.time()
except KeyboardInterrupt:
    # handle the ctrl+c exception
    print('\ndone')
    
