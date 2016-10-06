import asyncio
import sys
import struct
from threading import Thread, current_thread
import queue

class Message(object):
  def __init__(self, seq, type, cmd, args, data):
    self.seq = seq
    self.type = type
    self.cmd = cmd
    self.args = args
    self.data = data

async def donothing(q, loop):
  await q.get()

def ntrthreadloop_setup(loop, q):
  asyncio.set_event_loop(loop)
  loop.run_until_complete(
    asyncio.ensure_future(donothing(q, loop), loop=loop)
  )
  print("stopping thread")
  current_thread().stop()

class Client(object):

  def connect(*args):
    ntrloop = asyncio.new_event_loop()
    asyncqueue = asyncio.Queue(1, loop=ntrloop)
    ntrthread = Thread(target=ntrthreadloop_setup, args=(ntrloop,asyncqueue))
    ntrthread.start()

    async def doasync(loop, q, host, port, log=sys.stdout.write):
      client = Client(
        loop,
        await asyncio.open_connection(
          host, port, loop=loop
        ),
        log
      )
      seq = client.seqctr
      client.seqctr += 1000
      await client.sendHeartbeat_async(seq)
      q.put(client)

    threadqueue = queue.Queue(1)
    ntrloop.call_soon_threadsafe(asyncio.ensure_future, doasync(ntrloop, threadqueue, *args))
    return threadqueue.get()


  def __init__(self, loop, conn, log):
    self.loop = loop
    self.conn = conn
    #with open("/dev/urandom", "rb") as fd:
    #  _seq, = struct.unpack("@I", fd.read(4))
    #  if _seq > 1000:
    #    self.seqctr = _seq
    #  else:
    #    self.seqctr = 1001
    self.seqctr = 0
    self.seqs = {}
    self.log = log


    self.backtask = asyncio.ensure_future(self.background(), loop=self.loop)


  async def dosync_ntrthread(self, q, task):
    q.put(await task)

  def dosync(self, task):
    q = queue.Queue(1)
    self.loop.call_soon_threadsafe(asyncio.ensure_future, self.dosync_ntrthread(q, task))
    return q.get()


  def log_message(self, msg):
    #patch up later w/ reg fixes
    if msg.data != None:
      if msg.data == "rtRecvSocket failed: 00000000":
        self.log("connection established!")
      else:
        self.log(msg.data.decode())
    else:
      self.log("got \"unknown\" message with seq: {}, type: {}, cmd: {}\n".format(
        msg.seq, msg.type, msg.cmd
      ))

  async def background(self):
    print("background started!")
    while True:
      reader, _ = self.conn
      try:
        header = await reader.readexactly(84)
      except:
        if reader.at_eof():
          print("at_eof!")
          ntrqueue.put(None)
          return
        continue

      print(header)
      magic, seq, type, cmd = struct.unpack("<IIII", header[:16])
      print(hex(magic))
      if (magic != 0x12345678):
        print("bad magic value: " + magic)
        continue
      args = struct.unpack("<" + "I"*16, header[16:80])
      size,  = struct.unpack("<I", header[80:])
      print(size)
      data = None
      if size != 0:
        data = await reader.readexactly(size)
      msg = Message(seq, type, cmd, args, data)
      if seq in self.seqs:
        try:
          await self.seqs[seq].put(msg)
        except asyncio.QueueFull:
          pass
        except:
          print("An error occurred.")
      else:
        self.log_message(msg)

  def disconnect(self):
    reader, writer = self.conn
    writer.close()

  async def sendPacket_async(self, seq, type, cmd, args=[], data=None):
    send_args = args + ([0]*(16-len(args)))
    header = struct.pack("<IIII", 0x12345678, seq, type, cmd)
    header += struct.pack("<" + "I"*16, *send_args)

    if data is str:
      _data= data.encode()
      msg = header + _data + struct.pack("<I", len(_data))
    elif data is bytes:
      msg = header + data + struct.pack("<I", len(data))
    else:
      msg = header + struct.pack("<I", 0)

    _, writer = self.conn
    writer.write(msg)

  def sendPacket(self, *args):
    return self.dosync(self.sendPacket_async(*args))

  async def sendHeartbeat_async(self, seq):
    print("sending heartbeat")
    asyncio.ensure_future(self.sendPacket_async(seq, 0x0, 0x0, []))

  def sendHeartbeat(self):
    seq = self.seqctr
    self.seqctr += 1000
    self.dosync(self.sendHeartbeat_async(seq))

  async def readMemory_async(self, pid, address, length, filename=None):
    q = asyncio.Queue(1, loop=self.loop)
    seq = self.seqctr
    self.seqctr += 1000

    self.seqs[seq] = q
    asyncio.ensure_future(self.sendPacket_async(seq, 0x0, 0x9, [pid, address, length]))
    msg = await q.get()
    del self.seqs[seq]

    #maybe log metadata here?

    return msg.data

  def readMemory(self, *args):
    return self.dosync(self.readMemory_async(*args))


def connect(*args):
  ntrloop = asyncio.new_event_loop()
  self.queue = asyncio.Queue(1, loop=self.loop)
  self.thread = Thread(target=ntrthreadloop_setup, args=(self.thread,self.loop,self.queue))
  self.thread.start()

  async def doasync(q, host, port, log=sys.stdout.write):
    q.put(await task)
    client = Client(
      ntrloop,
      await asyncio.open_connection(
        host, port, loop=ntrloop
      ),
      log
    )
    await client.sendHeartbeat_async()
    q.put(client)

  q = queue.Queue(1)
  ntrloop.call_soon_threadsafe(asyncio.ensure_future, doasync(q, *args))
  return q.get()


__all__ = ["Client"]
