from List import *
from datastructure.list.LinkedList import LinkedList


class SortedLinkedList(LinkedList):
    def add(self, value):
        if self.head is None:
            self.head = Node(value)
            self.length += 1
            return

        if self.head.value > value:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return

        it_node = self.head
        while it_node.next is not None:
            if it_node.next.value > value:
                new_node = Node(value)
                new_node.next = it_node.next
                it_node.next = new_node
                self.length += 1
                return
            it_node = it_node.next

        new_node = Node(value)
        it_node.next = new_node
        self.length += 1
