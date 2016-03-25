import unittest
from datastructure.list.SortedLinkedList import SortedLinkedList

class TestQ2(unittest.TestCase):

#1. Criar uma lista vazia;
    def test_creation(self):
        list = SortedLinkedList()
        self.assertIsNotNone(list)
        self.assertIsNone(list.head)
        self.assertEqual(list.length, 0)


#2. Inserir elemento no inicio;
    def test_insertion(self):
        list = SortedLinkedList()
        list.add(56)
        self.assertEqual(list.length, 1)

        list.add(342)
        self.assertEqual(list.length, 2)

        list.add(70)
        self.assertEqual(list.length, 3)

        list.add(60)
        self.assertEqual(list.length, 4)


#3. Imprimir os valores armazenados na lista;
    def test_print(self):
        list = SortedLinkedList()
        self.assertEqual("", str(list))

        list.add(51)
        self.assertEqual("51", str(list))

        list.add(23)
        list.add(32)
        list.add(55)
        list.add(1)
        list.add(59)
        self.assertEqual("1 23 32 51 55 59", str(list))



#4 Imprimir os valores armazenados na lista usando recursao;
    def test_recursive_print(self):
        list = SortedLinkedList()
        self.assertEqual("", list.printRecursive())

        list.add(984)
        self.assertEqual("984", list.printRecursive())

        list.add(3)
        list.add(78)
        list.add(1000)
        self.assertEqual("3 78 984 1000", list.printRecursive())


#5.Imprimir os valores armazenados na lista em ordem reversa (da cauda para a cabeca da lista);
    def test_print_reverse(self):
        list = SortedLinkedList()
        self.assertEqual("", list.printReverse())

        list.add(234)
        self.assertEqual("234", list.printReverse())

        list.add(33)
        list.add(89)
        list.add(670)
        self.assertEqual("670 234 89 33", list.printReverse())


#6.Verificar se a lista esta vazia (retorna 1 se vazia ou 0 se nao vazia);
    def test_is_empty(self):
        list = SortedLinkedList()
        self.assertTrue(list.isEmpty())

        list.add(45)
        self.assertFalse(list.isEmpty())


#7.Recuperar/Buscar um determinado elemento da lista;
    def test_find(self):
        list = SortedLinkedList()
        self.assertIsNone(list.find(578))

        list.add(34)
        list.add(77)
        list.add(4)
        list.add(6)
        self.assertEquals(4, list.find(4))
        self.assertEquals(77, list.find(77))
        self.assertEquals(34, list.find(34))
        self.assertIsNone(list.find(666))

#.8 Remover um determinado elemento da lista;
    def test_remove(self):
        list = SortedLinkedList()
        self.assertIsNone(list.remove(78))

        list.add(34)
        list.add(3)
        list.add(78)
        list.add(55)
        list.add(60)

        list.remove(3)
        self.assertEqual(list.length, 4)

        list.remove(60)
        self.assertEqual(list.length, 3)

        list.remove(78)
        self.assertEqual(list.length, 2)

        self.assertIsNone(list.remove(234))
        self.assertEqual(list.length, 2)


#9.Remover um determinado elemento da lista usando recursao;
    def test_remove_recursion(self):
        list = SortedLinkedList()
        self.assertIsNone(list.remove(78))

        list.add(34)
        list.add(3)
        list.add(78)
        list.add(55)
        list.add(60)

        list.remove(3)
        self.assertEqual(list.length, 4)

        list.remove(60)
        self.assertEqual(list.length, 3)

        list.remove(78)
        self.assertEqual(list.length, 2)

        self.assertIsNone(list.remove(234))
        self.assertEqual(list.length, 2)


#10. Liberar a lista;
    def test_list_clean(self):
        list = SortedLinkedList()
        self.assertEqual(list.length, 0)
        self.assertIsNone(list.head)

        list.add(45)
        list.add(33)
        list.add(450)
        list.clean()
        self.assertEqual(list.length, 0)
        self.assertIsNone(list.head)

        list.clean()
        self.assertEqual(list.length, 0)
        self.assertIsNone(list.head)

#11 Verificar se duas lista sao iguais
    def test_compare_lists(self):
        list1 = SortedLinkedList()
        list2 = SortedLinkedList()

        self.assertTrue(list1 == list2)
        self.assertFalse(list1 != list2)
        self.assertEqual(list1.length, list2.length)

        list1.add(34)
        list2.add(34)
        self.assertTrue(list1 == list2)
        self.assertFalse(list1 != list2)
        self.assertEqual(list1.length, list2.length)

        list1.add(56)
        list1.add(28)
        list2.add(56)
        self.assertFalse(list1 == list2)
        self.assertTrue(list1 != list2)
        self.assertLess(list2.length, list1.length)

        list2.add(555)
        self.assertFalse(list1 == list2)
        self.assertTrue(list1 != list2)
        self.assertEqual(list2.length, list1.length)

if __name__ == '__main__':
    unittest.main()