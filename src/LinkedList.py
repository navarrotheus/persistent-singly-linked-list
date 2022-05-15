from Node import Node

class LinkedList:
    def __init__(self, nodes=None):
      self.head = None
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

    def append(self, new_node):
      if self.head is None:
        self.head = new_node
        return
      
      if (new_node.value <= self.head.value):
        new_node.next = self.head
        self.head = new_node
        return

      current_node = self.head
      while (current_node.next and new_node.value > current_node.next.value):
        current_node = current_node.next

      new_node.next = current_node.next
      current_node.next = new_node

    def remove(self, target_node_value):
      if self.head is None:
        raise Exception("List is empty")

      if self.head.value == target_node_value:
        self.head = self.head.next
        return

      previous_node = self.head
      for node in self:
        if node.value == target_node_value:
            previous_node.next = node.next
            return
        previous_node = node

      raise Exception("Node with value '%s' not found" % target_node_value)