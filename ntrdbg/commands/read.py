import asyncio

from ..clientbase import ClientBase


class Read(ClientBase):
  async def read_async(self, pid, address, length, filename=None):
    await self.heartbeat_async()

    q = asyncio.Queue(1, loop=self.loop)
    seq = self.seqctr
    self.seqctr += 1000

    self.seqs[seq] = q
    asyncio.ensure_future(
      self.send_packet_async(seq, 0x0, 0x9, [pid, address, length])
    )
    msg = await q.get()
    del self.seqs[seq]

    # maybe log metadata here?
    return msg.data

  def read(self, *args):
    return self.dosync(self.read_async(*args))
