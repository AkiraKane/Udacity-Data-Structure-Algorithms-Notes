class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)

# treversing the list


def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


print_linked_list(head)

# creating a linked list using iteration
# O(n^2)


def create_linked_list(input_list):

    head = None

    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(value)

    return head


def create_linked_list_better(input_list):

    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head

        else:
            tail.next = Node(value)
            tail = tail.next

    return head


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # move to the tail (the last node)
        else:
            node = self.head
            while node.next:
                node = node.next

            node.next = Node(value)
            return

    def to_list(self):
        out_list = []

        node = self.head

        while node:
            out_list.append(node.value)
            node = node.next

        return out_list


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next

##################### Doubly Linked List ###################


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return


linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous
