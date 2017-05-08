import re

# Open file
f = open('chat.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'\d{1,2}/\d{1,2}/\d{1,2}', f.read())

print("Total messages exchanged: ", len(strings))

for string in strings:
	print(string)