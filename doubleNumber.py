#Author: Jared Lefkort
#Date: 2/29/2016

number = input("What number should I double? ")

errorMessage = True

while errorMessage == True:
	try:
		number = float(number)
		
		#could put the doubling line here
		#try block is only for exception causers
	except ValueError:
		number = input("Sorry thats not a number. Try again: ")
		errorMessage = True

	else:	
		print("Double that is {}.".format(number * 2))
		errorMessage = False