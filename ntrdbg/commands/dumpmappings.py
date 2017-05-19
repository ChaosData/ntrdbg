import asyncio

from ..clientbase import ClientBase

class DumpMappings(ClientBase):
  async def dump_mappings_async(self, pid):
    await self.packet_lock.acquire()

    seq = self.seqctr
    self.seqctr += 1000

    await self.send_packet_async(seq, 0x0, 0x8, [pid])

    res = await self.get_response_async()
    self.packet_lock.release()

    data = res.decode('utf-8')
    ret = {}
    lines = [line for line in data.split('\n') if line != ""]
    for line in lines:
      if "valid" in line or "end of" in line:
        continue
      #00100000 - 00132fff , size: 00033000
      rg,sz = line.split(',')
      start, end = rg.split('-')
      sz = int(sz.split(':')[1].strip(), 16)
      start = int(start.strip(), 16)
      end = int(end.strip(), 16)
      ret[start] = {
        "start": start,
        "size": sz,
        "end": end
      }
    return ret

  def dump_mappings(self, pid):
    return self.dosync(self.dump_mappings_async(pid))
