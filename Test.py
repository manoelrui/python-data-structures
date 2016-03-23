from LinkedList import LinkedList

list = LinkedList()
list.add(567)
list.add(45)
list.add(34)
list.add(67)
list.add(7)
list.add(789)

print 'Length of List: ', list.length
print list.printRecursive()
print list.printReverse()
list.graph()
list.clean()
