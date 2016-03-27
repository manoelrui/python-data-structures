from datastructure.list.LinkedList import *


class CircularLinkedList(LinkedList):
    def __init__(self, tail=None):
        super(CircularLinkedList, self).__init__()
        self.tail = tail

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.tail.next = self.head
        self.length += 1

    def find(self, value):
        father, node = self.find_node(value)
        if node is None:
            return None
        return node.value

    def find_node(self, value):
        father_node = None
        it_node = self.head
        while True:
            if it_node is None or value == it_node.value:
                return father_node, it_node

            if it_node.next is self.tail.next:
                return None, None

            father_node = it_node
            it_node = it_node.next

    def remove(self, value):
        father, node_to_remove = self.find_node(value)

        if node_to_remove is None:
            return None

        if node_to_remove == self.head:
            self.head = node_to_remove.next
        else:
            if node_to_remove is self.tail:
                self.tail = father
            father.next = node_to_remove.next

        self.tail.next = self.head
        del node_to_remove
        self.length -= 1

    def remove_recursive(self, value):
        return self.__removeRecursive(None, self.head, value)

    def __removeRecursive(self, father, node, value):
        if node is None:
            return

        if node.value == value:
            if node == self.head:
                self.head = node.next
            else:
                if node is self.tail:
                    self.tail = father
                father.next = node.next

            self.tail.next = self.head
            del node
            self.length -= 1
            return

        if node is self.tail:
            return

        father = node
        self.__removeRecursive(father, node.next, value)

    def clean(self):
        if self.head is None:
            return

        while self.head is not self.tail:
            node_to_remove = self.head
            self.head = self.head.next
            del node_to_remove

        del self.head
        self.head = None

        self.length = 0

    def print_recursive(self):
        if self.head == None:
            return ""
        return self.__printRecursive(self.head)

    def __printRecursive(self, node=None):
        if node is self.tail:
            return str(node.value)
        return str(node.value) + " " + self.__printRecursive(node.next)

    def print_reverse(self):
        if self.head == None:
            return ""
        return self.__printReverse(self.head)

    def __printReverse(self, node=None):
        if node is self.tail:
            return str(node.value)
        return self.__printReverse(node.next) + " " + str(node.value)

    def __str__(self):
        result_string = ""
        it_node = self.head
        if it_node is not None:
            result_string += str(it_node.value)
            while it_node.next != self.tail.next:
                result_string += " " + str(it_node.next.value)
                it_node = it_node.next
        return result_string