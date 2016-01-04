#Inputs
x = 600851475143

#No point checking if 0 or 1 can divide in, so start with 2
y = 2

#Checks if number can evenly divide into input
def dividesEqually(x, y):
	while y < 13195:
		if x%y == 0:
			if checkIfPrime(y) is True:
				print y
				
		y += 1

#Checks if number that can divide evenly into input is a prime		
def checkIfPrime(x):
			y = 2
			while y < x:
				if x%y == 0:
					return False
				y += 1
			return True

dividesEqually(x, y)
