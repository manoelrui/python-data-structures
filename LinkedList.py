from List import ABCList
from Node import Node

class LinkedList(ABCList):	
	def add(self, value):
		newNode = Node(value)
		if self.head == None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode
		self.length += 1

	def find(self, value):
		pass
	
	def remove(self, value):
		pass

	def __str__(self):
		resultString = ""
		itNode = self.head
		if itNode != None:
			resultString += str(itNode.value)
			while(itNode.next != None):
				resultString += " " + str(itNode.next.value)
				itNode = itNode.next
		return resultString

