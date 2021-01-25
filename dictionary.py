import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input( "Did you mean %s instead? Enter y or n:" %get_close_matches(word,data.keys())[0])
        if yn=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="n": 
            return "Word not found"
        else:
            return "U dumb"    
    else:
        return "Word not found"


word=input("Enter word: ")
out=translate(word)
if type(out)==list:
    for i in out:
        print(i)

else:
    print(out)
