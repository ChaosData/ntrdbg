#!/usr/bin/env python3.5

import asyncio
import sys
from threading import Thread
import queue
import atexit

from .client import Client


async def donothing(q):
  await q.get()
  # print("done doing nothing")


def ntrthreadloop_setup(loop, asyncqueue):
  asyncio.set_event_loop(loop)
  loop.run_until_complete(
    asyncio.ensure_future(donothing(asyncqueue), loop=loop)
  )

def connect(*args):
  ntrloop = asyncio.new_event_loop()
  asyncqueue = asyncio.Queue(1, loop=ntrloop)
  ntrthread = Thread(target=ntrthreadloop_setup, args=(ntrloop, asyncqueue))
  ntrthread.setDaemon(True)
  ntrthread.start()

  async def doasync(retq, loop, asyncq, host, port, log=sys.stdout.write):
    conn = None
    try:
      conn = await asyncio.wait_for(
        asyncio.open_connection(
          host, port, loop=loop
        ),
        timeout=2
      )
    except asyncio.TimeoutError:
      sys.stderr.write("Failed to connect to debugger daemon.\n")
    except Exception as ex:
      sys.stderr.write("An error ocurred: {}\n".format(ex))

    if conn is not None:
      c = Client(loop, asyncq, conn, log)
      # seq = c.seqctr
      # c.seqctr += 1000
      retq.put(c)
    else:
      retq.put(None)
      await asyncq.put(None)
      # print(len(asyncio.Task.all_tasks(loop)))

  threadqueue = queue.Queue(1)
  ntrloop.call_soon_threadsafe(
    asyncio.ensure_future,
    doasync(threadqueue, ntrloop, asyncqueue, *args)
  )
  ret = threadqueue.get()
  if ret is None:
    # print(asyncio.Task.all_tasks(ntrloop))
    # print(len(asyncio.Task.all_tasks(ntrloop)))
    ntrloop.stop()
  else:
    atexit.register(ret.delete)
  return ret


__all__ = ["connect"]

# if __name__ == "__main__":
#   import code
#   conn = connect('192.168.2.15', 8000)
#   code.interact(local=locals())
