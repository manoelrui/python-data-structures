from List import ABCList
from Node import Node
from graphviz import Digraph

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

	def graph(self):
		g = Digraph('G', filename='LinkedList')
		g.body.extend(['rankdir=LR'])

		itNode = self.head
		if itNode != None:
			g.node(str(itNode.value))
			while(itNode.next != None):
				g.edge(str(itNode.value), str(itNode.next.value))
				g.node(str(itNode.next.value))
				itNode = itNode.next
		g.view()
