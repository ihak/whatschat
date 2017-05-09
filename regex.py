import re


def find_all():
	# Open file
	f = open('chat.txt', 'r')
	# Feed the file text into findall(); it returns a list of all the found strings
	match = re.match(r'\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2} (?:(?:P|A)M) - (?:\w+ )*\w+:', f.read())

	if match:
		print("match: ", match.group(0))

def single_find():
	text = "9/13/16, 12:33 PM - Hanif Mianjee: <Media omitted>"
	match = re.match(r'^\d{1,2}/\d{1,2}/\d{1,2}, \d{1,2}:\d{2} (?:(?:P|A)M) - (?:\w+\s)*\w+:', text)
	if match:
		print("found: ", match.group(1))

def capture():
	text = "aircraft and jet"
	matches = re.findall(r'\b(air(?:craft|plane)|jet)\b', text)

	for string in matches:
		print(string)

def match():
	text = "fruit=apple \n color=blue"
	# match = re.search(r'[ \t]*(\w+)[ \t]*=[ \t]*(.+)', text)
	match = re.search(r'\w+=.+', text)
	if match:
		print("found: ", match.group(1))	

# single_find()
find_all()
# match()