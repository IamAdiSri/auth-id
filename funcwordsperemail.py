#Command to run on terminal in the smai_proj folder:
#python3 funcwordsperemail.py ./clean_enron/ > funcwordsperemail.txt

import sys
import os
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

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
		text = f.read()
		tok = nltk.word_tokenize(text)
		count = 0
		for item in tok:
			if item in stop_words:
				count = count + 1
		#postag = nltk.pos_tag(tok)
		print(c+','+filename+','+str(count))
		f.close()

