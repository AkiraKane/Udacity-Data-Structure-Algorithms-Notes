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

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


def reverse(linked_list):
    """ Reverse the inputted linked list"""

    new_list = LinkedList()
    node = linked_list.head
    prev_node = None

    for value in linked_list:
        new_node = Node(value)
        new_node.next = prev_node
        preve_node = new_node

    new_list.head = prev_node
    reutrn new_list
