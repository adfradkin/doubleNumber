userNumber = input("Tell me a number: ")
finalNumber = None
while finalNumber != userNumber:
	try:
	#checks if its a number
		userNumber = float(userNumber)
	#only put lines that you expect to cause exceptions here
		finalNumber = userNumber
	except ValueError:
		userNumber = input("That is'nt a number, try again:")
		#

print("Double that is {}".format(userNumber*2))
