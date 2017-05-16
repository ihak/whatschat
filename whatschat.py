#!/usr/bin/env python3
""" 
This is a simple WhatsApp chat analysis tool that takes WhatsApp chat text file
as an input and displays useful information like 
1. number of messages exchanged
2. Number of days messages extend to
3. Total time spend messaging etc
"""

from sys import argv, exit
import re
from User import User
from Message import Message
from datetime import datetime

# if len(argv) < 2:
# 	print("usage: ", argv[0], " <txt>")
# 	exit()

users = []
messages = []

while True:
	try:
		line = raw_input()
		
		match = re.match(r'(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2} (?:P|A)M) - ((?:\w+ )*\w+): (.+)', line)
		
		if match:
			date = match.group(1)
			name = match.group(2)
			text = match.group(3)

			matchedUser = None

			for user in users:
				if user.name == name:
					matchedUser = user

			if matchedUser:
				matchedUser.messageCount += 1

			else:
				matchedUser = User(name)
				users.append(matchedUser)

			msg = Message(date, matchedUser, text)
			messages.append(msg)

	except EOFError:
		break

print("Users : ", len(users))
for user in users:
	print("User ", user.name, " has sent ", user.messageCount, " messages.")

date1 = messages[0].date_time
date2 = messages[-1].date_time
duration = date2 - date1

groups = {}
arr = []
previous = None

for message in messages:
	if len(arr) == 0:
		arr.append(message)
	else:
		fmt = "%m/%d/%y, %I:%M %p"
		time1 = datetime.strftime(previous.date_time, fmt)
		time2 = datetime.strftime(message.date_time, fmt)
		
		diff = message.date_time - previous.date_time
		print("comparing ", time1, " with ", time2, "diff: ", diff)
		if diff.total_seconds() < 3600:
			arr.append(message)
		else:
			groups[datetime.strftime(previous.date_time, "%m/%d/%y, %I:%M %p")] = arr
			arr = [message]
	previous = message
groups[datetime.strftime(previous.date_time, "%m/%d/%y, %I:%M %p")] = arr

print("Group length: ", len(groups))
# print("Group: ", groups)

print("Total message count : ", len(messages))
print("Duration: ", duration.days)

for key,value in groups.items():
	fmt = "%m/%d/%y, %I:%M %p"
	time1 = datetime.strftime(value[0].date_time, fmt)
	time2 = datetime.strftime(value[-1].date_time, fmt)
	print(key, "count: ", len(value), time1, time2)