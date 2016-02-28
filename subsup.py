#This program finds all phonetic sub and super strings of the given ENGLISH word.

import codecs
import string
#reload(sys)
dicty=codecs.open('nocdict.txt', 'r', 'utf-8')
#sys.setdefaultencoding('utf-8')
eng = raw_input("Please enter an English word (spelling counts):\n")
eng=eng.lower()

wordlist=[]

for line in dicty:
	wordlist.append(line)

for line in wordlist:
	words = string.split(line)
	if eng == words[0]: #The Enlish words are the 0 column, so we find our word there
		ipa = words[1] #And we save the IPA for that word

dicty.close() #This is a messy fix to a bug: if I close and open the file the "for line in..." line works fine, otherwise not so much...

print "\nThe following are English phonetic superstrings of the entered word:\n"
for line in wordlist:
	words = string.split(line)
	if ipa in words[1]:
		print words[0]



print "\nThe following are English phonetic substrings of the entered word:\n"
for line in wordlist:
	words = string.split(line)
	if words[1] in ipa:
		print words[0]

