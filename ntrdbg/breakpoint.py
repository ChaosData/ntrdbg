INFINITE_LOOP = b"\xfe\xff\xff\xea"

async def default_task(bp, reg):
  print("breakpoint hit pid: " + bp.pid + ", address: " + reg["pc"])

class Breakpoint(object):
  def __init__(self, pid, address, orig, onhit_task=None):
    self.pid = pid
    self.address = address
    self.orig = orig
    self.hit = False
    if onhit_task is None:
      self.onhit_task = default_task
    else:
      self.onhit_task = onhit_task


