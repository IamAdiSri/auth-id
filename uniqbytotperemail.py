#Command to run on terminal in the smai_proj folder:
#python uniqbytotperemail.py ./clean_enron/ > uniqbytotperemail.txt

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
		list2 = []
		for line in f:
			line = line.strip('\n')
			list1 = line.split()
			for item in list1:
				list2.append(item)
		count1 = len(set(list2))
		count = len(list2)
		#text = f.read()
		#count = len(text.split())
		uniqbytot = count1/float(count)
		print c+','+filename+','+str(uniqbytot)
		f.close()
