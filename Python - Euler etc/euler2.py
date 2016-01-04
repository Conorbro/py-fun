x = 0 #first 
y = 2 #second 
z = 1 #third 
evenSum = 2 #Be sure to include the first even number in the Fibonacci sequence below 4 million!

while x < 4000000:
		x = z + y 		#make new number from previous two numbers
		z = y 			#z equals old number
		y = x 			#y equals new number
		
		if x%2==0:		#if x is even add to evenSum
			print x
			evenSum += x
		
print evenSum