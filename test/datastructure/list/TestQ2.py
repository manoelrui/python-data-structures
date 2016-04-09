import unittest
from datastructure.list.SortedLinkedList import SortedLinkedList


class TestQ2(unittest.TestCase):
    # 1. Criar uma lista vazia;
    def test_creation(self):
        l = SortedLinkedList()
        self.assertIsNotNone(l)
        self.assertIsNone(l.head)
        self.assertEqual(l.length, 0)

    # 2. Inserir elemento no inicio;
    def test_insertion(self):
        l = SortedLinkedList()
        self.assertEqual(l.length, 0)
        self.assertEqual("", str(l))

        l.add(56)
        self.assertEqual(l.length, 1)
        self.assertEqual("56", str(l))

        l.add(342)
        self.assertEqual(l.length, 2)
        self.assertEqual("56 342", str(l))

        l.add(70)
        self.assertEqual(l.length, 3)
        self.assertEqual("56 70 342", str(l))

        l.add(30)
        l.add(35)
        self.assertEqual(l.length, 5)
        self.assertEqual("30 35 56 70 342", str(l))

        l.add(400)
        l.add(420)
        self.assertEqual(l.length, 7)
        self.assertEqual("30 35 56 70 342 400 420", str(l))

        l.add(60)
        l.add(64)
        self.assertEqual(l.length, 9)
        self.assertEqual("30 35 56 60 64 70 342 400 420", str(l))

    # 3. Imprimir os valores armazenados na lista;
    def test_print(self):
        l = SortedLinkedList()
        self.assertEqual("", str(l))

        l.add(51)
        self.assertEqual("51", str(l))

        l.add(23)
        l.add(32)
        l.add(55)
        l.add(1)
        l.add(59)
        self.assertEqual("1 23 32 51 55 59", str(l))

    # 4 Imprimir os valores armazenados na lista usando recursao;
    def test_recursive_print(self):
        l = SortedLinkedList()
        self.assertEqual("", l.print_recursive())

        l.add(984)
        self.assertEqual("984", l.print_recursive())

        l.add(3)
        l.add(78)
        l.add(1000)
        self.assertEqual("3 78 984 1000", l.print_recursive())

    # 5.Imprimir os valores armazenados na lista em ordem reversa (da cauda para a cabeca da lista);
    def test_print_reverse(self):
        l = SortedLinkedList()
        self.assertEqual("", l.print_reverse())

        l.add(234)
        self.assertEqual("234", l.print_reverse())

        l.add(33)
        l.add(89)
        l.add(670)
        self.assertEqual("670 234 89 33", l.print_reverse())

    # 6.Verificar se a lista esta vazia (retorna 1 se vazia ou 0 se nao vazia);
    def test_is_empty(self):
        l = SortedLinkedList()
        self.assertTrue(l.is_empty())

        l.add(45)
        self.assertFalse(l.is_empty())

    # 7.Recuperar/Buscar um determinado elemento da lista;
    def test_find(self):
        l = SortedLinkedList()
        self.assertIsNone(l.find(578))

        l.add(34)
        l.add(77)
        l.add(4)
        l.add(6)
        self.assertEquals(4, l.find(4))
        self.assertEquals(77, l.find(77))
        self.assertEquals(34, l.find(34))
        self.assertIsNone(l.find(666))

    # .8 Remover um determinado elemento da lista;
    def test_remove(self):
        l = SortedLinkedList()
        self.assertTrue(l.remove(78) == False)
        self.assertEqual("", str(l))

        l.add(34)
        l.add(3)
        l.add(78)
        l.add(55)
        l.add(60)
        l.add(70)
        l.add(66)

        self.assertTrue(l.remove(3) == True)
        self.assertEqual(l.length, 6)
        self.assertEqual("34 55 60 66 70 78", str(l))

        self.assertTrue(l.remove(60) == True)
        self.assertEqual(l.length, 5)
        self.assertEqual("34 55 66 70 78", str(l))

        self.assertTrue(l.remove(78) == True)
        self.assertEqual(l.length, 4)
        self.assertEqual("34 55 66 70", str(l))

        self.assertTrue(l.remove(70) == True)
        self.assertEqual(l.length, 3)
        self.assertEqual("34 55 66", str(l))

        self.assertTrue(l.remove(34) == True)
        self.assertEqual(l.length, 2)
        self.assertEqual("55 66", str(l))

        self.assertTrue(l.remove(55) == True)
        self.assertEqual(l.length, 1)
        self.assertEqual("66", str(l))

        self.assertTrue(l.remove(3454) == False)
        self.assertEqual(l.length, 1)
        self.assertEqual("66", str(l))

    # 9.Remover um determinado elemento da lista usando recursao;
    def test_remove_recursion(self):
        l = SortedLinkedList()
        self.assertTrue(l.remove_recursive(78) == False)
        self.assertEqual("", str(l))

        l.add(34)
        l.add(3)
        l.add(78)
        l.add(55)
        l.add(60)
        l.add(70)
        l.add(66)

        self.assertTrue(l.remove_recursive(3) == True)
        self.assertEqual(l.length, 6)
        self.assertEqual("34 55 60 66 70 78", str(l))

        self.assertTrue(l.remove_recursive(60) == True)
        self.assertEqual(l.length, 5)
        self.assertEqual("34 55 66 70 78", str(l))

        self.assertTrue(l.remove_recursive(78) == True)
        self.assertEqual(l.length, 4)
        self.assertEqual("34 55 66 70", str(l))

        self.assertTrue(l.remove_recursive(70) == True)
        self.assertEqual(l.length, 3)
        self.assertEqual("34 55 66", str(l))

        self.assertTrue(l.remove_recursive(34) == True)
        self.assertEqual(l.length, 2)
        self.assertEqual("55 66", str(l))

        self.assertTrue(l.remove_recursive(55) == True)
        self.assertEqual(l.length, 1)
        self.assertEqual("66", str(l))

        self.assertTrue(l.remove_recursive(3454) == False)
        self.assertEqual(l.length, 1)
        self.assertEqual("66", str(l))

    # 10. Liberar a lista;
    def test_list_clean(self):
        l = SortedLinkedList()
        self.assertEqual(l.length, 0)
        self.assertIsNone(l.head)

        l.add(45)
        l.add(33)
        l.add(450)
        l.clean()
        self.assertEqual(l.length, 0)
        self.assertIsNone(l.head)

        l.clean()
        self.assertEqual(l.length, 0)
        self.assertIsNone(l.head)

    # 11 Verificar se duas lista sao iguais
    def test_compare_lists(self):
        list1 = SortedLinkedList()
        list2 = SortedLinkedList()
        self.assertFalse(list1 == None)
        self.assertFalse(list2 == None)

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
