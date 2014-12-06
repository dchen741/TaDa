import threading
import time
import os

class Simulator:
  def __init__(self, threads, predicate, semaphores = [], poll_rate=0.01, clean_fun=None):
    self.threads    = threads
    self.predicate  = predicate
    self.semaphores = semaphores
    self.states     = [None for _ in threads]
    self.mutex      = threading.Lock()
    self.poll_rate  = poll_rate 
    self.clean_fun  = clean_fun
    self.statesList = []

  def run_sim(self):
    threads = self.spin_threads()
    message = self.poll_loop()
    self.cleanup(threads)
    return message

  def spin_threads(self):
    id_n = 0
    threads = []
    for target in self.threads:
      t = threading.Thread(target=target, args =(self, id_n))
      t.daemon = True
      threads.append(t)
      id_n += 1
    map(lambda t: t.start(), threads)

  def poll_loop(self):
    while True:
      self.mutex.acquire()
      success, failure, message = self.predicate(self.states)
      self.mutex.release()
      if success:
        return True, message
      if failure:
        return False, message
      time.sleep(self.poll_rate)

  def update_state(self, thread_id, state):
    self.mutex.acquire()
    self.states[thread_id] = state
    self.add_state(self.states)
    self.mutex.release()

  def cleanup(self, threads):
    if self.clean_fun:
      self.clean_fun()

  def add_state(self, state):
    self.statesList.append(state)

  def visualize(self):
    i=0
    movement = "n"
    while movement != "-next":
      os.system('clear')
      states = self.statesList[i]
      print "Frame: " + str(i)
      for x in range(len(states)):
          print "State " + str(x) + ": " + str(states[x])
      movement = raw_input("\nHit Enter to go to the next snapshot.\nType p + Enter to go the the last snapshot. \nTo move on, type -next.\n")
      if movement == "":
        i = i + 1
        if i >= len(self.statesList):
          i = len(self.statesList)-1
      elif movement == "p":
        i = i - 1
        if i < 0:
          i = 0
