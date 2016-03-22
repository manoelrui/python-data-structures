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
        father, node = self.findNode(value).value
        return node.value

    def findNode(self, value):
        fatherNode = None
        itNode = self.head
        while (True):
            if value == itNode.value:
                return fatherNode, itNode

            if itNode.next == None:
                return None, None

            fatherNode = itNode
            itNode = itNode.next

    def remove(self, value):
        father, nodeToRemove = self.findNode(value)

        if nodeToRemove == self.head:
            self.head = nodeToRemove.next
        else:
            father.next = nodeToRemove.next

        del nodeToRemove
        self.length -= 1

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

    def __str__(self):
        resultString = ""
        itNode = self.head
        if itNode != None:
            resultString += str(itNode.value)
            while (itNode.next != None):
                resultString += " " + str(itNode.next.value)
                itNode = itNode.next
        return resultString

    def graph(self):
        g = Digraph('G', filename='LinkedList')
        g.body.extend(['rankdir=LR'])

        itNode = self.head
        if itNode != None:
            g.node(str(itNode.value))
            while (itNode.next != None):
                g.edge(str(itNode.value), str(itNode.next.value))
                g.node(str(itNode.next.value))
                itNode = itNode.next
        g.view()
