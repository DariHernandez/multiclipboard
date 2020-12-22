#! python3
# Saves and loads pices of text to the clipboard

import shelve, pyperclip, sys, os

helpMenssage = """Saves and loads pices of text to the clipboard
Usage: 
main.py save <keyword> - Saves clipboard to keyword
main.py <keyword> - Loads keyword to clipboard
main.py list - Loads all keywords to clipboard
main.py del <keyword> - Delete specific keyword
main.py del - Delete all keywords
"""

path = os.path.dirname (__file__)
mcbShelf = shelve.open(os.path.join(path, 'clipboard'))

#Save clipboard content
if len(sys.argv) == 3: 
    if sys.argv[1].lower() == 'save':                   #Save keyword
        print ('keyword %s saved' % (sys.argv[2]))
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'del':               #Delete keyword
        print ('keyword %s deleted' % (sys.argv[2]))
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2: 
    #List keywords and load content
    if sys.argv[1].lower() == 'list':                   #Show list of keywords
        print ('--- list of keywords ---')
        for keyword in list(mcbShelf.keys()): 
            print (keyword)
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'del':               #Delete all keywords
        print ('All keywords delated')
        for item in mcbShelf.keys():
            del mcbShelf[item]
        pyperclip.copy('')
    elif sys.argv[1] in mcbShelf:                       #Copy keyword
        print ('Text for the keyword %s copied' % (sys.argv[1]))
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else: 
        print (helpMenssage)
        sys.exit()

mcbShelf.close()

