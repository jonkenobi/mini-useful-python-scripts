# ! python 3
#mcb.pyw --saves and loads pieces of texts to clipboard
    #-- somewhat like saving things into a dictionary, with keys corresponding to  text,
    # but saving into a shelf object instead
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#         py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbshelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv)== 2:
    #List keywords and load content
    if sys.argv[1] == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])
mcbshelf.close()




