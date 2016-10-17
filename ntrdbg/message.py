class Message(object):
  def __init__(self, seq, typ, cmd, args, data):
    self.seq = seq
    self.type = typ
    self.cmd = cmd
    self.args = args
    self.data = data
