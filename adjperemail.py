#Command to run on terminal in the smai_proj folder:
#python3 adjperemail.py ./clean_enron/ > adjperemail.txt

import sys
import os
import nltk

classes = ['Benjamin_Rogers','Chris_Dorland','Drew_Fossum','Jeffrey_Shankman','Kevin_Presto','Kimberly_Watson','Lynn_Blair','Mark_Haedicke','Michelle_Cash', 'Phillip_Allen']
#classes = ['Benjamin_Rogers']

direc = sys.argv[1]
#direc = "./clean_enron/"

for c in classes:
	listing = os.listdir(direc+c)
	for filename in listing:
		f = open(direc+c+'/'+filename, 'r')
		text = f.read()
		tok = nltk.word_tokenize(text)
		postag = nltk.pos_tag(tok)
		count = 0
		for i in range(len(postag)):
			if postag[i][1] == "JJ" or postag[i][1] == "JJR" or postag[i][1] == "JJS":
				count = count + 1
		print(c+','+filename+','+str(count))
		f.close()

