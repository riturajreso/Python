def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1,arg2):
	print "arg1 = %r and arg2 = %r" %(arg1, arg2)

def print_once(arg1):
	print "arg1 = %r" % arg1

def print_none():
	print "I am Nothinf"



print_two("Rituraj","Rakesh")
print_two_again("Shivam","Shameer")
print_once("Uttam")
print_none()