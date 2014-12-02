import threading
import time

class Simulator:
  def __init__(self, threads, predicate, poll_rate=0.01, clean_fun=None):
    self.threads   = threads
    self.predicate = predicate
    self.states    = [None for _ in threads]
    self.mutex     = threading.Lock()
    self.poll_rate = poll_rate 
    self.clean_fun = clean_fun

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
      success, messgae = self.predicate(self.states)
      self.mutex.release()
      if success:
        return messgae
      time.sleep(self.poll_rate)

  def update_state(self, thread_id, state):
    self.mutex.acquire()
    self.states[thread_id] = state
    self.mutex.release()

  def cleanup(self, threads):
    if self.clean_fun:
      self.clean_fun()
