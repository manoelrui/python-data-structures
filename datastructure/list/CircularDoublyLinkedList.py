from datastructure.list.CircularLinkedList import *


class CircularDoublyLinkedList(CircularLinkedList):
    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.prev = self.head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.head.prev = self.tail
        self.tail.next = self.head
        self.length += 1

    def remove(self, value):
        father, node_to_remove = self.find_node(value)

        if node_to_remove is None:
            return False

        if node_to_remove == self.head:
            self.head = node_to_remove.next
        else:
            if node_to_remove is self.tail:
                self.tail = father
            father.next = node_to_remove.next
            if node_to_remove.next is not None:
                node_to_remove.next.prev = father

        self.head.prev = self.tail
        self.tail.next = self.head
        del node_to_remove
        self.length -= 1
        return True

    def remove_recursive(self, value):
        return self.__removeRecursive(None, self.head, value)

    def __removeRecursive(self, father, node, value):
        if node is None:
            return False

        if node.value == value:
            if node == self.head:
                self.head = node.next
            else:
                if node is self.tail:
                    self.tail = father
                father.next = node.next
                if node.next is not None:
                    node.next.prev = father

            self.head.prev = self.tail
            self.tail.next = self.head
            del node
            self.length -= 1
            return True

        if node is self.tail:
            return False

        father = node
        return self.__removeRecursive(father, node.next, value)