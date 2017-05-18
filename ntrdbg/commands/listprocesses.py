import asyncio

from ..clientbase import ClientBase

class ListProcesses(ClientBase):
  async def list_processes_async(self):
    await self.heartbeat_async()

    seq = self.seqctr
    self.seqctr += 1000

    await self.send_packet_async(seq, 0x0, 0x5)

    res = await self.get_response_async()
    data = res.decode('utf-8')

    ret = {}
    lines = [line for line in data.split('\n') if line != ""]
    for line in lines:
      if line.startswith("pid:"):
        pid, pname, tid, kpobj = line.split(',')
        pid = int(pid.split(':')[1].strip(),16)
        pname = pname.split(':')[1].strip()
        tid = int(tid.split(':')[1].strip(),16)
        kpobj = int(kpobj.split(':')[1].strip(),16)
        ret[pid] = {
          "pid": pid,
          "pname": pname,
          "tid": tid,
          "kpobj": kpobj
        }

    return ret


  def list_processes(self):
    return self.dosync(self.list_processes_async())
