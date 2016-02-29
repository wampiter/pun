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

#Vowel replacements:
closed=codecs.open('close.txt','r','utf-8')
opens=codecs.open('open.txt','r','utf-8')
for line in closed:
	closeline=line #No puns here!

for line in opens:
	openline=line

subs = []

for char in ipa:
	if char in closeline:
		for vow in closeline:
			a=ipa.replace(char,vow)
			subs.append(a)

for char in ipa:
	if char in openline:
		for vow in openline:
			a=ipa.replace(char,vow)
			subs.append(a)

done = [eng]
print "\nThe following are English phonetic superstrings of the entered word:\n"
for line in wordlist:
	words = string.split(line)
	for ipa in subs:
		if ipa in words[1] and words[0] not in done:
			print words[0]
			done.append(words[0])



print "\nThe following are English phonetic substrings of the entered word:\n"
for line in wordlist:
	words = string.split(line)
	for ipa in subs:
		if words[1] in ipa and words[0] not in done:
			print words[0]
			done.append(words[0])