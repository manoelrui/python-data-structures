from datastructure.list.List import Node2
from datastructure.list.SortedLinkedList import SortedLinkedList


class DoublySortedLinkedList(SortedLinkedList):
    def add(self, value):
        if self.head is None:
            self.head = Node2(value)
            self.length += 1
            return

        if self.head.value > value:
            new_node = Node2(value)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return

        it_node = self.head
        while it_node.next is not None:
            if it_node.next.value > value:
                new_node = Node2(value)
                new_node.prev = it_node
                new_node.next = it_node.next
                it_node.next.prev = new_node
                it_node.next = new_node
                self.length += 1
                return
            it_node = it_node.next

        new_node = Node2(value)
        new_node.prev = it_node
        it_node.next = new_node
        self.length += 1

    def remove(self, value):
        if self.head is None:
            return

        if value == self.head.value:
            node_to_remove = self.head
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next
            del node_to_remove
            self.length -= 1
            return

        it_node = self.head
        while it_node is not None:
            if it_node.value == value:
                node_to_remove = it_node
                it_node.prev.next = it_node.next
                if it_node.next is not None:
                    it_node.next.prev = it_node.prev
                del node_to_remove
                self.length -= 1
            it_node = it_node.next

    def remove_recursive(self, value):
        pass