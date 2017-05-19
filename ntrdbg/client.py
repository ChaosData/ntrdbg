import asyncio

from .commands import *
from .breakpoint import *

from typing import List

class Client(Read, Write, ListProcesses, DumpThreads, DumpMappings):
  def __init__(self, loop, asyncqueue, conn, log):
    super().__init__()
    self.loop = loop
    self.asyncqueue = asyncqueue
    self.conn = conn
    # with open("/dev/urandom", "rb") as fd:
    #  _seq, = struct.unpack("@I", fd.read(4))
    #  if _seq > 1000:
    #    self.seqctr = _seq
    #  else:
    #    self.seqctr = 1001
    self.log = log

    self.dbg_lock = asyncio.Lock()
    self.breakpoints = {}

    self.backtask = asyncio.ensure_future(self.background(), loop=self.loop)
    self.beattask = asyncio.ensure_future(self.beat(), loop=self.loop)

  def __enter__(self):
    pass

  def __exit__(self, typ, val, ex):
    pass

  def __del__(self):
    # print("__del__")
    self.disconnect()

  def delete(self):
    # print("delete")
    self.disconnect()

  async def beat(self):
    while self.conn is not None:
      await asyncio.sleep(1)
      if await self.heartbeat_async(False):
        break
    await asyncio.sleep(1)
    await self.asyncqueue.put(None)

  async def add_breakpoint_async(self, pid, address, onhit_task=None):
    await self.dbg_lock.acquire()

    bpm = {}
    if pid in self.breakpoints:
      bpm = self.breakpoints[pid]
    else:
      self.breakpoints[pid] = bpm
    orig = await self.read_async(pid, address, 4)

    bpm[address] = Breakpoint(pid, address, orig, onhit_task)
    await self.write_async(pid, address, INFINITE_LOOP)

    self.dbg_lock.release()

  def add_breakpoint(self, *args):
    return self.dosync(self.add_breakpoint_async(*args))

  async def remove_breakpoint_async(self, pid, address):
    await self.dbg_lock.acquire()

    bpm = {}
    if pid in self.breakpoints:
      bpm = self.breakpoints[pid]
    else:
      self.breakpoints[pid] = bpm
    if address in bpm:
      bp = bpm.pop(address)
      await self.write_async(pid, address, bp.orig)

    self.dbg_lock.release()

  def remove_breakpoint(self, *args):
    return self.dosync(self.remove_breakpoint_async(*args))

  async def breakpoint_scanner(self):
    while self.conn is not None:
      await asyncio.sleep(1)
      await self.dbg_lock.acquire()

      for pid in self.breakpoints:
        bpm = self.breakpoints[pid]
        td = await self.dump_threads_async(pid)
        for idx in td["threads"]:
          pc = td["threads"][idx]["reg"]["pc"]
          for address in bpm:
            bp: Breakpoint = bpm[address]
            if not bp.hit:
              if bp.address == pc:
                bp.hit = True
                await bp.onhit_task(bp, td["threads"][idx]["reg"])

      self.dbg_lock.release()



