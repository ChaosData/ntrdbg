import asyncio

from ..clientbase import ClientBase

'''
public void sendWriteMemPacket(UInt32 addr, UInt32 pid, byte[] buf) {
  UInt32[] args = new UInt32[16];
  args[0] = pid;
  args[1] = addr;
  args[2] = (UInt32) buf.Length;
  sendPacket(1, 10, args, args[2]);
  netStream.Write(buf, 0, buf.Length);
}
'''


class Write(ClientBase):
  async def write_async(self, pid, address, buf):
    await self.heartbeat_async()

    # q = asyncio.Queue(1, loop=self.loop)
    seq = self.seqctr
    self.seqctr += 1000

    # self.seqs[seq] = q
    asyncio.ensure_future(
      self.send_packet_async(seq, 0x1, 0xa, [pid, address, len(buf)], buf)
    )
    # msg = await q.get()
    # del self.seqs[seq]

    # maybe log metadata here?
    # return msg.data

  def write(self, *args):
    return self.dosync(self.write_async(*args))
