import json
from difflib import SequenceMatcher, get_close_matches
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word];
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]

    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        temp=get_close_matches(word,data.keys())[0]
        print("your word doesn't exist, do you mean "+temp)
        print("if yes type y else n")
        ans=input()
        if(ans=='y'):
            return data[temp]
        elif(ans=='n'):
            return "word doesn't exist"
        else:
            return "sorry we don't understand what you want to search, please double check it"
    else:
        return "sorry we don't understand what you want to search, please double check it"


word=input("enter word:")
result=translate(word)

if(type(result)==list):
    for i in result:
        print(i)
else:
    print(result)
