import os
import sys
import puzzle
import simulator
import time

statesList = []

def main():
  str1 = [ 'for x in xrange(100):'
         , '     import time'
         , '     time.sleep(0.01)'
         , '     controller.update_state(thread_id, str(x))'
         , 'controller.update_state(thread_id, "complete")']
  str2 = [ 'for x in xrange(100):'
         , '     import time'
         , '     time.sleep(0.01)'
         , '     controller.update_state(thread_id, str(x))'
         , 'controller.update_state(thread_id, "complete")']
  code = ['\n'.join(str1), '\n'.join(str2)]
  threads = map(mk_thread, code)

  def pred(states):
    global statesList
    #  print 'State 0: %i, State 1: %i' % (states[0], states[1])
    if states[0] == "complete" and states[1] == "complete":
      statesList.append((states[0], states[1]))
      return True, None
    else:
      statesList.append((states[0], states[1]))
      return False, None

  sim = simulator.Simulator(threads, pred)
  sim.run_sim()
  visualize()

def visualize():
  i=0
  movement = "n"
  while movement != "-next":
    os.system('clear')
    #print "NUM STATES IS " + str(len(statesList))
    states = statesList[i]
    print "Frame: " + str(i)
    for x in range(len(states)):
        print "State " + str(x) + ": " + str(states[x])
    movement = raw_input("\nHit Enter to go to the next snapshot.\nType p + Enter to go the the last snapshot. \nTo move on, type -next.\n")
    if movement == "":
      i = i + 1
      if i >= len(statesList):
        i = len(statesList)-1
    elif movement == "p":
      i = i - 1
      if i < 0:
        i = 0

def mk_thread(s):
  def f(controller, thread_id):
    exec s in globals(), locals()
  return f

if __name__ == '__main__':
  main()
