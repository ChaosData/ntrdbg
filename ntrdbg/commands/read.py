import asyncio

from ..clientbase import ClientBase

class Read(ClientBase):
  async def read_async(self, pid, address, length, filename=None, append=False):
    await self.heartbeat_async()

    q = asyncio.Queue(1, loop=self.loop)
    seq = self.seqctr
    self.seqctr += 1000

    self.seqs[seq] = q
    await self.send_packet_async(seq, 0x0, 0x9, [pid, address, length])
    msg = await q.get()
    del self.seqs[seq]

    res = await self.get_response_async() # eats up a "finished" message
    if res != b"finished":
      print("did not recieve a b'finished' message, got: {}".format(res))

    if filename != None:
      with open(filename, "ab" if append else "wb") as fd:
        fd.write(msg.data)
      return None
    else:
      return msg.data

  def read(self, *args):
    return self.dosync(self.read_async(*args))
