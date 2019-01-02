#AUTHOR: Stephen Blaney

import json
from difflib import get_close_matches

data = json.load(open("Teaching/data.json"))
#creating our data object and reading in our json data

def translate(w): #creating our translate function thta takes word as a local parameter
    w = w.lower() #converting all letters inputted by user to lowercase
    if w in data:
        return data[w] #return our data with whatever word was inputted

    elif len(get_close_matches(w, data.keys())) > 0:
        yn =  input("Did you mean %s instead? Enter Y if Yes or N if no " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data [get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Sorry we don't know what you mean please double check"
        else:
            return "Sorry please enter Y or N"
    else:
        return "The word you entered is not in the dictionary."

word = input("Enter Word: ") #prompt the user to enter a word word is a global variable

output = translate(word)  #printing our translate fuction to the Command line#

if type(output) == list:
    for item in output:
    print(item)
else:
    print(output)
