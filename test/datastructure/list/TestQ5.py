import unittest
from datastructure.list.CircularDoublyLinkedList import *


class TestQ5(unittest.TestCase):
    # 1. Criar uma lista vazia;
    def test_creation(self):
        l = CircularDoublyLinkedList()
        self.assertIsNotNone(l)
        self.assertIsNone(l.head)
        self.assertEqual(len(l), 0)

    # 2. Inserir elemento no inicio;
    def test_insertion(self):
        l = CircularDoublyLinkedList()
        self.assertEqual(len(l), 0)
        self.assertEqual("", str(l))

        l.add(56)
        self.assertEqual(len(l), 1)
        self.assertEqual("56", str(l))
        self.assertTrue(l.head is l.tail)
        self.assertTrue(l.head.next is l.tail.next)
        self.assertTrue(l.head.next is l.tail.prev)
        self.assertTrue(l.head.prev is l.tail.prev)
        self.assertTrue(l.head.prev is l.tail.next)
        self.assertTrue(l.head is l.tail)

        l.add(342)
        self.assertEqual(len(l), 2)
        self.assertEqual("342 56", str(l))
        self.assertTrue(l.head.next is l.tail)
        self.assertTrue(l.head is l.tail.prev)
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head is l.tail.next)

        l.add(70)
        self.assertEqual(len(l), 3)
        self.assertEqual("70 342 56", str(l))
        self.assertTrue(l.head.next is l.tail.prev)
        self.assertTrue(l.head is l.tail.next)
        self.assertTrue(l.head.next.prev is l.head)
        self.assertTrue(l.tail.prev.next is l.tail)

        l.add(60)
        self.assertEqual(len(l), 4)
        self.assertEqual("60 70 342 56", str(l))

    # 3. Imprimir os valores armazenados na lista;
    def test_print(self):
        l = CircularDoublyLinkedList()
        self.assertEqual("", str(l))

        l.add(44)
        self.assertEqual("44", str(l))

        l.add(98)
        l.add(12)
        l.add(6)
        self.assertEqual("6 12 98 44", str(l))

    # 4 Imprimir os valores armazenados na lista usando recursao;
    def test_recursive_print(self):
        l = CircularDoublyLinkedList()
        self.assertEqual("", l.print_recursive())

        l.add(34)
        self.assertEqual("34", l.print_recursive())

        l.add(8)
        l.add(23)
        l.add(112)
        self.assertEqual("112 23 8 34", l.print_recursive())

    # 5.Imprimir os valores armazenados na lista em ordem reversa (da cauda para a cabeca da lista);
    def test_print_reverse(self):
        l = CircularDoublyLinkedList()
        self.assertEqual("", l.print_recursive())

        l.add(13)
        self.assertEqual("13", l.print_recursive())

        l.add(76)
        l.add(2)
        l.add(150)
        self.assertEqual("13 76 2 150", l.print_reverse())

    # 6.Verificar se a lista esta vazia (retorna 1 se vazia ou 0 se nao vazia);
    def test_is_empty(self):
        l = CircularDoublyLinkedList()
        self.assertTrue(l.is_empty())

        l.add(676)
        self.assertFalse(l.is_empty())

    # 7.Recuperar/Buscar um determinado elemento da lista;
    def test_find(self):
        l = CircularDoublyLinkedList()
        self.assertIsNone(l.find(45))

        l.add(236)
        l.add(34)
        l.add(50)
        l.add(670)
        self.assertEquals(50, l.find(50))
        self.assertEquals(670, l.find(670))
        self.assertEquals(236, l.find(236))
        self.assertIsNone(l.find(666))

    # .8 Remover um determinado elemento da lista;
    def test_remove(self):
        l = CircularDoublyLinkedList()
        self.assertTrue(l.remove(78) == False)
        self.assertEqual("", str(l))

        l.add(34)
        l.add(3)
        l.add(78)
        l.add(55)
        l.add(60)
        l.add(70)
        l.add(66)

        self.assertTrue(l.remove(66) == True)
        self.assertEqual(len(l), 6)
        self.assertEqual("70 60 55 78 3 34", str(l))
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head.next.prev is l.head)
        self.assertTrue(l.tail.prev.next is l.tail)
        self.assertTrue(l.tail.next is l.head)

        self.assertTrue(l.remove(34) == True)
        self.assertEqual(len(l), 5)
        self.assertEqual("70 60 55 78 3", str(l))
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head.next.prev is l.head)
        self.assertTrue(l.tail.prev.next is l.tail)
        self.assertTrue(l.tail.next is l.head)

        self.assertTrue(l.remove(60) == True)
        self.assertEqual(len(l), 4)
        self.assertEqual("70 55 78 3", str(l))

        self.assertTrue(l.remove(70) == True)
        self.assertEqual(len(l), 3)
        self.assertEqual("55 78 3", str(l))
        self.assertTrue(l.head.next is l.tail.prev)
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head is l.tail.next)
        self.assertTrue(l.head.next.prev is l.head)
        self.assertTrue(l.tail.prev.next is l.tail)

        self.assertTrue(l.remove(3) == True)
        self.assertEqual(len(l), 2)
        self.assertEqual("55 78", str(l))
        self.assertTrue(l.head.next is l.tail)
        self.assertTrue(l.head is l.tail.prev)
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head is l.tail.next)

        self.assertTrue(l.remove(55) == True)
        self.assertEqual(len(l), 1)
        self.assertEqual("78", str(l))
        self.assertTrue(l.head.next is l.tail.next)
        self.assertTrue(l.head is l.tail.prev)
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head is l.tail.next)
        self.assertTrue(l.head is l.tail)

        self.assertTrue(l.remove(3454) == False)
        self.assertEqual(len(l), 1)
        self.assertEqual("78", str(l))

    # 9.Remover um determinado elemento da lista usando recursao;
    def test_remove_recursion(self):
        l = CircularDoublyLinkedList()
        self.assertTrue(l.remove_recursive(78) == False)
        self.assertEqual("", str(l))

        l.add(34)
        l.add(3)
        l.add(78)
        l.add(55)
        l.add(60)
        l.add(70)
        l.add(66)

        self.assertTrue(l.remove_recursive(66) == True)
        self.assertEqual(len(l), 6)
        self.assertEqual("70 60 55 78 3 34", str(l))
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head.next.prev is l.head)
        self.assertTrue(l.tail.prev.next is l.tail)
        self.assertTrue(l.tail.next is l.head)

        self.assertTrue(l.remove_recursive(34) == True)
        self.assertEqual(len(l), 5)
        self.assertEqual("70 60 55 78 3", str(l))
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head.next.prev is l.head)
        self.assertTrue(l.tail.prev.next is l.tail)
        self.assertTrue(l.tail.next is l.head)

        self.assertTrue(l.remove_recursive(60) == True)
        self.assertEqual(len(l), 4)
        self.assertEqual("70 55 78 3", str(l))

        self.assertTrue(l.remove_recursive(70) == True)
        self.assertEqual(len(l), 3)
        self.assertEqual("55 78 3", str(l))
        self.assertTrue(l.head.next is l.tail.prev)
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head is l.tail.next)
        self.assertTrue(l.head.next.prev is l.head)
        self.assertTrue(l.tail.prev.next is l.tail)

        self.assertTrue(l.remove_recursive(3) == True)
        self.assertEqual(len(l), 2)
        self.assertEqual("55 78", str(l))
        self.assertTrue(l.head.next is l.tail)
        self.assertTrue(l.head is l.tail.prev)
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head is l.tail.next)

        self.assertTrue(l.remove_recursive(55) == True)
        self.assertEqual(len(l), 1)
        self.assertEqual("78", str(l))
        self.assertTrue(l.head.next is l.tail.next)
        self.assertTrue(l.head is l.tail.prev)
        self.assertTrue(l.head.prev is l.tail)
        self.assertTrue(l.head is l.tail.next)
        self.assertTrue(l.head is l.tail)

        self.assertTrue(l.remove_recursive(3454) == False)
        self.assertEqual(len(l), 1)
        self.assertEqual("78", str(l))

    # 10. Liberar a lista;
    def test_list_clean(self):
        l = CircularDoublyLinkedList()
        self.assertEqual(len(l), 0)
        self.assertIsNone(l.head)

        l.add(5)
        l.add(34)
        l.add(980)
        l.clean()
        self.assertEqual(len(l), 0)
        self.assertIsNone(l.head)

        l.clean()
        self.assertEqual(len(l), 0)
        self.assertIsNone(l.head)


if __name__ == '__main__':
    unittest.main()
