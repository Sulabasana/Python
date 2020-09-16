import json
from difflib import get_close_matches
#compares words
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "Sorry the worde does not exist. Please check it"

word = input("Enter word: ")

print(translate(word))