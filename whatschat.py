#!/usr/bin/env python3
""" 
This is a simple WhatsApp chat analysis tool that takes WhatsApp chat text file
as an input and displays useful information like 
1. number of messages exchanged
2. Number of days messages extend to
3. Total time spend messaging etc
"""

from sys import argv, exit

line_count = 0

# if len(argv) < 2:
# 	print("usage: ", argv[0], " <txt>")
# 	exit()

while True:
	try:
		line = input()
		line_count += 1
	except EOFError:
		break

print("Line count: ", line_count)