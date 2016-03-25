from datastructure.list.SortedLinkedList import *
import Graphic as graph

l = SortedLinkedList()
l.add(56)
l.add(2)
l.add(10)
l.add(50)
l.add(1)
l.add(80)
l.add(79)
l.add(0)

list1 = LinkedList()
list1.add(1)
list1.add(80)
list1.add(79)
list1.add(0)

g = graph.Graphic(list1)
g.find(80)

print 'Length of l: ', l.length
print l
l.clean()
