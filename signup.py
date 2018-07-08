def signup(): 


	import MySQLdb as my

	print "Welcome to dynamic blood bank"

	print "sign up form"

	db = my.connect(host= "127.0.0.1",
					user="root",
					passwd="",
					db="logindb")
	query = db.cursor()
	print "connected"
	loop= 'true'
	while (loop == 'true'):
		name=raw_input("Enter name:")
		username=raw_input("Enter Username:")
		password=raw_input("Enter Password:")
		confirm_password=raw_input("Re-Enter Password:")
		mail=raw_input("Enter E-mail:")
		dob=raw_input("Enter DOB:")
		bloodgrp=raw_input("Enter the bloodgroup:")
		city=raw_input("Enter city:")
		mobile=raw_input("Enter the mobile number:")
		if(password == confirm_password):
			password= confirm_password
			query.execute("INSERT INTO `login` (`username`,`password`) VALUES(%s,%s)",(username,password))			
			query.execute("INSERT INTO `signup` (`name`,`mail`,`dob`,`bloodgrp`,`city`,`mobile`) VALUES (%s,%s,%s,%s,%s,%s)",(name,mail,dob,bloodgrp,city,mobile))
		
			db.commit()
			db.close()
			break
		else:
			print "Please Check Password"
	print "Registration Completed"
