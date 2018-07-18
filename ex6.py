x = "There are %d types of people." %10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)

print x
print y

print "I said: %r" %x
print "I also said: %r" %y

hilarious = False
joke_eva = "Isn't that joke so funny ? %r"

print joke_eva %hilarious

w = "This is the left side of the string----"
e = "This is the right side of the string ----"

print w + e
