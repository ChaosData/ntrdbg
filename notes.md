## Server Message structure

The client maintains a thread that actively reads messages sent by the server.

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

A `cmd` value of `0x0` appears to indicate a UTF-8 textual response with `\n`
line breaks. This is a response to multiple commands (list is a WIP):

* `memlayout`
  * starts with `"valid memregions:"`
* `listthread`
  * starts with `"tid:"`
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
