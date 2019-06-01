import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        closeValue = get_close_matches(w, data.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if yes or N for no. " %closeValue)
        if yn == "Y":
            return data[closeValue]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter the word: ")

output = translate(word)

if type(output) == list:
    for (i, item) in enumerate(output, start=1):
        print(str(i) + ". " + item)
else:
    print(output)