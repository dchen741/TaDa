from interface_io import *
from simulator import Simulator

import os

class Puzzle:
  def __init__(self, title, lesson, lines, code, answer, translator, predicate, semaphores, poll_rate = 0.01, hint=''):
    self.solved     = False
    self.title      = title
    self.lesson     = lesson
    self.lines      = lines
    self.code       = code
    self.answer     = answer
    self.translator = translator
    self.predicate  = predicate
    self.semaphores = semaphores
    self.poll_rate  = poll_rate
    self.hint       = hint

  def start_puzzle(self):
    while(not self.solved):
      while(True):
        response_code = self.code
        for i, l in enumerate(self.lines):
          clear()
          put_text(self.lesson)
          print_code(response_code, "\nThe code currently is:")
          resp = int(get_text('Place the line \'%s\': ' % l))
          response_code = self.process_input(resp, l, response_code)
        threads = self.translator(response_code)
        simulator = Simulator(threads, self.predicate, self.semaphores, self.poll_rate)
        success, message = simulator.run_sim()
        simulator.visualize()
        if success:
          put_text('Simulator test Passed!')
        else:  
          put_text('Simulator test Failed!')
        put_text(message)
        get_text('Check against the real answer? (y/n)')

        clear()
        put_text(self.lesson)
        print_code(response_code, "\nThe code currently is:")

        if(response_code == self.answer):
          put_text("Congratulations! That's correct. Good job!\n")
          break
        else:
          get_text("Woops! That's incorrect. Try again? (y/n)\n")
      self.solved = True

  def process_input(self, index, line, code_str):
    code = code_str.split('\n')
    code.insert(index, line)
    return '\n'.join(code)
