x = 100
y = 950


def mulEverything(x, y):
	w = 0
	while y<1000:
		x = 0
		while x<1000:
			z = x*y
			if isPalindrome(z) is True:
				if z>w:
					w = z
					print z
			x += 1
		y += 1
	
def isPalindrome(x):
	list = map(int, str(x))
				
	if len(list)==6:
		if list[0] == list [5] and list[1] == list[4] and list[2] == list[3]:
			return True
	else:
		return False
		#elif len(list)==5:
	#	if list[0] == list[4] and list[1] == list[3]:
	#		print list, "is a palindrome"
	
	
mulEverything(x, y)
