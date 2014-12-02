import os
import sys

userName = "Anonymous"
userMap = []
userLocation = 0
tasksCompleted = False

def welcomeWorld():
	os.system('clear')
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
	currentLocation = []
	textMap = ""
	textMap += "Start ----- "
	currentLocation.append("_____ ----- ")
	for i in range(len(userMap)):
		if userMap[i] == 0:
			textMap += "???? ----- "
			currentLocation.append("____ ----- ")
		else:
			currentLocation.append("____ ----- ")
			textMap += "DONE ----- "
	textMap += "Finished!\n"
	currentLocation[userLocation] = "__X__ ----- "
	print textMap
	for text in currentLocation:
		sys.stdout.write(text)
	print

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
	library = open('vocabLibrary.txt', 'r')
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
		elif userInput == '-viewDictionary':
			showDictionary(library)
		elif userInput == '-quit':
			break
		else:
			print "That is not a valid command. Please choose a command that is listed in -help\n"

def completedTasks():
	os.system('clear')
	if tasksCompleted == False:
		print "Thanks for playing! Try to finish next time :p"
	else:
		print "Great job! You have solved everything and you are one step closer to learning concurrent programming!"

def showDictionary(library):
	dictArray = []
	dictionary = {}
	for line in library:
		splitLine = line.rstrip('\n').split(':')
		dictArray.append(splitLine[0])
		dictionary[splitLine[0]] = splitLine[1]
	while(True):
		os.system('clear')
		counter = 0
		for item in dictArray:
			print str(counter) + ". " + item
			counter = counter + 1
		userInput = raw_input("Welcome to the concurrency library. Please type the number associated with the word you would like to learn about. (-1 to return)\n")
		if userInput == "-1":
			os.system('clear')
			break
		elif isinstance(int(userInput), int) and int(userInput) < len(dictionary.keys()):
			os.system('clear')
			tempWord = dictArray[int(userInput)]
			print tempWord + "\n"
			print "Definition:" + dictionary[tempWord]
			print "\n"
			raw_input('Enter to continue')
		else:
			print "That is not a valid option. Please enter a number or -1 to quit"

def help():
	print "-help: Brings up the list of possible commands"
	print "-viewMap: Shows a map of your current progress"
	print "-viewDictionary: Shows a list of vocabulary and provides definitions for them"
	print ""