# Notes
The client maintains a thread that actively reads messages sent by the server.

## Message structure

Each of these messages contanins a header, followed by a variable length data
section. The header of a message is 84 bytes, divided into message metadata, a
fixed set of 16 arguments, and a size field specifying the lenght of the data.
The first 4 bytes of the header are the magic number, `0x12345678`.

~~~
      0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f
    +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 00 |     magic     |      seq      |     type      |     cmd       |
    +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 10 |     arg_0     |     arg_1     |     arg_2     |     arg_3     |
    +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 20 |     arg_4     |     arg_5     |     arg_6     |     arg_7     |
    +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 30 |     arg_8     |     arg_9     |     arg_a     |     arg_b     |
    +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 40 |     arg_c     |     arg_d     |     arg_e     |     arg_f     |
    +---+---+---+---+==========================================================+
 50 |     size      |                    ...message data...                    |
    +---+---+---+---+==========================================================+
~~~

## Server Messages
A `cmd` value of `0x0` appears to indicate a UTF-8 textual response with `\n`
line breaks. This is a response to multiple commands (list is a WIP):

* `memlayout`
    * starts with `"valid memregions:"`
* `listthread`
    * starts with `"tid:"`
    * this returns the register values for each thread, but they're in the wrong
      order.

* `listprocess`
    * starts with `"pid: "`
* ??
    * starts with `"patching smdh"`
* ??
    * starts with `"rtRecvSocket failed: "`

Usually, it will just log the string to the main text display, but for various
UI features, it may update them using data from the string.

A `cmd` value of `0x9` is a response to the `ReadMem` command packet sent by
the `data()` function.

## `listthread` Response Registers
For some reason the debugger sends the register values (as space delimited ascii
hex within text data) in a strange order with some unknown values and possibly
duplicates. The order is as follows:

`unk0`, `unk1`, `unk2`, `r4`, `r5`, `unk5/r6`, `unk7`, `r1`, `r2`, `r3`, `r12`,
`unk12`, `sp`, `lr`, `pc`, `unk16`, `unk17`, `unk18`, `unk19`, `unk20`, `unk21`,
`unk22`, `unk23`, `unk24`, `unk25/r6`, `r7`, `r8`, `r9`, `r10`, `r11`, `unk31`


## Client Messages

The client sends messages via the
`sendPacket(UInt32 type, UInt32 cmd, UInt32[] args, UInt32 dataLen)` method.
With every new message to be sent, it increments a sequence member variable used
in the `seq` field of the packet. There is also a
`sendEmptyPacket(UInt32 cmd, UInt32 arg0 = 0, UInt32 arg1 = 0, UInt32 arg2 = 0)`
helper method used to wrap `sendPacket` with a simple to use API that gives the
`cmd` value and up to three arguments.

Known commands:
* heartbeat
    * cmd: `0x0`
    * type: `0x0`
    * no args
    * no data
* upload ("save") file
    * cmd: `0x1`
    * type: `0x1`
    * no args
    * data:
          * `0x200` length remote filename byte array (likely the server does a
            nul check/up to 0x200 for this)
          * `n` length file data byte array
* hello
    * cmd: `0x3`
    * type: `0x0`
    * no args
    * no data
* reload
    * cmd: `0x4`
    * type: `0x0`
    * no args
    * no data
* read memory
    * cmd: `0x9`
    * type: `0x0` (sent via `sendEmptyPacket`)
    * args:
        * pid
        * address
        * length
* write memory
    * cmd: `0xa`
    * type: `0x1`
    * args:
        * pid
        * address
        * data length (it sends this both in the args list and as the data
          length field)
    * data:
        * data byte array

