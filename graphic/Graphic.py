from datastructure.list.LinkedList import *
from graphviz import Digraph


class Graphic:
    def __init__(self, data_structure=None):
        self.data_structure = data_structure
        self.output_format = "png"
        self.output_dir = "images"

    def show(self):
        if isinstance(self.data_structure, LinkedList.__base__):
            self.__show_linked_list()

    def find(self, value):
        if isinstance(self.data_structure, LinkedList.__base__):
            self.__find_linked_list(value)

    def __show_linked_list(self):
        g = Digraph('G', filename=self.output_dir + '/' + 'LinkedList', format=self.output_format)
        g.body.extend(['rankdir=LR'])

        it_node = self.data_structure.head
        if it_node is not None:
            g.node("HEAD", style="filled", fillcolor="red", shape="cds")
            g.edge("HEAD", str(it_node.value))

        while it_node is not None:
            g.node(str(it_node.value), shape="box")

            if it_node.next is None:
                g.node("NULL", shape="none")
                g.edge(str(it_node.value), "NULL")
            else:
                g.edge(str(it_node.value), str(it_node.next.value))

            it_node = it_node.next
        g.view()

    def __find_linked_list(self, value):
        g = Digraph('G', filename=self.output_dir + '/' + 'LinkedList', format=self.output_format)
        g.body.extend(['rankdir=LR'])

        it_node = self.data_structure.head
        if it_node is not None:
            g.node("HEAD", style="filled", fillcolor="red", shape="cds")
            g.edge("HEAD", str(it_node.value))

        while it_node is not None:
            if it_node.value == value:
                g.node(str(it_node.value), style="filled", fillcolor="green", shape="box")
            else:
                g.node(str(it_node.value), shape="box")

            if it_node.next is None:
                g.node("NULL", shape="none")
                g.edge(str(it_node.value), "NULL")
            else:
                g.edge(str(it_node.value), str(it_node.next.value))

            it_node = it_node.next
        g.view()
