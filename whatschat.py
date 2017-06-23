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

def message_count(user, type):
	count = 0
	for message in messages:
		if (message.user.name == user.name) and  (message.type == type):
			count += 1
	return count

def message_print(user, type):
	for message in messages:
		if (message.user.name == user.name) and (message.type == type):
			print(message.message)
			pass

def word_count(user, word):
	count = 0
	for message in messages:
		if (message.user.name == user.name) and (message.type == 'text'):
			wordCount = message.message.lower().count(word)
			count += wordCount

			# if wordCount > 0:
				# print(message.message)

	return count

def group_messages(messages):
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
			# print("comparing ", time1, " with ", time2, "diff: ", diff)
			if diff.total_seconds() < 3600:
				arr.append(message)
			else:
				groups[datetime.strftime(previous.date_time, "%m/%d/%y, %I:%M %p")] = arr
				arr = [message]
		previous = message
	groups[datetime.strftime(previous.date_time, "%m/%d/%y, %I:%M %p")] = arr

	return groups

def group_description(groups):
	max_minutes = 0
	max_messages = 0

	for key,value in groups.items():
		startTime = value[0].date_time
		endTime = value[-1].date_time

		fmt = "%m/%d/%y, %I:%M %p"
		startTimeStr = datetime.strftime(startTime, fmt)
		endTimeStr = datetime.strftime(endTime, fmt)
		duration = endTime - startTime
		
		minutes = duration.seconds/60
		message_count = len(value)

		if max_minutes < minutes:
			max_minutes = minutes

		if max_messages < message_count:
			max_messages = message_count

		print("{} messages sent between {} and {} over a duration of {} minutes".format(message_count, startTimeStr, endTimeStr, minutes))

	print("Maximum number of messages sent: {}".format(max_messages))
	print("Maximum number of minutes: {}".format(max_minutes))

def group_max(groups):
	max_minutes = 0
		max_messages = 0

		for key,value in groups.items():
			startTime = value[0].date_time
			endTime = value[-1].date_time

			fmt = "%m/%d/%y, %I:%M %p"
			startTimeStr = datetime.strftime(startTime, fmt)
			endTimeStr = datetime.strftime(endTime, fmt)
			duration = endTime - startTime
			
			minutes = duration.seconds/60
			message_count = len(value)

			if max_minutes < minutes:
				max_minutes = minutes

			if max_messages < message_count:
				max_messages = message_count

	return (max_messages, max_minutes)	

def main():
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

	print("Total Users in this chat: ", len(users))
	# for user in users:
	# 	print("User ", user.name, " has sent ", user.messageCount, " messages.")
	# 	print("Media messages: ", message_count(user, 'media'), "Text messages: ", message_count(user, 'text'), "Links: ", message_count(user, 'link'))
		# print("word used: ", word_count(user, "lol"))

	date1 = messages[0].date_time
	date2 = messages[-1].date_time
	duration = date2 - date1

	groups = group_messages(messages)
	group_description(groups)

	print("Conversations: ", len(groups))
	# print("Group: ", groups)

	print("Total messages exchanged: ", len(messages))

	print("Total days: ", duration.days)
	print("Messages per day: ", len(messages)/duration.days)

main()