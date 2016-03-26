from application.BankAccount import *

m = AccountManager()
m.add(BankAccount(123, -32))
m.add(SavingAccount(456, 55))
m.add(LoyaltyAccount(789, 99))
m.add(BankAccount(131415, 776))

print m

# l = CircularDoublyLinkedList()
# l.add(34)
# l.add(3)
# l.add(78)
# l.add(55)
# l.add(60)
# l.add(70)
# l.add(66)
#
# print l

#l.remove_recursive(56)
#l.remove_recursive(64)

#g = graph.Graphic(l)
#g.show()
#g.find(80)

#print 'Length of l: ', l.length
#print l
#l.clean()
