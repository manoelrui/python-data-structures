from datastructure.list.LinkedList import *
from graphviz import Digraph

class Graphic():
    def __init__(self, dataStruct = None):
        self.dataStruct = dataStruct

    def show(self):
        if isinstance(self.dataStruct, LinkedList.__base__):
            self.__showLinkedList()

    def find(self, value):
        if isinstance(self.dataStruct, LinkedList.__base__):
            self.__findLinkedList(value)

    def __showLinkedList(self):
        g = Digraph('G', filename='LinkedList')
        g.body.extend(['rankdir=LR'])

        itNode = self.dataStruct.head
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


    def __findLinkedList(self, value):
        g = Digraph('G', filename='LinkedList')
        g.body.extend(['rankdir=LR'])

        itNode = self.dataStruct.head
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