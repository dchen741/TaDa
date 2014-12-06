def mk_thread(s):
  def f(controller, thread_id):
    exec s in globals(), locals()
  return f
