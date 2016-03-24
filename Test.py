#from datastricture.list.LinkedList import LinkedList
from datastructure.list.LinkedList import *

list = LinkedList()
list.add(45)
list.add(1)
list.add(78)
list.add(5)
list.add(3)
list.add(345)

print 'Length of List: ', list.length
print list
list.printGraphically()
list.clean()
