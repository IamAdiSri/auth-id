#Command to run on terminal in the smai_proj folder:
#python wordsperemail.py ./clean_enron/ > wordsperemail.txt

import sys
import os

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
		for line in f:
			line = line.strip('\n')
			count = count + len(line.split())
		#text = f.read()
		#count = len(text.split())
		print c+','+filename+','+str(count)
		f.close()
