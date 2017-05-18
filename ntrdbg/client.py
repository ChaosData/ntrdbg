import asyncio

from .commands import *


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

    self.backtask = asyncio.ensure_future(self.background(), loop=self.loop)

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
