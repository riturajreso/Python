def break_words(stuff):
	"""This function will break up words for us.- In array format"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(- 1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

ex_sentence = 'Myself Rituraj, Kabhi Kabhi apun ko lagta hai apunech bhagwan hai!!!'
#Priya => ['P', 'a', 'i', 'r', 'y']
#print => ['a', 'i', 'p', 'r', 'y']
ex_word = 'priya' 
word_test = break_words(ex_sentence)

print break_words(ex_sentence)
print sort_words(word_test)
print_first_word(word_test)
print_last_word(word_test)
print sort_sentence(ex_sentence)
print_first_and_last(ex_sentence)
print_first_and_last_sorted(ex_sentence)