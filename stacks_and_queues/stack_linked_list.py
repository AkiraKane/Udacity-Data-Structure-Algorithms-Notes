class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):

        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        # place the new node at the head of the linked list (top)
        else:
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elemens == 0

    def pop(self):
        if self.is_empty():
            return None

        # copy data to a local value
        value = self.head.value
        # move head pointer to point to next node
        self.head = self.head.next
        self.num_elements -= 1
        return value
