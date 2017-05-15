""" Message class. Represents a message."""

from datetime import datetime

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