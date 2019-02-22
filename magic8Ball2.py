import random

# notes about lists in python
# lists can span multiple lines
# they are unaffected by white space

# list of magic 8 ball responses
messages = ['It is almost certainly so',
			'Retry later sometime',
			'I would say no',
			'It aint lookin good boss',
			'Probably not likely',]

# output a random message from the list
print(messages[random.randint(0, len(messages) - 1)])


