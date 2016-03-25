from datastructure.list.DoublySortedLinkedList import *
import Graphic as graph
from datastructure.list.LinkedList import LinkedList

l = DoublySortedLinkedList()
l.add(56)
l.add(45)
l.add(3)
l.add(656)
l.add(64)

l.remove(656)
l.remove(64)
l.remove(3)

g = graph.Graphic(l)
g.find(80)

print 'Length of l: ', l.length
print l
l.clean()
