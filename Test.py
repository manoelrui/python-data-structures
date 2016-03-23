from LinkedList import LinkedList

list = LinkedList()
list.clean()

list.add(567)
list.add(45)
list.add(34)
list.add(67)
list.add(7)

print 'Length of List: ', list.length
print list.printRecursive(list.head)
print list.printReverse(list.head)
list.graph()
list.clean()
pass
