import os

def put_text(string):
  print string

def get_text(p=''):
  userInput = None
  while True:
    userInput = raw_input(p)
    if userInput:
      return userInput
    put_text('No input read. Try again:')

def print_code(code, message=None):
  if message:
    print message
  for i, line in enumerate(code.split('\n')):
    print '%s %s' % (str(i).ljust(2), line)

def clear():
  os.system('clear')
