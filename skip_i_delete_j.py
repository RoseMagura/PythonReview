# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    # Edge case - Skip 0 nodes (means Delete all nodes)
    if i == 0:
        return None
    
    # Edge case - Delete 0 nodes
    if j == 0:
        return head

    if head is None or j < 0 or i < 0:
        return head

    # count = 1

    current = head
    previous = None

    # new_head = None
    # new_tail = None

    while current:
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next

        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node
        
        previous.next = current
        # if count <= i:
        #     print(count)
        #     print('keeping')   
        #     if new_head is None:
        #         print('making linked list')
        #         new_head = current
        #         new_tail = new_head
        #     else:
        #         print('adding on')
        #         new_tail.next = current
        #         new_tail = new_tail.next
        # else:
        #     if count <= (j + i):
        #         print(count)
        #         print('deleting')
        #     else:
        #         if new_head is None:
        #             new_head = current
        #             new_tail = current
        #         else:
        #             new_tail.next = current
        #             new_tail = new_tail.next
        #         print('resetting')
        #         count = 1
        # count += 1
        # current = current.next
        # return new_head
    return head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]
        
    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)