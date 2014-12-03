import os
import sys
import puzzle
import simulator

statesList = []

def main():
  str1 = """for x in xrange(100):
              import time
              time.sleep(0.01)
              controller.update_state(thread_id, x)"""
  str2 = [ 'for x in xrange(100):'
         , '     import time'
         , '     time.sleep(0.01)'
         , '     controller.update_state(thread_id, x)']
  code = [str1, '\n'.join(str2)]
  threads = map(mk_thread, code)

  def pred(states):
    global statesList
    if states[0] == 99 and states[1] == 99:
      for states in statesList:
        print 'State 0: %i, State 1: %i' % (states[0], states[1])
      print 'DONE!'
      return True, None
    else:
      if states[0] and states[1] and states[0] != states[1]:
        statesList.append((states[0], states[1]))
      return False, None

  sim = simulator.Simulator(threads, pred)
  sim.run_sim()
  visualize()

def visualize():
  i=0
  print "LENGTH IS" + str(len(statesList))
  while i < range(len(statesList)):
    movement = raw_input("\nType n to go to the next snapshot, or p to go the the last snapshot.\n")
    os.system('clear')
    if movement == "n":
      print "Frame: " + str(i)
      states = statesList[i]
      for x in range(len(states)):
        print "State" + str(x) + ": " + str(states[x])
      i = i + 1
    elif movement == "p":
      i = i - 1
      states = statesList[i]
      for x in range(len(states)):
        print "State" + str(x) + ": " + str(states[x])
      i = i + 1

def mk_thread(s):
  def f(controller, thread_id):
    exec s in globals(), locals()
  return f

if __name__ == '__main__':
  main()
