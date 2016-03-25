from datastructure.list.SortedLinkedList import *
import Graphic as graph

list = SortedLinkedList()
list.add(56)
list.add(2)
list.add(10)
list.add(50)
list.add(1)
list.add(80)
list.add(79)
list.add(0)

list1 = LinkedList()
list1.add(1)
list1.add(80)
list1.add(79)
list1.add(0)

g = graph.Graphic(list1)
g.find(80)

print 'Length of List: ', list.length
print list
list.clean()
