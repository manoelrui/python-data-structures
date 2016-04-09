from datastructure.list.List import *


class LinkedList(ABCList):
    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
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

            if it_node.next is None:
                return None, None

            father_node = it_node
            it_node = it_node.next

    def remove(self, value):
        father, node_to_remove = self.find_node(value)

        if node_to_remove is None:
            return False

        if node_to_remove == self.head:
            self.head = node_to_remove.next
        else:
            father.next = node_to_remove.next

        del node_to_remove
        self.length -= 1
        return True

    def remove_recursive(self, value):
        return self.__remove_recursive(None, self.head, value)

    def __remove_recursive(self, father, node, value):
        if node is None:
            return False

        if node.value == value:
            if node == self.head:
                self.head = node.next
            else:
                father.next = node.next

            del node
            self.length -= 1
            return True

        father = node
        return self.__remove_recursive(father, node.next, value)


    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def clean(self):
        if self.head is None:
            return

        while self.head is not None:
            node_to_remove = self.head
            self.head = self.head.next
            del node_to_remove

        self.length = 0

    def print_recursive(self):
        return self.__printRecursive(self.head)

    def __printRecursive(self, node=None):
        if node is None:
            return ""
        result = self.__printRecursive(node.next)
        if result == "":
            return str(node.value)
        else:
            return str(node.value) + " " + self.__printRecursive(node.next)

    def print_reverse(self):
        return self.__printReverse(self.head)

    def __printReverse(self, node=None):
        if node is None:
            return ""
        result = self.__printReverse(node.next)
        if result == "":
            return str(node.value)
        else:
            return self.__printReverse(node.next) + " " + str(node.value)

    def __str__(self):
        result_string = ""
        it_node = self.head
        if it_node is not None:
            result_string += str(it_node.value)
            while it_node.next is not None:
                result_string += " " + str(it_node.next.value)
                it_node = it_node.next
        return result_string

    def __eq__(self, other_list):
        if other_list is None:
            return False

        if self.length != other_list.length:
            return False

        it_node_1 = self.head
        it_node_2 = other_list.head
        while it_node_1 is not None:
            if it_node_1.value != it_node_2.value:
                return False

            it_node_1 = it_node_1.next
            it_node_2 = it_node_2.next

        return True

    def __ne__(self, other_list):
        return not self.__eq__(other_list)

    def __len__(self):
        return self.length
