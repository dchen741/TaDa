import puzzle
import simulator

def main():
  str1 = """for x in xrange(100):
              import time
              time.sleep(0.1)
              controller.update_state(thread_id, x)"""
  str2 = [ 'for x in xrange(100):'
         , '     import time'
         , '     time.sleep(0.1)'
         , '     controller.update_state(thread_id, x)']
  code = [str1, '\n'.join(str2)]
  threads = map(mk_thread, code)

  def pred(states):
    if states[0] == 99 and states[1] == 99:
      print 'DONE!'
      return True, None
    else:
      if states[0] != states[1]:
        print 'State 0: %i, State 1: %i' % (states[0], states[1])
      return False, None

  sim = simulator.Simulator(threads, pred)
  sim.run_sim()

def mk_thread(s):
  def f(controller, thread_id):
    exec s in globals(), locals()
  return f

if __name__ == '__main__':
  main()