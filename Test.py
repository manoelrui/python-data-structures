from LinkedList import LinkedList

list = LinkedList()
list.add(567)
list.add(45)
list.add(34)
list.add(2)
list.add(43)
list.add(54)

print 'Length of List: ', list.length
print list.printReverse(list.head)
list.graph()
