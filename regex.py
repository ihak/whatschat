import re


def find_all():
	# Open file
	f = open('chat.txt', 'r')
	# Feed the file text into findall(); it returns a list of all the found strings
	strings = re.findall(r'\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2} (?:(?:P|A)M) - ((?:\w+ )*\w+):', f.read())

	print("Total messages exchanged: ", len(strings))

	for string in strings:
		print(string)

def single_find():
	text = "9/13/16, 12:33 PM - Hanif Mianjee: <Media omitted>"
	match = re.search(r'^\d{1,2}/\d{1,2}/\d{1,2}, \d{1,2}:\d{2} ((P|A)M) - (\w+\s)*\w+:', text)
	if match:
		print("found: ", match.group())

find_all()