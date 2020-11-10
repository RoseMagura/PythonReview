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
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head

        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next
        
        raise ValueError("Value not found in the list.")

    def size(self):
        """ Return the size or length of the linked list. """
        # TODO: Write function to get size here
        node = self.head
        size = 0
        while node:
            size += 1
            node = node.next
        return size

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None
      
        node = self.head
        self.head = self.head.next
        return node.value
    

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return
        
        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return
            index += 1
            node = node.next
        else:
            self.append(value)
        
        
def reverse(linked_list):
    reversed = LinkedList()
    node = linked_list.head
    while node:
        # print(node.value)
        reversed.prepend(node.value)
        node = node.next
    return reversed

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
linked_list.prepend(1)
linked_list.prepend(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(3)
linked_list.remove(1)

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) 
# and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
# print(flipped.to_list())

# print(linked_list.to_list())
# print(reverse(linked_list).to_list())
# assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)
# assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)
# assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"