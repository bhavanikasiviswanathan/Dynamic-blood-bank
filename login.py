
def login():
	import MySQLdb

	print "Welcome to Dynamic Blood Bank"

	db = MySQLdb.connect(host= "127.0.0.1",
						 user="root",
					 	passwd="",
					 	db="logindb")
	query = db.cursor()

	loop= 'true'
	while (loop == 'true'):
		username = raw_input("Username: ")
		password = raw_input("Password: ")
		if(query.execute("SELECT * from  `login`  WHERE `username` = '"+username+"'  AND `password` = '"+ password +"'")):
			db.commit()
			print "logged in"
			break
		else:
			db.commit() 
			print "Please Register"
			decision = raw_input("If you want to Register type '1' want to exit type '2':")
			s= "1"
			if (decision == s):
				from signup import *
				signup()
				
			else:
				break