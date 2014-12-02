import text_interface as interface

import os

class Puzzle:
  def __init__(self, title, lesson, lines, code, answer, hint=''):
    self.id     = 1 #TODO: increment ids
    self.solved = False
    self.title  = title
    self.lesson = lesson
    self.lines  = lines
    self.code   = code
    self.answer = answer
    self.hint   = hint

  def start_puzzle(self):
    while(not self.solved):
      interface.put_text(self.lesson)
      interface.get_text('Ready for the puzzle? (y/n)\n')
      while(True):
        response_code = self.code
        for i, l in enumerate(self.lines):
          interface.print_code(response_code, "The code currently is:")
          resp = int(interface.get_text('Place the line \'%s\': ' % l))
          response_code = self.process_input(resp, l, response_code)

        interface.print_code(response_code, "The code currently is:")

        if(response_code == self.answer):
          interface.put_text("Congratulations! That's correct. Good job!\n")
          break
        else:
          interface.put_text("Woops! That's incorrect. Try again!\n")
      self.solved = True
      return self.id

  def process_input(self, index, line, code_str):
    code = code_str.split('\n')
    code.insert(index, line)
    return '\n'.join(code)
