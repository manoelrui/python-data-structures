from abc import ABCMeta, abstractmethod


class Node:
    def __init__(self, value=None, node=None):
        self.value = value
        self.next = node


class ABCList:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.length = 0
        self.head = None

    @abstractmethod
    def add(self, value):
        pass

    @abstractmethod
    def find(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    @abstractmethod
    def remove_recursive(self, value):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def clean(self):
        pass

    @abstractmethod
    def print_recursive(self):
        pass

    @abstractmethod
    def print_reverse(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other_list):
        pass

    @abstractmethod
    def __ne__(self, other_list):
        pass
