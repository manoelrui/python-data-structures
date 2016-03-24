#from datastricture.list.LinkedList import LinkedList
from datastructure.list.LinkedList import *

list = LinkedList()
list.add(567)
list.add(45)
list.add(34)
list.add(67)
list.add(7)
list.add(789)

print list.find(34)
list.removeRecursive(67)

print 'Length of List: ', list.length
print list
list.graph()
list.clean()
