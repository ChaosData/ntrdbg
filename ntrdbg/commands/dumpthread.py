import asyncio

from ..clientbase import ClientBase

class DumpThread(ClientBase):
  async def dump_thread_async(self, pid):
    await self.heartbeat_async()

    seq = self.seqctr
    self.seqctr += 1000

    await self.send_packet_async(seq, 0x0, 0x7, [pid])

    res = await self.get_response_async()
    data = res.decode('utf-8')

    ret = {
      "pid": pid,
      "threads": []
    }
    lines = [line for line in data.split('\n') if line != ""]
    for i in range(len(lines)):
      idx = i // 8
      if len(ret["threads"]) == idx:
        ret["threads"].append({})
      if i % 8 == 0 and lines[i].startswith("tid:"):
        ret["threads"][idx]["tid"] = int(lines[i].split("tid:")[1].strip(), 16)
      elif i % 8 == 2 and len(lines[i]) > 32:
        vals = [line for line in lines[i].split(" ") if line != ""]
        ret["threads"][idx]["reg"] = {
          "r0": vals[7],
          "r1": vals[8],
          "r2": vals[9],
          "r3": vals[10],
          "r4": vals[3],
          "r5": vals[4],
          "r6": vals[5],
          "r7": vals[26],
          "r8": vals[27],
          "r9": vals[28],
          "r10": vals[29],
          "r11": vals[30],
          "r12": vals[11],
          "sp": vals[13],
          "lr": vals[14],
          "pc": vals[15]
        } # r6 is repeated for some reason
        for key in ret["threads"][idx]["reg"]:
          ret["threads"][idx]["reg"][key] =\
            int(ret["threads"][idx]["reg"][key], 16)
        ret["threads"][idx]["unknown"] = {
          0: vals[0],
          1: vals[1],
          2: vals[2],
          6: vals[6],
          12: vals[12],
          16: vals[16],
          17: vals[17],
          18: vals[18],
          19: vals[19],
          20: vals[20],
          21: vals[21],
          22: vals[22],
          23: vals[23],
          24: vals[24],
          31: vals[31]
        }
        for key in ret["threads"][idx]["unknown"]:
          ret["threads"][idx]["unknown"][key] =\
            int(ret["threads"][idx]["unknown"][key], 16)
    return ret



  def dump_thread(self, *args):
    return self.dosync(self.dump_thread_async(*args))
