from LinkedList import LinkedList

list = LinkedList()
list.add(5556)
list.add(45)
list.add(34)
list.add(2)
list.add(43)
list.add(54)
list.add(566)
list.add(5)
list.add(67)
list.add(3)

list.remove(2)

print 'Length of List: ', list.length
print list
list.graph()
