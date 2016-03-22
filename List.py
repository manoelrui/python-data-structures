from abc import ABCMeta, abstractmethod

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
	
