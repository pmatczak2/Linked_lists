class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):  # Here __init__() that allows you to quickly create linked lists with some data:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):  # The __repr__ method will return the string that will print the linked list
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


    def __iter__(self):  # How to Traverse a Linked List
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def add_first(self, node):  # Inserting at the Beginning
        node.next = self.head
        self.head = node

    def add_last(self, node):  # Inserting at the End
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

llist = LinkedList(['a', 'b','c'])

llist.add_last(Node('d'))
print(llist)
