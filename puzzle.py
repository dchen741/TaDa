class Puzzle:
	def __init__(self, t, less, p, cde, ansr):
		self.id = 1
		self.solved = False
		self.title = t
		self.lesson = less
		self.prompt = p
		self.code = cd
		self.answer = ansr

	def start_puzzle(self):
		while(self.solved == False):
			print self.lesson
			userInput = ''
			while (userInput != 'ok'):
				userInput = raw_input("Type 'ok' to continue\n")
			print self.code
			while(userInput != self.answer):
				userInput = raw_input(prompt)
				if(userInput != self.answer):
					print("Woops! That's incorrect. Try again!\n")
			self.solved = True
			return self.id

