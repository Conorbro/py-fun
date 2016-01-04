import string, re                                                                                                                                                                               
#open the file                                                                                                                                                               
eqfile = open("file.txt")                                                                                                                                                
gibberish = eqfile.read()                                                                                                                                                    
eqfile.close()                                                                                                                                                           

print "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", gibberish))
