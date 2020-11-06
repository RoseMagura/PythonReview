class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
    
    def search(self, value):
        if self.head is None:
            return None

        node = self.head
        
        while node:
            if node.value == value:
                return node
            node = node.next
        
        raise ValueError("Value not found in list")

    def to_list(self):
        # TODO: Write function to turn Linked List into Python List
        list = []
        node = self.head
        while node:
            list.append(node.value)
            node = node.next
        return list
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            self.head = Node(value)
            return

        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def size(self):
        """ Return the size or length of the linked list. """
        # TODO: Write function to get size here
        node = self.head
        size = 0
        while node:
            size += 1
            node = node.next
        return size

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
    
    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

linked_list = LinkedList()
linked_list.prepend(1)
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(3)
linked_list.append(4)
linked_list.append(3)
# linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)
# assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)
# assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"