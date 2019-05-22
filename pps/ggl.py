#!python3
# ggl- a script that google searches the arg i give

import webbrowser,sys

if len(sys.argv)>1:
    search = ' '.join(sys.argv[1:])
    webbrowser.open("https://www.google.com/search?q="+ search)
