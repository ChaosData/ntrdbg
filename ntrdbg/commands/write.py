import asyncio

from ..clientbase import ClientBase

class Write(ClientBase):
  async def write_async(self, pid, address, buf):
    await self.lock.acquire()

    # errorq = asyncio.Queue(1, loop=self.loop)
    seq = self.seqctr
    # print("write w/ seq: {}".format(seq))
    self.seqctr += 1000

    #self.seqs[seq] = errorq
    # asyncio.ensure_future(
    await self.send_packet_async(seq, 0x1, 0xa, [pid, address, len(buf)], buf)
    # )

    # msg = await errorq.get()
    # del self.seqs[seq]
    #
    # # maybe log metadata here?
    # print("error?: {}".format(msg))
    # # return msg.data
    #
    # if msg != "error":
    #   res = await self.get_response_async()
    #   print("got: {}".format(res))

    # error = errorq.get()
    # res = self.get_response_async()

    # print("error: {}".format(error))
    # print("res: {}".format(res))
    #
    # done, pending = await asyncio.wait(
    #   [error, res],
    #   return_when=asyncio.FIRST_COMPLETED
    # )
    # print("done: {}".format(done))
    # print("pending: {}".format(pending))
    #
    # # ??? both are done?
    # done = done.pop()
    # pending = pending.pop()
    #
    # del self.seqs[seq]
    # print("done: {}".format(done))
    # print("pending: {}".format(pending))
    #
    # if done._coro == error:
    #   print("done == error")
    # if done._coro == res:
    #   print("done == res")
    # if pending._coro == error:
    #   print("pending == error")
    # if pending._coro == res:
    #   print("pending == res")
    #
    # return [done, pending]

    res = await self.get_response_async()
    self.lock.release()

    if res != b"finished":
      print("did not recieve a b'finished' message, got: {}".format(res))

    return None

  def write(self, *args):
    return self.dosync(self.write_async(*args))
