from sys import argv

scritp, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file\n."
print_all(current_file)

print "Printing lines"
line_no = 1;
print_a_line(line_no,current_file)	

line_no = line_no + 1;
print_a_line(line_no,current_file)	

line_no = line_no + 1;
print_a_line(line_no,current_file)	
