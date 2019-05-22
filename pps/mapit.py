#!python3
# opens the place you typed in on google map

import webbrowser,sys
# import pyperclip

if len(sys.argv)>1:
    #Get address from command line
    address = ' '.join(sys.argv[1:])
# else:
#     address = pyperclip.paste()
webbrowser.open('www.google.com/maps/place/'+address)


