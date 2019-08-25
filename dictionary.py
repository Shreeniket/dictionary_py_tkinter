import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
	if(w[0].isupper()):
		pass
	else:
		toCheck = get_close_matches(w,data.keys())[0]

		if(toCheck[0].isupper()):
			return(data[toCheck])
		else:
			w = w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys())) > 0:
		print("Did you mean %s instead?" % get_close_matches(w, data.keys())[0])
		answer = input("Enter y for yes and anything else for no:")
		if answer == 'y':
			word = get_close_matches(w, data.keys())[0]
			return(data[word])
		else:
			return "Sorry, then the word on your mind does not exist in this dictionary."
	else:
		return "The word doesn't exist. Please double check"

word = input("Enter word:")
result = translate(word)

if type(result) is list:
	for i in range(len(result)):
		print("\nMeaning %s:" % str(i+1))
		print("==========")
		print(result[i])
else:
	print(result)
