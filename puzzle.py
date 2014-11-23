import text_interface as interface

class Puzzle:
	def __init__(self, title, lesson, prompt, code, answer):
		self.id = 1
		self.solved = False
		self.title = title
		self.lesson = lesson
		self.prompt = prompt
		self.code = code
		self.answer = answer

	def start_puzzle(self):
		while(not self.solved):
			interface.put_text(self.lesson)
			interface.get_text('Ready?\n')
			interface.put_text(self.code)
			userInput = None
			while(True):
				userInput = interface.get_text(self.prompt)
				if(self.process_input(userInput) == self.answer):
					interface.put_text("Congratulations! That's correct. Good job!\n")
					break
				else:
					interface.put_text("Woops! That's incorrect. Try again!\n")
			self.solved = True
			return self.id

	def process_input(self, input):
		code = self.code.split('\n')
		i = int(input)
		code.insert(i, "print 'hello world!'")
		return '\n'.join(code)

	# def print_puzzle(self):
		# interface.put_text(self.)