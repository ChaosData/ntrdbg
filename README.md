# ntrdbg
*A better debugger client for NTR CFW's "debugger."*

## Example Usage

***Note:*** In-development, debug info may result in blindness.

***Note:*** The server is super unstable, if failing to connect, go to the home
menu settings and toggle the "Wireless Communication / NFC" setting off and
then on, and reconnect.

```
$ python3.6
Python 3.6.1 (default, May 18 2017, 02:18:45)
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ntrdbg; conn = ntrdbg.connect('192.168.2.15', 8000)
>>> conn.list_processes()
{0: {'pid': 0, 'pname': 'fs', 'tid': 0, 'kpobj': 4294401072}, 1: {'pid': 1, 'pname': 'loader', 'tid': 0, 'kpobj': 4294401696}, 2: {'pid': 2, 'pname': 'pm', 'tid': 0, 'kpobj': 4294402320}, 3: {'pid': 3, 'pname': 'sm', 'tid': 0, 'kpobj': 4294402944}, 4: {'pid': 4, 'pname': 'pxi', 'tid': 0, 'kpobj': 4294403568}, 5: {'pid': 5, 'pname': 'ns', 'tid': 1127205576933378, 'kpobj': 4294404192}, 6: {'pid': 6, 'pname': 'ptm', 'tid': 1127205576909314, 'kpobj': 4294404816}, 7: {'pid': 7, 'pname': 'cfg', 'tid': 1127205576906498, 'kpobj': 4294405440}, 8: {'pid': 8, 'pname': 'gpio', 'tid': 1127205576907522, 'kpobj': 4294406064}, 9: {'pid': 9, 'pname': 'i2c', 'tid': 1127205576908290, 'kpobj': 4294406688}, 10: {'pid': 10, 'pname': 'mcu', 'tid': 1127205576908546, 'kpobj': 4294407312}, 11: {'pid': 11, 'pname': 'pdn', 'tid': 1127205576909058, 'kpobj': 4294407936}, 12: {'pid': 12, 'pname': 'spi', 'tid': 1127205576909570, 'kpobj': 4294408560}, 13: {'pid': 13, 'pname': 'ps', 'tid': 1127205576913154, 'kpobj': 4294409184}, 14: {'pid': 14, 'pname': 'ErrDisp', 'tid': 1126106065308162, 'kpobj': 4294409808}, 15: {'pid': 15, 'pname': 'menu', 'tid': 1126106065309442, 'kpobj': 4294410432}, 16: {'pid': 16, 'pname': 'hid', 'tid': 1127205576908034, 'kpobj': 4294411056}, 17: {'pid': 17, 'pname': 'codec', 'tid': 1127205576906754, 'kpobj': 4294411680}, 18: {'pid': 18, 'pname': 'dsp', 'tid': 1127205576907266, 'kpobj': 4294412304}, 19: {'pid': 19, 'pname': 'am', 'tid': 1127205576905986, 'kpobj': 4294412928}, 20: {'pid': 20, 'pname': 'gsp', 'tid': 1127205576907778, 'kpobj': 4294413552}, 21: {'pid': 21, 'pname': 'qtm', 'tid': 1127205576917506, 'kpobj': 4294414176}, 22: {'pid': 22, 'pname': 'camera', 'tid': 1127205576906242, 'kpobj': 4294414800}, 23: {'pid': 23, 'pname': 'csnd', 'tid': 1127205576910594, 'kpobj': 4294415424}, 24: {'pid': 24, 'pname': 'mic', 'tid': 1127205576908802, 'kpobj': 4294416048}, 25: {'pid': 25, 'pname': 'ir', 'tid': 1127205576913666, 'kpobj': 4294416672}, 26: {'pid': 26, 'pname': 'nwm', 'tid': 1127205576912130, 'kpobj': 4294417296}, 27: {'pid': 27, 'pname': 'socket', 'tid': 1127205576912386, 'kpobj': 4294417920}, 28: {'pid': 28, 'pname': 'http', 'tid': 1127205576911106, 'kpobj': 4294418544}, 29: {'pid': 29, 'pname': 'ssl', 'tid': 1127205576912642, 'kpobj': 4294419168}, 30: {'pid': 30, 'pname': 'cecd', 'tid': 1127205576910338, 'kpobj': 4294419792}, 31: {'pid': 31, 'pname': 'friends', 'tid': 1127205576913410, 'kpobj': 4294420416}, 32: {'pid': 32, 'pname': 'ac', 'tid': 1127205576909826, 'kpobj': 4294421040}, 33: {'pid': 33, 'pname': 'boss', 'tid': 1127205576913922, 'kpobj': 4294421664}, 34: {'pid': 34, 'pname': 'act', 'tid': 1127205576914946, 'kpobj': 4294422288}, 35: {'pid': 35, 'pname': 'news', 'tid': 1127205576914178, 'kpobj': 4294422912}, 36: {'pid': 36, 'pname': 'ndm', 'tid': 1127205576911618, 'kpobj': 4294423536}, 37: {'pid': 37, 'pname': 'nim', 'tid': 1127205576911874, 'kpobj': 4294424160}, 38: {'pid': 38, 'pname': 'dlp', 'tid': 1127205576910850, 'kpobj': 4294424784}}
>>> conn.dump_threads(38)
{'pid': 38, 'threads': [{'tid': 181, 'reg': {'r0': 0, 'r1': 4293927612, 'r2': 0, 'r3': 0, 'r4': 1159184, 'r5': 4293934224, 'r6': 4294967295, 'r7': 0, 'r8': 4, 'r9': 4, 'r10': 4294127660, 'r11': 85, 'r12': 0, 'sp': 268435344, 'lr': 1092481, 'pc': 1118512}, 'unknown': {0: 4294460581, 1: 4294967295, 2: 0, 6: 4294967295, 12: 0, 16: 536870928, 17: 4294614862, 18: 1072168895, 19: 64896, 20: 0, 21: 620756992, 22: 0, 23: 4294811848, 24: 1610612755, 31: 4283694592}}]}
>>> conn.dump_mappings(38)
{1048576: {'start': 1048576, 'size': 122880, 'end': 1171455}, 134217728: {'start': 134217728, 'size': 24576, 'end': 134242303}, 268431360: {'start': 268431360, 'size': 4096, 'end': 268435455}}
>>> conn.read(38, 268431360, 32)
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> conn.write(38, 268431360, b"AAAAAAAA")
>>> conn.write(38, 268431362, b"BB")
>>> conn.write(38, 268431366, b"ZZ")
>>> conn.read(38, 268431360, 32)
b'AABBAAZZ\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> conn.disconnect()
```
