import puzzle
import simulator

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
      sim.add_state((states[0], states[1]))
      return True, None
    else:
      sim.add_state((states[0], states[1]))
      return False, None

  sim = simulator.Simulator(threads, pred)
  sim.run_sim()
  sim.visualize()

def mk_thread(s):
  def f(controller, thread_id):
    exec s in globals(), locals()
  return f

# def run_code():
#   str1 = [ 'for x in xrange(100):'
#          , '     import time'
#          , '     time.sleep(0.01)'
#          , '     controller.update_state(thread_id, str(x))'
#          , 'controller.update_state(thread_id, "complete")']
#   str2 = [ 'for x in xrange(100):'
#          , '     import time'
#          , '     time.sleep(0.01)'
#          , '     controller.update_state(thread_id, str(x))'
#          , 'controller.update_state(thread_id, "complete")']
#   code = ['\n'.join(str1), '\n'.join(str2)]
#   threads = map(mk_thread, code)

#   def pred(states):
#     global statesList
#     #  print 'State 0: %i, State 1: %i' % (states[0], states[1])
#     if states[0] == "complete" and states[1] == "complete":
#       sim.add_state((states[0], states[1]))
#       return True, None
#     else:
#       sim.add_state((states[0], states[1]))
#       return False, None

#   sim = simulator.Simulator(threads, pred)
#   sim.run_sim()
#   sim.visualize()

if __name__ == '__main__':
  main()
