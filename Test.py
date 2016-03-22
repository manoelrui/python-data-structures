from Node import Node
import List
from LinkedList import LinkedList

node1 = Node(3)
node2 = Node(45)

node1.next = node2

print 'Node1: ', node1.value
print 'Node 2: ', node2.value
print 'Next of Node1: ', node1.next.value
