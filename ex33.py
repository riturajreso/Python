i = 0
numbers = []

def insert_data(n):
	global i
	while i < n:
		print "No at the top is %d" %i
		numbers.append(i)
		i = i + 1 
		print "Numbers are  ", numbers
		print "No at the bottom is %d" %i
	for x in numbers:
		print x

insert_data(5)
