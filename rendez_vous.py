from puzzle import Puzzle
import copy
import utils

import threading

semaphores = {
  'alice' : threading.Semaphore(),
  'bob'   : threading.Semaphore()
}

def get_block(lines):
  block = []
  i = 0
  for line in lines:
    i += 1
    if line == 'break':
      break
    elif line:
      block.append(line)
  return block, lines[i:]

def trans_line(line):
  trans = {
    '  alice.signal()':'controller.semaphores[\'alice\'].release()',
    '  bob.signal()':'controller.semaphores[\'bob\'].release()',
    '  alice.wait()':'controller.semaphores[\'alice\'].acquire()',
    '  bob.wait()':'controller.semaphores[\'bob\'].acquire()',
    '  Alice arrives':'controller.update_state(thread_id, \'Alice is here\')',
    '  Bob arrives':'controller.update_state(thread_id, \'Bob is here\')',
    '  Alice enters the park':'controller.update_state(thread_id, \'Alice is inside\')',
    '  Bob enters the park':'controller.update_state(thread_id, \'Bob is inside\')',
    'Thread Alice:':'',
    'Thread Bob:':'',
    '':'break',
  }
  return trans[line]

def translator(input):
  threads = []
  code = map(trans_line, input.split('\n'))
  while code:
    thread, code = get_block(code)
    threads.append(copy.deepcopy(thread))
  threads = ['\n'.join(t) for t in threads]
  return map(utils.mk_thread, threads)

prev_states = None
stagnant = 0
def predicate(states):
  global stagnant

  # check if one is inside and not the other
  if states[0] == 'Alice is inside' and states[1] == 'Bob is inside':
    return True, False, 'Both have entered together!'
  if states[0] == 'Alice is inside' and states[1] != 'Bob is inside':
    return False, True, 'Oh no! Alice went inside without Bob!'
  if states[0] != 'Alice is inside' and states[1] == 'Bob is inside':
    return False, True, 'Oh no! Bob went inside without Alice!'

  # Keep track of how long it's been since something changed
  if not prev_states:
    stagnant = 0
  if states == prev_states:
    stagnant += 1
  else:
    stagnant = 0

  # If nothing has changed in a while, assume deadlock
  if stagnant > 100:
    return False, True, 'Uh oh! Alice and Bob haven\'t moved in a long time. You might have caused a deadlock!'

  return False, False, ''

# Puzzle(self, title, lesson, lines, code, answer, translator, predicate, poll_rate = 0.01, hint=''):
rendez_vous_p = Puzzle("Rendez-vous", #title
                "Alice and Bob are going to the amusement park. They intend to meet at the gate and enter together. You can use 'alice.signal()' to signal alice's arrival, and 'alice.wait()' to wait until alice has signaled her arrival. The same is true for 'bob.signal()' and 'bob.wait()'. Add these lines to the given code to ensure neither will enter the park without the other.", #lesson
                ['  alice.signal()', '  alice.wait()', '  bob.signal()', '  bob.wait()'], #lines
                "Thread Alice:\n  Alice arrives\n  Alice enters the park\n\nThread Bob:\n  Bob arrives\n  Bob enters the park", #code
                "Thread Alice:\n  Alice arrives\n  alice.signal()\n  bob.wait()\n  Alice enters the park\n\nThread Bob:\n  Bob arrives\n  bob.signal()\n  alice.wait()\n  Bob enters the park", #answer
                translator, #translator
                predicate, #predicate
                semaphores, #semaphores
                )

def main():
  rendez_vous_p.start_puzzle()

if __name__ == '__main__':
  main()
