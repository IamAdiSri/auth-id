import sys
import os


# Create vectors of stylometric features from all the features
# Features must be in lexicographical ordering wrt (Author_name, file_name)

#####################################

file_ids = []

style_vectors = []

## file_names = 'adjperemail', 'funcwordsperemail', 'perpronperemail',
## 'avgsentlenperemail', 'avgwordlenperemail', 'charsperemail', 
## 'uniqbytotperemail', 'wordsperemail'

######################################
ctr = 0
l = []

with open('./extracted_features/adjperemail.txt', 'r') as f:
	for line in f:
		l = line.strip().split(',')
		style_vectors.append(l)
ctr += 3



with open('./extracted_features/funcwordsperemail.txt', 'r') as f:
	for line in f:
		l = line.split(',')
		for vec in style_vectors:
			if l[0] == vec[0] and l[1] == vec[1] :
				vec.append(l[2].strip())
ctr += 1
for vec in style_vectors:
	if len(vec) < ctr :
		vec.append(0.0)



with open('./extracted_features/perpronperemail.txt', 'r') as f:
	for line in f:
		l = line.split(',')
		for vec in style_vectors:
			if l[0] == vec[0] and l[1] == vec[1] :
				vec.append(l[2].strip())
ctr += 1
for vec in style_vectors:
	if len(vec) < ctr :
		vec.append(0.0)



with open('./extracted_features/avgsentlenperemail.txt', 'r') as f:
	for line in f:
		l = line.split(',')
		for vec in style_vectors:
			if l[0] == vec[0] and l[1] == vec[1] :
				vec.append(l[2].strip())
ctr += 1
for vec in style_vectors:
	if len(vec) < ctr :
		vec.append(0.0)


with open('./extracted_features/avgwordlenperemail.txt', 'r') as f:
	for line in f:
		l = line.split(',')
		for vec in style_vectors:
			if l[0] == vec[0] and l[1] == vec[1] :
				vec.append(l[2].strip())
ctr += 1
for vec in style_vectors:
	if len(vec) < ctr :
		vec.append(0.0)


with open('./extracted_features/charsperemail.txt', 'r') as f:
	for line in f:
		l = line.split(',')
		for vec in style_vectors:
			if l[0] == vec[0] and l[1] == vec[1] :
				vec.append(l[2].strip())
ctr += 1
for vec in style_vectors:
	if len(vec) < ctr :
		vec.append(0.0)


with open('./extracted_features/uniqbytotperemail.txt', 'r') as f:
	for line in f:
		l = line.split(',')
		for vec in style_vectors:
			if l[0] == vec[0] and l[1] == vec[1] :
				vec.append(l[2].strip())
ctr += 1
for vec in style_vectors:
	if len(vec) < ctr :
		vec.append(0.0)


with open('./extracted_features/wordsperemail.txt', 'r') as f:
	for line in f:
		l = line.split(',')
		for vec in style_vectors:
			if l[0] == vec[0] and l[1] == vec[1] :
				vec.append(l[2])
ctr += 1
for vec in style_vectors:
	if len(vec) < ctr :
		vec.append(0.0)
	if len(vec) != 10:
		print "Some vector is wrong"
		print vec


sv_file = open("stylometricVector.txt", "w+")

'''
element = ''

for vec in style_vectors:
	temp = ''
	for element in vec:
		temp += element.strip('\n') + ','
		temp.strip('\n')
	temp.strip()
	temp.strip(',')
	temp += '\n'
	sv_file.write(temp)

'''

for vec in style_vectors:
	temp = ','.join(vec)
	sv_file.write(temp)

sv_file.close()