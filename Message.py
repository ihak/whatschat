""" Message class. Represents a message."""

from datetime import datetime
import re

class Message(object):
	"""Represents a single message in the chat"""
	def __init__(self, date, user, message):
		super(Message, self).__init__()
		
		fmt = "%m/%d/%y, %I:%M %p"

		try:
			self.date_time = datetime.strptime(date, fmt)
		except ValueError:
			print("unable to parse the date")

		self.user = user
		self.message = message

		if self.message == "<Media omitted>":
			self.type = 'media'
		elif len(re.findall(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', self.message)) > 0:
			self.type = 'link'
		else:
			self.type = 'text'
