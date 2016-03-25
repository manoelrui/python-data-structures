from List import *
from datastructure.list.LinkedList import LinkedList

class SortedLinkedList(LinkedList):
    def add(self, value):
        if self.head == None:
            self.head = Node(value)
            self.length += 1
            return

        if self.head.value > value:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
            self.length += 1
            return

        itNode = self.head
        while(itNode.next != None):
            if itNode.next.value > value:
                newNode = Node(value)
                newNode.next = itNode.next
                itNode.next = newNode
                self.length += 1
                return
            itNode = itNode.next

        newNode = Node(value)
        itNode.next = newNode
        self.length += 1


