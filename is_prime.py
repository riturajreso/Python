def is_prime(num):
	if num < 2:
		return 0
	else:
		divisor = 2
		for i in range(divisor,num):
			if num % i == 0:
				return 0	
		return	1

def getNextPrime(n):
	prime = is_prime(n)
	if prime == 0:
		print "Not a prime no"
	else:
		for x in range(n,n+50):
			if is_prime(x) == 1:
				print x

#getNextPrime(5)