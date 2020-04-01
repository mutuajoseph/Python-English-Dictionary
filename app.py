import json
from difflib import get_close_matches

data = json.load(open("meanings.json"))

# print(data)

def translate(word):

    word = word.lower()

    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:

        confirmation = input("Did you mean %s instead? Enter y if yes or n if no: " % get_close_matches(word, data.keys())[0]) 

        if confirmation == 'y':
            return data[get_close_matches(word, data.keys())[0]]

        elif confirmation == 'n':
            return "The word entered does not exist! Please double check your entry"

        else:
            return "I cant understand your query"

    else:
        return ("Word doesn't exist")

word = input('Enter word: ')

word_meaning = translate(word)

if type(word_meaning) == 'list':
    for item in word_meaning:
        print (word_meaning)
else:
    print(word_meaning)
