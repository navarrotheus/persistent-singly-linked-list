from Node import Node

class LinkedList:
    def __init__(self):
      self.head = None
      self.latest_version = 0
      self.versions_heads = []

    def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
        nodes.append(str(node.value))
        node = node.next
      nodes.append('None')
      return f'V{self.latest_version}: ' + ' -> '.join(nodes)

    def __iter__(self):
      node = self.head

      while node is not None:
        yield node
        node = node.next

    def append(self, new_node_value):
      self.latest_version = self.latest_version + 1
      new_node = Node(new_node_value, self.latest_version)

      # lista vazia
      if self.head is None:
        self.head = new_node

        new_node.insert_mod(self.latest_version, None)
        self.versions_heads.append(self.head)
        return
      
      # inicio da lista
      if (new_node.value <= self.head.value):
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node

        new_node.insert_mod(self.latest_version, new_node.next)

        self.versions_heads.append(self.head)
        return

      current_node = self.head
      while (current_node.next and new_node.value > current_node.next.value):
        current_node = current_node.next

      # final da lista
      if current_node.next is None:
        current_node.next = new_node
        new_node.previous = current_node

        new_node.previous.insert_mod(self.latest_version, new_node)
        new_node.insert_mod(self.latest_version, None)

        self.versions_heads.append(self.head)
        return

      # entre dois nós
      new_node.next = current_node.next
      new_node.next.previous = new_node
      current_node.next = new_node
      new_node.previous = current_node

      new_node.previous.insert_mod(self.latest_version, new_node)
      new_node.insert_mod(self.latest_version, new_node.next)

      self.versions_heads.append(self.head)

    def remove(self, target_node_value):
      self.latest_version = self.latest_version + 1

      # lista vazia
      if self.head is None:
        raise Exception("List is empty")

      # inicio da lista
      if self.head.value == target_node_value:
        old_head = self.head
        self.head = self.head.next
        self.head.previous = None

        old_head.insert_mod(self.latest_version, None)
        self.versions_heads.append(self.head)
        return

      for node in self:
        if node.value == target_node_value:
          # final da lista
          if node.next is None:
            node.previous.next = None

            node.previous.insert_mod(self.latest_version, None)

            self.versions_heads.append(self.head)
            return

          # entre dois nós
          node.previous.next = node.next
          node.next.previous = node.previous

          node.previous.insert_mod(self.latest_version, node.next)

          self.versions_heads.append(self.head)
          return

      raise Exception("Node with value '%s' not found" % target_node_value)

    def successor(self, target_successor_value, version_value):
      if version_value > self.latest_version:
        version_value = self.latest_version

      version_head = self.versions_heads[version_value - 1]

      current_node = version_head
      while current_node is not None and current_node.value <= target_successor_value:
        for mod in current_node.mods:
          if mod[0] <= version_value:
            current_node = mod[1]

      if current_node is not None and current_node.value == version_head.value:
        raise Exception(f'Node with value {target_successor_value} does not exists in version {version_value}')
      
      return current_node

    def get_list_by_version(self, version_value):
      if version_value > self.latest_version:
        version_value = self.latest_version
      
      version_head = self.versions_heads[version_value - 1]

      linked_list = []

      successor = version_head
      while successor is not None:
        linked_list.append(successor.value)
        successor = self.successor(successor.value, version_value)
      
      return linked_list
      

