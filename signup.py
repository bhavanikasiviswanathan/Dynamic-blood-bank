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
			#otp generating module
			import random
			contents = "0123456789"
			otp_length = 6
			output =""
			for i in range(otp_length):
				index = random.randrange(len(contents))
			        output = output +contents[index]
 			output2 = "The OTP for Dynamic Blood Bank is "+output 
	
 			#otp sending module
			import smtplib

			fromaddr = "from_address"
			toaddr = mail
			msg = output2
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(fromaddr, "Password")
			server.sendmail(fromaddr, toaddr, msg)
			server.quit()
			otp = raw_input( "Please enter the OTP to login:")
			if(output == otp):		
				query.execute("INSERT INTO `signup` (`name`,`mail`,`dob`,`bloodgrp`,`city`,`mobile`) VALUES (%s,%s,%s,%s,%s,%s)",(name,mail,dob,bloodgrp,city,mobile))
				db.commit()
				db.close()
				break
			else:
				print "Sorry the OTP entered was WRONG!!"

		else:
			print "Please Check Password"
	print "Registration Completed"
