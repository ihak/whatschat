import re
from datetime import datetime

def find_all():
	# Open file
	f = open('chat.txt', 'r')
	# Feed the file text into findall(); it returns a list of all the found strings
	match = re.match(r'(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{2} (?:(?:P|A)M)) - ((?:\w+ )*\w+):', f.read())

	if match:
		print("match: ", match.group(3))

def single_find():
	text = "11/7/16, 11:09 PM - Hassan Ahmed Khan: <Meida Omitted>"
	match = re.match(r'(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2} (?:P|A)M) - ((?:\w+ )*\w+): (.+)', text)
	if match:
		print("found: ", match.group(3))

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

def date():
	date1 = "9/23/16, 11:45 PM"
	date2 = "9/24/16, 12:05 AM"

	fmt = "%m/%d/%y, %I:%M %p"
	time1 = datetime.strptime(date1, fmt)
	time2 = datetime.strptime(date2, fmt)
	diff = time2 - time1

	print("date: ", time1)
	print("date: ", time2)
	print("diff days: ", diff.days)
	print("diff seconds: ", diff.seconds)

date()
# single_find()