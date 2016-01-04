source = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
alpha = 'abcdefghijklmnopqrstuvqwxyz'

check = False
num = 0

for x in source:

	num=0
	#check for letter
	if x==' ' or x=='(' or x==')' or x=='.':
		print ' '
		check = False
	
	else: check = True
	
	#find letter in alphabet, print out letter 2 spaces ahead of it
	if check==True:
		for letters in alpha:
				num += 1
				if x==letters:
					num+=1
					if num<=26:	
						#print num
						print alpha[num]
					elif num>26:
						print alpha[num-27]