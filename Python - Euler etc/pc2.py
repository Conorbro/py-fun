alpha = 'abcdefghijklmnopqrstuvqwxyz'

openfile = open('file.txt')
openfile.read()

with open('file.txt') as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    for letters in alpha:
				if c==letters:
					print c