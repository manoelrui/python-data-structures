from List import *
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
        father, node = self.findNode(value)
        if node == None:
            return None
        return node.value


    def findNode(self, value):
        fatherNode = None
        itNode = self.head
        while (True):
            if itNode == None or value == itNode.value:
                return fatherNode, itNode

            if itNode.next == None:
                return None, None

            fatherNode = itNode
            itNode = itNode.next


    def remove(self, value):
        father, nodeToRemove = self.findNode(value)

        if nodeToRemove == None:
            return None

        if nodeToRemove == self.head:
            self.head = nodeToRemove.next
        else:
            father.next = nodeToRemove.next

        del nodeToRemove
        self.length -= 1

    def removeRecursive(self, value):
        return self.__removeRecursive(None, self.head, value);

    def __removeRecursive(self, father, node, value):
        if node == None:
            return None, None

        if node.value == value:
            if node == self.head:
                self.head = node.next
            else:
                father.next = node.next

            del node
            self.length -= 1
            return

        father = node
        self.__removeRecursive(father, node.next, value)

    def isEmpty(self):
        if self.length == 0:
            return True
        return False


    def clean(self):
        if self.head == None:
            return

        while(self.head != None):
            nodeToRemove = self.head
            self.head = self.head.next
            del nodeToRemove

        self.length = 0

    def printRecursive(self):
        return self.__printRecursive(self.head)


    def __printRecursive(self, node=None):
        if node == None:
            return ""
        result = self.__printRecursive(node.next)
        if result == "":
            return str(node.value)
        else:
            return str(node.value) +  " " + self.__printRecursive(node.next)


    def printReverse(self):
         return self.__printReverse(self.head)


    def __printReverse(self, node=None):
        if node == None:
            return ""
        result = self.__printReverse(node.next)
        if result == "":
            return str(node.value)
        else:
            return self.__printReverse(node.next) + " " + str(node.value)


    def __str__(self):
        resultString = ""
        itNode = self.head
        if itNode != None:
            resultString += str(itNode.value)
            while (itNode.next != None):
                resultString += " " + str(itNode.next.value)
                itNode = itNode.next
        return resultString

    def __eq__(self, list):
        return True

    def printGraphically(self):
        g = Digraph('G', filename='LinkedList')
        g.body.extend(['rankdir=LR'])

        itNode = self.head
        if itNode != None:
            g.node("HEAD", style="filled", fillcolor="red", shape="cds")
            g.edge("HEAD", str(itNode.value))

        while (itNode != None):
            g.node(str(itNode.value), shape="box")

            if itNode.next == None:
                g.node("NULL", shape="none")
                g.edge(str(itNode.value), "NULL")
            else:
                g.edge(str(itNode.value), str(itNode.next.value))

            itNode = itNode.next
        g.view()


    def findGraphically(self, value):
        g = Digraph('G', filename='LinkedList')
        g.body.extend(['rankdir=LR'])

        itNode = self.head
        if itNode != None:
            g.node("HEAD", style="filled", fillcolor="red", shape="cds")
            g.edge("HEAD", str(itNode.value))

        while (itNode != None):
            if itNode.value == value:
                g.node(str(itNode.value), style="filled", fillcolor="green", shape="box")
            else:
                g.node(str(itNode.value), shape="box")

            if itNode.next == None:
                g.node("NULL", shape="none")
                g.edge(str(itNode.value), "NULL")
            else:
                g.edge(str(itNode.value), str(itNode.next.value))

            itNode = itNode.next
        g.view()