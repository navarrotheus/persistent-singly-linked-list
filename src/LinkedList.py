from Node import Node

class LinkedList:
    def __init__(self, nodes=None):
      self.head = None
      self.index_last_version = 0

      if nodes is not None:
        node = Node(value=nodes.pop(0))
        self.head = node
        for elem in nodes:
          node.next = Node(value=elem)
          node = node.next

    def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
        nodes.append(str(node.value))
        node = node.next
      nodes.append("None")
      return " -> ".join(nodes)

    def __iter__(self):
      node = self.head

      while node is not None:
        yield node
        node = node.next

    def append(self, new_node_value):
      new_node = Node(new_node_value)
      if self.head is None:
        self.head = new_node
        return
      
      if (new_node.value <= self.head.value):
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        return

      current_node = self.head
      while (current_node.next and new_node.value > current_node.next.value):
        current_node = current_node.next

      new_node.next = current_node.next
      current_node.next = new_node

      new_node.previous = current_node
      if new_node.next is not None:
        new_node.next.previous = new_node

    def remove(self, target_node_value):
      if self.head is None:
        raise Exception("List is empty")

      if self.head.value == target_node_value:
        self.head = self.head.next
        self.head.previous = None
        return

      for node in self:
        if node.value == target_node_value:
          node.previous.next = node.next
          if node.next is not None:
            node.next.previous = node.previous
          return

      raise Exception("Node with value '%s' not found" % target_node_value)