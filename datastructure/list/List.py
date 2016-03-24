from abc import ABCMeta, abstractmethod

class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

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
    def isEmpty(self):
        pass

    @abstractmethod
    def clean(self):
        pass

    @abstractmethod
    def printRecursive(self, node):
        pass

    @abstractmethod
    def printReverse(self, node):
        pass

	@abstractmethod
	def __str__(self):
			pass

