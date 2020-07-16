class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

class LinkedList:
    # def __init__(self):
    #     self.head = None   
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for el in nodes:
                node.next = Node(data=el)
                node = node.next
                
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def add_first(self, node):
        node.next = self.head
        self.head = node
        
    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for curr in self:
            pass
        curr.next = node
        
    def add_after(self, target_data, new_node):
        if not self.head:
            raise Exception('List is empty')
        for node in self:
            if node.data == target_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_data)
    
    # def add_before(self, target_data, new_node):
    #     if not self.head:
    #         raise Exception('List is empty')
    #     for node in self:
    #         if node.next.data == target_data:
    #             new_node.next = node.next
    #             node.next = new_node
    #             return
            
    def add_before(self, target_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_data)
    
    # def remove_node(self, target_data):
    #     if not self.head:
    #         raise Exception("List is empty")

    #     if self.head.data == target_data:
    #         self.head = self.head.next
    #         return

    #     previous_node = self.head
    #     for node in self:
    #         if node.data == target_data:
    #             previous_node.next = node.next
    #             return
    #         previous_node = node

    #     raise Exception("Node with data '%s' not found" % target_data)   
    
    def remove_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
            
    def find(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found
    
    def reverse(self):
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node
            
llist = LinkedList()
first_node = Node('a')
llist.head = first_node
print(llist)

second_node = Node('b')
third_node = Node('c')

first_node.next = second_node
second_node.next = third_node
# llist.add_first('c')
print(llist)

list2 = LinkedList(['angela', 'ben', 'christina', 'dasha', 'elon'])
list2.add_first(Node('andy'))
list2.add_last(Node('kate'))
list2.add_after('elon', Node('frank'))
list2.add_before('kate', Node('glen'))
list2.remove_node('glen')
list2.reverse()
for name in list2:
    print(name)