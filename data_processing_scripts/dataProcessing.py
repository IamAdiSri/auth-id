#!/usr/bin/python
import MySQLdb
import os
# Open database connection
db = MySQLdb.connect("localhost","root",<password>,"enron")

# prepare a cursor object using cursor() method
# abstraction meant for data set traversal
# one cursor per connection
cursor = db.cursor()

try:
   	# Execute the SQL command
	cursor.execute("""select E.firstName, E.lastName, M.body, M.mid from message as M, employeelist as E where (Email_id = sender or Email2 = sender or Email3 = sender or Email4 = sender) and M.folder LIKE '%Sent%' and eid in (10, 18, 92, 31, 137, 117, 20, 118, 65, 36, 112, 16);""")
	# Commit your changes in the database
   	db.commit()

	###########################################################
	###########################################################

	# Fetch a single row using fetchall() method.
	data_1 = cursor.fetchall()
	for record in data_1:
		#os.system('mkdir -p ' + 'clean_enron/' + record[1] + '_' + record[2])
		with open('./clean_enron/' + record[0] + '_' + record[1] + '/' + str(record[3]) + '.txt', 'w+') as f:
			f.write(record[2] + '\n')

	###########################################################
	###########################################################

	rc = cursor.rowcount
	print "\nRow count: ", rc

except:
   	# Rollback in case there is any error
   	db.rollback()
   	print ("Exception")

#close the cursor
cursor.close()

# close the connection
db.close()
