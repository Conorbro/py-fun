y = 20
found = False

while found == False:
		x = 1
		count = 0
		while x <= 20:
			if y%x == 0:
				count += 1
			else:	
				break
			x += 1
			#print x , "x"
			#print count , "Count"
			if count == 20:
				found = True
				print y
		y += 1
		#print y
	