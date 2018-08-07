import json
from difflib import get_close_matches

data = json.load(open('data.json','r'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff = 0.8)) > 0:
        yn = input( 'Did you mean -> %s <- instead ? Press Y if yes , or press N : ' %get_close_matches(word,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word,data.keys(),cutoff = 0.8)[0]]
        elif yn == 'N':
            return ['No such word exist, please check it once again.']
        else :
            return ["we don't understand you ."]
    else:
        return ['Oops! you entered wrong word']

word = input('Enter the word :  ')

for item in translate(word):
    print (item)
