class Node:
    def __init__(self, cargo =None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

def print_list(node):
    while node:
        print node,
        node = node.next
    print

print_list(n1)

def print_backward(list):
    if list == None:
        return
    head = list
    tail = list.next
    print_backward(tail)
    print head,

print print_backward(n1)


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
