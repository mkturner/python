'''
	Given a number, write a snippet of code that will print
	"You have money" if > 0
	"You're out" if == 0
	"You seem to be in debt" if < 0
'''

money = input("Enter the amount of money you have: ")

if (money > 0): 
	print "You have money"
elif (money < 0):
	print "You seem to be in debt"
else:
	print "You're out"