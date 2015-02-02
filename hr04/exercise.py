'''
In your program, you're given a string that contains the body of an
email. If the email contains the word "emergency", print out "Do you
want to make this email urgent?" If it contains the word "joke", 
print out "Do you want to set this email as non-urgent?"
'''

email1 = "This is a really bad joke!"

email2 = "This is an emergency!"

email3 =  "Hey, how's it been?"

email_list = [email1, email2, email3]

for i in email_list:
	
	print
	print 'This is the email: '
	print i
	print

	if i.count('emergency') :
		print 'Do you want to make this email urgent?\n'
	elif i.count('joke'):
		print 'Do you want to set this email as non-urgent?\n'
	else:
		print 'No trigger words found.\n'