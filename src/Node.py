class Node:
    def __init__(self, value, version):
      self.value = value
      self.next = None
      self.previous = None
      self.version = version

      # (value, version)
      self.mods = []

    def __repr__(self):
      return str(self.value)

    def insert_mod(self, value, version):
      mod = (value, version)
      self.mods.append((mod))
