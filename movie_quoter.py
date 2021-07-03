#1 python3
#movie_quoter.py is a movie quoting command line program

QUOTES = {
    'Star Wars' : "May the Force be with you.",
    'The Wizard Of Oz' : "There's no place like home.",
    'Titanic' : "I'm the king of the world.",
    'The Terminator' : "I'll be back.",
    'Jaws' : "You're going to need a bigger boat.",
    }

import sys, pyperclip

#This throws a message if an argument is not given after the file name.
if len(sys.argv) < 2:
    print("Usage: python3 movie_quoter.py [Keyphrase] - copies phrase to clipboard.")
    sys.exit()


#This grabs any number of arguments after the file name and stores them as an array.
cmd_args = sys.argv[1:len(sys.argv)]

#This takes the arguments given from their list and converts them into a string to search
#the dictionary of movies.
keyphrase = " ".join(cmd_args).title()

if keyphrase in QUOTES:
    pyperclip.copy(QUOTES[keyphrase])
    print("Quote from " + keyphrase + " has been copied to the clipboard.")
else:
    print("This movie is not in our database yet.")