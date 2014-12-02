import os

userName = "Anonymous"
userMap = []
userLocation = 0

def welcomeWorld():
	print "\n"
	print "************************************************************"
	print "**********                                        **********"
	print "**********                 Welcome!               **********"
	print "**********                                        **********"
	print "**********          As the new owner of this      **********"
	print "**********       amusement park, you have some    **********"
	print "**********             things to fix!             **********"
	print "**********                                        **********"
	print "**********                                        **********"
	print "************************************************************"

def about():
	print "\nAbout: This project was created by students with the goal to "
	print "teach others about the basic concepts of concurrent programming.\n"

def getName():
	global userName
	userName = raw_input("What is your name? ")
	return userName

def drawMap():
	print "Here is your current progress today! The 'x' marks your current location"
	currentLocation = ""
	textMap = ""
	textMap += "Start ----- "
	currentLocation += "_____ ----- "
	for i in range(len(userMap)):
		if userMap[i] == 0:
			textMap += "???? ----- "
			currentLocation += "____ ----- "
		else:
			currentLocation += "____ ----- "
			textMap += "DONE ----- "
	textMap += "Finished!\n"
	print textMap
	print currentLocation

def put_text(string):
	print string

def get_text(p=''):
	userInput = None
	while True:
		userInput = raw_input(p)
		if userInput:
			return userInput
		put_text('No input read. Try again:')

def beginAdventure():
	print "Hello " + userName + "! I am your assistant, Sam Ifor. There is a lot of work to be done. Today, there are some problems that need to be fixed! Let us get to it shall we?\n"
	numTasks = raw_input("How many tasks would you like to fix today (1-3)? ")
	global userMap
	for i in range(int(numTasks)):
		userMap.append(0)
	print "Great!\n"
	print "If you are new to this, feel free to type '-help' to get a list of possible commands\n"
	while(True):
		userInput = raw_input("What would you like to do? (-help for list of options)\n")
		if userInput == '-help':
			help()
		elif userInput == '-viewMap':
			drawMap()
		elif userInput == '-quit':
			break
		else:
			print "That is not a valid command. Please choose a command that is listed in -help\n"

def completedTasks():
	os.system('clear')
	print "Great job! You have solved everything and the park is fully functional!"

def help():
	print "-help: Brings up the list of possible commands"
	print "-viewMap: Shows a map of your current progress"
	print ""

def print_code(code, message=None):
	os.system('clear')
	if message:
		print message
	for i, line in enumerate(code.split('\n')):
		print '%s %s' % (str(i).ljust(2), line)
