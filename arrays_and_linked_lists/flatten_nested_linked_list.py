class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)


def merge(list1, list2):
    """ Merges the two linked lists in a single, soted linked list"""
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    list1_elt = list1.head
    list2_elt = list2.head

    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
