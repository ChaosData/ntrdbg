# ntrdbg
*A better debugger client for NTR CFW's "debugger."*

## Example Usage

***Note:*** In-development, debug info is being dumped everywhere!

***Note:*** Heartbeats are not currently forced to run constantly
(I need to interleave them safely). Due to this, connections may time out after
a bit of inactivity, which will also kill the debug server listener.
Just go to the home menu settings and toggle the
"Wireless Communication / NFC" setting off and then on, and reconnect.

```
$ python3.6
Python 3.6.1 (default, May 18 2017, 02:18:45)
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ntrdbg; conn = ntrdbg.connect('192.168.2.15', 8000)
ClientBase __init__ called
sending heartbeat
background started!
got header: b'xV4\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1d\x00\x00\x00'
got seq: 0
got size: 29
b'rtRecvSocket failed: 00000000'
*beat*
>>> conn.list_processes()
sending heartbeat
got header: b'xV4\x12\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
got seq: 1000
got size: 0
None
*beat*
got header: b'xV4\x12\xb8\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x004\x0b\x00\x00'
got seq: 3000
got size: 2868
b'pid: 0x00000000, pname:       fs, tid: 0000000000000000, kpobj: fff75c30\npid: 0x00000001, pname:   loader, tid: 0000000000000000, kpobj: fff75ea0\npid: 0x00000002, pname:       pm, tid: 0000000000000000, kpobj: fff76110\npid: 0x00000003, pname:       sm, tid: 0000000000000000, kpobj: fff76380\npid: 0x00000004, pname:      pxi, tid: 0000000000000000, kpobj: fff765f0\npid: 0x00000005, pname:       ns, tid: 0004013000008002, kpobj: fff76860\npid: 0x00000006, pname:      ptm, tid: 0004013000002202, kpobj: fff76ad0\npid: 0x00000007, pname:      cfg, tid: 0004013000001702, kpobj: fff76d40\npid: 0x00000008, pname:     gpio, tid: 0004013000001b02, kpobj: fff76fb0\npid: 0x00000009, pname:      i2c, tid: 0004013000001e02, kpobj: fff77220\npid: 0x0000000a, pname:      mcu, tid: 0004013000001f02, kpobj: fff77490\npid: 0x0000000b, pname:      pdn, tid: 0004013000002102, kpobj: fff77700\npid: 0x0000000c, pname:      spi, tid: 0004013000002302, kpobj: fff77970\npid: 0x0000000d, pname:       ps, tid: 0004013000003102, kpobj: fff77be0\npid: 0x0000000e, pname:  ErrDisp, tid: 0004003000008a02, kpobj: fff77e50\npid: 0x0000000f, pname:     menu, tid: 0004003000008f02, kpobj: fff780c0\npid: 0x00000010, pname:      hid, tid: 0004013000001d02, kpobj: fff78330\npid: 0x00000011, pname:    codec, tid: 0004013000001802, kpobj: fff785a0\npid: 0x00000012, pname:      dsp, tid: 0004013000001a02, kpobj: fff78810\npid: 0x00000013, pname:       am, tid: 0004013000001502, kpobj: fff78a80\npid: 0x00000014, pname:      gsp, tid: 0004013000001c02, kpobj: fff78cf0\npid: 0x00000015, pname:      qtm, tid: 0004013000004202, kpobj: fff78f60\npid: 0x00000016, pname:   camera, tid: 0004013000001602, kpobj: fff791d0\npid: 0x00000017, pname:     csnd, tid: 0004013000002702, kpobj: fff79440\npid: 0x00000018, pname:      mic, tid: 0004013000002002, kpobj: fff796b0\npid: 0x00000019, pname:       ir, tid: 0004013000003302, kpobj: fff79920\npid: 0x0000001a, pname:      nwm, tid: 0004013000002d02, kpobj: fff79b90\npid: 0x0000001b, pname:   socket, tid: 0004013000002e02, kpobj: fff79e00\npid: 0x0000001c, pname:     http, tid: 0004013000002902, kpobj: fff7a070\npid: 0x0000001d, pname:      ssl, tid: 0004013000002f02, kpobj: fff7a2e0\npid: 0x0000001e, pname:     cecd, tid: 0004013000002602, kpobj: fff7a550\npid: 0x0000001f, pname:  friends, tid: 0004013000003202, kpobj: fff7a7c0\npid: 0x00000020, pname:       ac, tid: 0004013000002402, kpobj: fff7aa30\npid: 0x00000021, pname:     boss, tid: 0004013000003402, kpobj: fff7aca0\npid: 0x00000022, pname:      act, tid: 0004013000003802, kpobj: fff7af10\npid: 0x00000023, pname:     news, tid: 0004013000003502, kpobj: fff7b180\npid: 0x00000024, pname:      ndm, tid: 0004013000002b02, kpobj: fff7b3f0\npid: 0x00000025, pname:      nim, tid: 0004013000002c02, kpobj: fff7b660\npid: 0x00000026, pname:      dlp, tid: 0004013000002802, kpobj: fff7b8d0\nend of process list.\n'
{0: {'pid': 0, 'pname': 'fs', 'tid': 0, 'kpobj': 4294401072}, 1: {'pid': 1, 'pname': 'loader', 'tid': 0, 'kpobj': 4294401696}, 2: {'pid': 2, 'pname': 'pm', 'tid': 0, 'kpobj': 4294402320}, 3: {'pid': 3, 'pname': 'sm', 'tid': 0, 'kpobj': 4294402944}, 4: {'pid': 4, 'pname': 'pxi', 'tid': 0, 'kpobj': 4294403568}, 5: {'pid': 5, 'pname': 'ns', 'tid': 1127205576933378, 'kpobj': 4294404192}, 6: {'pid': 6, 'pname': 'ptm', 'tid': 1127205576909314, 'kpobj': 4294404816}, 7: {'pid': 7, 'pname': 'cfg', 'tid': 1127205576906498, 'kpobj': 4294405440}, 8: {'pid': 8, 'pname': 'gpio', 'tid': 1127205576907522, 'kpobj': 4294406064}, 9: {'pid': 9, 'pname': 'i2c', 'tid': 1127205576908290, 'kpobj': 4294406688}, 10: {'pid': 10, 'pname': 'mcu', 'tid': 1127205576908546, 'kpobj': 4294407312}, 11: {'pid': 11, 'pname': 'pdn', 'tid': 1127205576909058, 'kpobj': 4294407936}, 12: {'pid': 12, 'pname': 'spi', 'tid': 1127205576909570, 'kpobj': 4294408560}, 13: {'pid': 13, 'pname': 'ps', 'tid': 1127205576913154, 'kpobj': 4294409184}, 14: {'pid': 14, 'pname': 'ErrDisp', 'tid': 1126106065308162, 'kpobj': 4294409808}, 15: {'pid': 15, 'pname': 'menu', 'tid': 1126106065309442, 'kpobj': 4294410432}, 16: {'pid': 16, 'pname': 'hid', 'tid': 1127205576908034, 'kpobj': 4294411056}, 17: {'pid': 17, 'pname': 'codec', 'tid': 1127205576906754, 'kpobj': 4294411680}, 18: {'pid': 18, 'pname': 'dsp', 'tid': 1127205576907266, 'kpobj': 4294412304}, 19: {'pid': 19, 'pname': 'am', 'tid': 1127205576905986, 'kpobj': 4294412928}, 20: {'pid': 20, 'pname': 'gsp', 'tid': 1127205576907778, 'kpobj': 4294413552}, 21: {'pid': 21, 'pname': 'qtm', 'tid': 1127205576917506, 'kpobj': 4294414176}, 22: {'pid': 22, 'pname': 'camera', 'tid': 1127205576906242, 'kpobj': 4294414800}, 23: {'pid': 23, 'pname': 'csnd', 'tid': 1127205576910594, 'kpobj': 4294415424}, 24: {'pid': 24, 'pname': 'mic', 'tid': 1127205576908802, 'kpobj': 4294416048}, 25: {'pid': 25, 'pname': 'ir', 'tid': 1127205576913666, 'kpobj': 4294416672}, 26: {'pid': 26, 'pname': 'nwm', 'tid': 1127205576912130, 'kpobj': 4294417296}, 27: {'pid': 27, 'pname': 'socket', 'tid': 1127205576912386, 'kpobj': 4294417920}, 28: {'pid': 28, 'pname': 'http', 'tid': 1127205576911106, 'kpobj': 4294418544}, 29: {'pid': 29, 'pname': 'ssl', 'tid': 1127205576912642, 'kpobj': 4294419168}, 30: {'pid': 30, 'pname': 'cecd', 'tid': 1127205576910338, 'kpobj': 4294419792}, 31: {'pid': 31, 'pname': 'friends', 'tid': 1127205576913410, 'kpobj': 4294420416}, 32: {'pid': 32, 'pname': 'ac', 'tid': 1127205576909826, 'kpobj': 4294421040}, 33: {'pid': 33, 'pname': 'boss', 'tid': 1127205576913922, 'kpobj': 4294421664}, 34: {'pid': 34, 'pname': 'act', 'tid': 1127205576914946, 'kpobj': 4294422288}, 35: {'pid': 35, 'pname': 'news', 'tid': 1127205576914178, 'kpobj': 4294422912}, 36: {'pid': 36, 'pname': 'ndm', 'tid': 1127205576911618, 'kpobj': 4294423536}, 37: {'pid': 37, 'pname': 'nim', 'tid': 1127205576911874, 'kpobj': 4294424160}, 38: {'pid': 38, 'pname': 'dlp', 'tid': 1127205576910850, 'kpobj': 4294424784}}
>>> conn.dump_threads(0x00000023)
sending heartbeat
got header: b'xV4\x12\xa0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
got seq: 4000
got size: 0
None
*beat*
got header: b'xV4\x12p\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x01\x00\x00'
got seq: 6000
got size: 378
b'tid: 0x000000a2\npc: 00108e00, lr: 0010032b\n0012f320 00000009 000a8012 0012f320 0010b48c 0010a4b0 000a8012 00000000 00000000 00000000 00000000 00000000 00000000 0fffffbc 0010032b 00108e00 20000010 fffa9f4e 3fe7ffbf 0000fd80 00000000 4f000000 00000000 fffda0c8 60000013 00000000 00000000 00000009 00000009 fff3302c ff51bec8 ff51bdb8 \nrecommend pc:\n00108e00\nrecommend lr:\n0010032b\n'
{'pid': 35, 'threads': [{'tid': 162, 'reg': {'r0': 0, 'r1': 0, 'r2': 0, 'r3': 0, 'r4': 1241888, 'r5': 1094796, 'r6': 1090736, 'r7': 0, 'r8': 9, 'r9': 9, 'r10': 4294127660, 'r11': 4283547336, 'r12': 0, 'sp': 268435388, 'lr': 1049387, 'pc': 1084928}, 'unknown': {0: 1241888, 1: 9, 2: 688146, 6: 688146, 12: 0, 16: 536870928, 17: 4294614862, 18: 1072168895, 19: 64896, 20: 0, 21: 1325400064, 22: 0, 23: 4294811848, 24: 1610612755, 31: 4283547064}}]}
>>> conn.dump_mappings(0x00000023)
sending heartbeat
got header: b'xV4\x12X\x1b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
got seq: 7000
got size: 0
None
*beat*
got header: b'xV4\x12(#\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x93\x00\x00\x00'
got seq: 9000
got size: 147
b'valid memregions:\n00100000 - 00132fff , size: 00033000\n08000000 - 0800ffff , size: 00010000\n0fffe000 - 0fffffff , size: 00002000\nend of memlayout.\n'
{1048576: {'start': 1048576, 'size': 208896, 'end': 1257471}, 134217728: {'start': 134217728, 'size': 65536, 'end': 134283263}, 268427264: {'start': 268427264, 'size': 8192, 'end': 268435455}}
>>> conn.read(0x00000023, 0x100020, 16)
sending heartbeat
got header: b"xV4\x12\x10'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
got seq: 10000
got size: 0
None
*beat*
got header: b'xV4\x12\xf8*\x00\x00\x00\x00\x00\x00\t\x00\x00\x00#\x00\x00\x00 \x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'
got seq: 11000
got size: 16
b'Z#\x00\xea\x14\x00\x9f\xe5\x14\x10\x9f\xe5\x00 \xa0\xe3'
got header: b'xV4\x12\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00'
got seq: 12000
got size: 8
b'finished'
b'Z#\x00\xea\x14\x00\x9f\xe5\x14\x10\x9f\xe5\x00 \xa0\xe3'
>>> conn.write(0x00000023, 0x100020, b"AAAAA")
sending heartbeat
got header: b'xV4\x12\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
got seq: 13000
got size: 0
None
*beat*
got header: b'xV4\x12\x98:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00'
got seq: 15000
got size: 8
b'finished'
>>> conn.read(0x00000023, 0x100020, 16)
sending heartbeat
got header: b'xV4\x12\x80>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
got seq: 16000
got size: 0
None
*beat*
got header: b'xV4\x12hB\x00\x00\x00\x00\x00\x00\t\x00\x00\x00#\x00\x00\x00 \x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'
got seq: 17000
got size: 16
b'AAAAA\x00\x9f\xe5\x14\x10\x9f\xe5\x00 \xa0\xe3'
got header: b'xV4\x12PF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00'
got seq: 18000
got size: 8
b'finished'
b'AAAAA\x00\x9f\xe5\x14\x10\x9f\xe5\x00 \xa0\xe3'
```
