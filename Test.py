#from datastricture.list.LinkedList import LinkedList
from datastructure.list.LinkedList import *

list = LinkedList()
list.add(56)

list.remove(345)
list.remove(5)

print 'Length of List: ', list.length
print list
list.printGraphically()
list.findGraphically(78)
list.clean()
