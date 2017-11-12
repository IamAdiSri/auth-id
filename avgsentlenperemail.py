#Command to run on terminal in the smai_proj folder:
#python avgsentlenperemail.py ./clean_enron/ > avgsentlenperemail.txt

import sys
import os
from nltk.tokenize import sent_tokenize

classes = ['Benjamin_Rogers','Chris_Dorland','Drew_Fossum','Jeffrey_Shankman','Kevin_Presto','Kimberly_Watson','Lynn_Blair','Mark_Haedicke','Michelle_Cash', 'Phillip_Allen']
#classes = ['Benjamin_Rogers']
#print len(classes)

direc = sys.argv[1]
#direc = "./clean_enron/"

for c in classes:
	listing = os.listdir(direc+c)
	#numemail = len(listing)
	#count = 0
	for filename in listing:
		f = open(direc+c+'/'+filename, 'r')
		count = 0
		count1 = 0
		for line in f:
			count1 = count1+1
			line = line.strip('\n')
			count = count + len(line.split())
		#text = f.read()
		#list1 = sent_tokenize(text)
		#numsent = len(list1)
		#count = len(text.split())
		#count = 0
		#for item in list1:
		#	count = count + len(item.split())
		avgsentlen = count/float(count1)
		print c+','+filename+','+str(avgsentlen)
		f.close()
	#avgword = count/float(numemail)
	#print c,avgword
