""" User class. Represents a single user in a chat."""

class User(object):
	""" User class representing a single user in a chat."""

	def __init__(self, name):
		super(User, self).__init__()
		self.name = name
		self.messageCount = 1