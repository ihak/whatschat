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

# if len(argv) < 2:
# 	print("usage: ", argv[0], " <txt>")
# 	exit()

users = []
messages = []

def message_count(user, type):
	count = 0
	for message in messages:
		if (message.user.name == user.name) and  (message.type == type):
			count += 1
	return count

def message_print(user, type):
	for message in messages:
		if (message.user.name == user.name) and (message.type == type):
			# print(message.message)
			pass

def word_count(user, word):
	count = 0
	for message in messages:
		if (message.user.name == user.name) and (message.type == 'text'):
			wordCount = message.message.lower().count(word)
			count += wordCount

			if wordCount > 0:
				print(message.message)

	return count

while True:
	try:
		line = raw_input()
		
		match = re.match(r'(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2} (?:P|A)M) - ((?:\w+ )*\w+): (.+)', line)
		
		if match:
			date = match.group(1)
			name = match.group(2)
			text = match.group(3)

			# print(date)

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
	print("Media messages: ", message_count(user, 'media'), "Text messages: ", message_count(user, 'text'), "Links: ", message_count(user, 'link'))
	print("word used: ", word_count(user, "lol"))

date1 = messages[0].date_time
date2 = messages[-1].date_time
duration = date2 - date1

print("Total message count : ", len(messages))

print("Duration: ", duration.days)

print(messages[76].message)

user = users[1]
message_print(user, 'link')
