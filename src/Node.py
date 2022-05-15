class Node:
    def __init__(self, value):
      self.value = value
      self.next = None
      self.previous = None

    def __repr__(self):
      return str(self.value)