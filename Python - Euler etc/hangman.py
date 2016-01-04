from PIL import Image
import subprocess

#Set Word
win = False 
find = False
word = list("elephant")
copy = list("")
guesses = 0

#Set Blank Spaces
for x in word:
	copy+="_"

#Game Loop
while win==False:
	
	#Prompt user for guess
	guess = raw_input('Welcome to hangman! Enter guess letter:')
	guesses += 1
	print 'Guess = ', guess

	#check guess letter against set word
	y = 0
	find = False
	
	for x in word:
		
		if guess==x:
			copy[y] = x
			print 'Letter found in space ', y, 'of', len(word) 
			find = True
			print "Word = ", copy
		y += 1
		
	if find==False:
		#image = Image.open('hang.png')
		#image.show()
		#p = subprocess.Popen(["display", "hang.png"])
		print 'Letter', guess, 'not found in word.'	

	if copy==word:
		win = True

print "You won using ", guesses, " guesses!"