## Message structure

Each message contanins a header, followed by a variable length data section.
The header of a message is 84 bytes, divided into message metadata, a fixed set of 16 arguments, and a size field specifying the lenght of the data.

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
    +---+---+---+---+===============================================+
 50 |     size      |              ...message data...               |
    +---+---+---+---+===============================================+

~~~