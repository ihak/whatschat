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

line_count = 0

# if len(argv) < 2:
# 	print("usage: ", argv[0], " <txt>")
# 	exit()

users = []

while True:
	try:
		line = raw_input()
		
		match = re.match(r'(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{2} (?:(?:P|A)M)) - ((?:\w+ )*\w+):', line)
		
		if match:
			date = match.group(1)
			time = match.group(2)
			name = match.group(3)

			matchedUser = None

			for user in users:
				if user.name == name:
					matchedUser = user

			if matchedUser:
				matchedUser.messageCount += 1

			else:
				users.append(User(name))

		line_count += 1
	except EOFError:
		break

print("Users : ", len(users))
totalMessages = 0
for user in users:
	totalMessages += user.messageCount
	print("User ", user.name, " has sent ", user.messageCount, " messages.")

print("Total message count : ", totalMessages)