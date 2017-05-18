import asyncio
import queue
import struct

from .message import Message


async def dosync_ntrthread(q, task):
  q.put(await task)

class ClientBase(object):
  def __init__(self):
    print("ClientBase __init__ called")
    self.seqctr = 0
    self.seqs = {}

    self.loop = None
    self.asyncqueue = None
    self.conn = None
    self.log = None

  def dosync(self, task):
    q = queue.Queue(1)
    self.loop.call_soon_threadsafe(
      asyncio.ensure_future, dosync_ntrthread(q, task)
    )
    return q.get()

  def log_message(self, msg):
    # patch up later w/ reg fixes
    if msg.data is not None:
      if msg.data == "rtRecvSocket failed: 00000000":
        self.log("connection established!")
      else:
        self.log(msg.data.decode())
    else:
      self.log(
        "got \"unknown\" message with "
        "seq: {}, type: {}, cmd: {}\n".format(
          msg.seq, msg.type, msg.cmd
        )
      )

  async def background(self):
    print("background started!")
    while True:
      reader, _ = self.conn
      try:
        header = await reader.readexactly(84)
      # except asyncio.IncompleteReadError:
      #        print("ffffff")
      #        continue
      except Exception as e:
        if reader.at_eof():
          print("at_eof!")
          await self.asyncqueue.put(None)
          return
        else:
          print("error: {}".format(e))
          if str(e) == '[Errno 32] Broken pipe':
            print("connection borked")
            await self.disconnect_async()
            keys = self.seqs.keys()
            for key in keys:
              q = self.seqs[key]
              await q.put(Message(0,0,0,0, "error")) # fix this up

            # await self.asyncqueue.put(None)
            print("???")
            return
        continue

      print("got header: {}".format(header))
      magic, seq, typ, cmd = struct.unpack("<IIII", header[:16])
      if magic != 0x12345678:
        print("bad magic value: " + magic)
        continue
      print("got seq: {}".format(seq))
      args = struct.unpack("<" + "I" * 16, header[16:80])
      size, = struct.unpack("<I", header[80:])
      print("got size: {}".format(size))
      data = None
      if size != 0:
        data = await reader.readexactly(size)
      print(data)
      msg = Message(seq, typ, cmd, args, data)
      if seq in self.seqs:
        try:
          await self.seqs[seq].put(msg)
        except asyncio.QueueFull:
          print("queue full")
          pass
        except Exception as ex:
          print("An error occurred: {}".format(ex))
      else:
        print("not in seqs")
        self.log_message(msg)

  async def disconnect_async(self):
    if self.conn is not None:
      reader, writer = self.conn
      writer.close()
      reader.feed_eof()
      self.conn = None

  # note: this can be called multiple times depending on how threads/process are
  #      cleaned up.
  def disconnect(self):
    if self.conn is not None:
      self.dosync(self.disconnect_async())

  async def send_packet_async(self, seq, typ, cmd, args=None, data=None):
    if args is None:
      args = []
    send_args = args + ([0] * (16 - len(args)))
    header = struct.pack("<IIII", 0x12345678, seq, typ, cmd)
    # print(send_args)
    header += struct.pack("<" + "I" * 16, *send_args)

    # print(header)
    msg = b''
    _data = None
    if type(data) is str:
      _data = data.encode()
      msg += header + struct.pack("<I", len(_data))# + _data
    elif type(data) is bytes:
      _data = data
      msg += header + struct.pack("<I", len(data))# + data
    else:
      msg += header + struct.pack("<I", 0)
    # print(msg)
    _, writer = self.conn
    writer.write(msg)
    # need to have some sort of pause here to check if an error was returned b/c
    # the header was disliked for some reason

    # if _data is not None:
    #   q = self.seqs[seq]
    #
    #   try:
    #     res = await asyncio.wait_for(
    #       q.get(),
    #       timeout=20
    #     )
    #     print("error: {}".format(res.data))
    #     await q.put(res.data)
    #   except asyncio.TimeoutError:
    #     print("timed out")
    #     writer.write(_data)
    #     await q.put(None)
    #   except Exception as ex:
    #     print("???: {}".format(ex))
    if _data is not None:
      writer.write(_data)

  def send_packet(self, *args):
    return self.dosync(self.send_packet_async(*args))

  async def heartbeat_async(self, output=True):
    if output:
      print("sending heartbeat")

    q = asyncio.Queue(1, loop=self.loop)
    seq = self.seqctr
    self.seqctr += 1000

    self.seqs[seq] = q
    asyncio.ensure_future(self.send_packet_async(seq, 0x0, 0x0, []))
    await q.get()
    del self.seqs[seq]
    if output:
      print("*beat*")

  def heartbeat(self, *args):
    self.dosync(self.heartbeat_async(*args))

  async def get_response_async(self):
    if self.conn is None:
      return None

    q = asyncio.Queue(1, loop=self.loop)
    seq = self.seqctr
    self.seqctr += 1000

    self.seqs[seq] = q
    asyncio.ensure_future(self.send_packet_async(seq, 0x0, 0x0, []))
    msg = await q.get()
    del self.seqs[seq]
    return msg.data

  def get_response(self):
    self.dosync(self.get_response_async())
