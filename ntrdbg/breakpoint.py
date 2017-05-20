from .pretty import *

INFINITE_LOOP_ARM = b"\xfe\xff\xff\xea"
INFINITE_LOOP_THUMB = b"\xfe\xe7"

async def default_task(conn, bp, reg):
  print("\nBreakpoint hit in pid: {}".format(bp.pid))
  print_regs(reg)
  data = await conn.read_async(bp.pid, reg["pc"], 40)  # fix mapping boundary

  if not bp.is_thumb:
    print_ins_arm(data, bp.address)
  else:
    print_ins_thumb(data, bp.address)



class Breakpoint(object):
  def __init__(self, pid, address, is_thumb, orig, onhit_task=None):
    self.pid = pid
    self.address = address
    self.is_thumb = is_thumb
    self.orig = orig
    self.hit = False
    self.onhit_task = onhit_task

  async def call_task_async(self, *args):
    if self.onhit_task is None:
      try:
        await default_task(*args)
      except Exception as e:
        print("error: " + str(e))
    else:
      try:
        await self.onhit_task(*args)
      except Exception as e:
        print("error: " + str(e))
