INFINITE_LOOP = b"\xfe\xff\xff\xea"


async def default_task(conn, bp, reg):
  print("breakpoint hit pid: {}, address: {}".format(bp.pid, reg["pc"]))


class Breakpoint(object):
  def __init__(self, pid, address, orig, onhit_task=None):
    self.pid = pid
    self.address = address
    self.orig = orig
    self.hit = False
    self.onhit_task = onhit_task

  async def call_task_async(self, *args):
    if self.onhit_task is None:
      await default_task(*args)
    else:
      try:
        await self.onhit_task(*args)
      except Exception as e:
        print("error: " + str(e))
