from PIL import Image
from random import randint
import requests

# Get random word from the dictionary
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.splitlines()
word = WORDS[randint(0,len(WORDS))].lower()

def startGame():
	# Initialize Game
	win = False
	lost = False
	find = False
	copy = list("")
	guesses = -1

	# Set Blank Spaces in user's guess
	for x in word:
		copy+="_"

	print "Welcome to Hangman!"

	# Game Loop
	while not win and not lost:

		# Prompt user for guess
		guess = raw_input('Enter guess letter (no longer than 1 character in length):')[:1]
		print 'Guess = ', guess

		# Check guess letter against set word
		y = 0
		find = False

		for x in word:
			if guess==x:
				copy[y] = x
				print 'Letter found in space ', y, 'of', len(word)
				find = True
				print "Word = ", copy
			y += 1

		if not find:
			if guesses > 0:
				image.close()
			guesses += 1
			image = Image.open('hang' + str(guesses) + '.gif')
			image.show()
			if guesses > 9:
				lost = True
				print "You've been hung! :("
			else:
				print 'Letter', guess, 'not found in word.'

		if ''.join(copy) == word:
			win = True
	if win:
		print "You won using", guesses + len(word), "guesses!"
	else:
		print "You lost!"
	print "Exiting..."

startGame()
