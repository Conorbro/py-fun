y = 0
x = 0
while x < 1000:
	if (x%3) and (x%5) == 0:
		y += x
	elif (x%3) == 0:
		y += x
	elif (x%5) == 0:
		y +=x
	x += 1	
print y