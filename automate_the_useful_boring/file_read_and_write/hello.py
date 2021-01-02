import time
print("hello pycharm")
bacon = open('bacon.txt','a')
print('opening...')
bacon.write(str(time.time())+'\n')
bacon.close()

bacon = open('bacon.txt')
b = bacon.read()
bacon.close()
print(b)