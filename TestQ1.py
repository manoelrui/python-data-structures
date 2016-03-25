import unittest
from datastructure.list.LinkedList import LinkedList


class TestQ1(unittest.TestCase):
    # 1. Criar uma lista vazia;
    def test_creation(self):
        l = LinkedList()
        self.assertIsNotNone(l)
        self.assertIsNone(l.head)
        self.assertEqual(l.length, 0)

    # 2. Inserir elemento no inicio;
    def test_insertion(self):
        l = LinkedList()
        l.add(5)
        self.assertEqual(l.length, 1)

        l.add(67)
        self.assertEqual(l.length, 2)

        l.add(1)
        self.assertEqual(l.length, 3)

        l.add(18)
        self.assertEqual(l.length, 4)

    # 3. Imprimir os valores armazenados na lista;
    def test_print(self):
        l = LinkedList()
        self.assertEqual("", str(l))

        l.add(44)
        self.assertEqual("44", str(l))

        l.add(98)
        l.add(12)
        l.add(6)
        self.assertEqual("6 12 98 44", str(l))

    # 4 Imprimir os valores armazenados na lista usando recursao;
    def test_recursive_print(self):
        l = LinkedList()
        self.assertEqual("", l.print_recursive())

        l.add(34)
        self.assertEqual("34", l.print_recursive())

        l.add(8)
        l.add(23)
        l.add(112)
        self.assertEqual("112 23 8 34", l.print_recursive())

    # 5.Imprimir os valores armazenados na lista em ordem reversa (da cauda para a cabeca da lista);
    def test_print_reverse(self):
        l = LinkedList()
        l.add(76)
        l.add(2)
        l.add(150)
        self.assertEqual("76 2 150", l.print_reverse())

    # 6.Verificar se a lista esta vazia (retorna 1 se vazia ou 0 se nao vazia);
    def test_is_empty(self):
        l = LinkedList()
        self.assertTrue(l.is_empty())

        l.add(676)
        self.assertFalse(l.is_empty())

    # 7.Recuperar/Buscar um determinado elemento da lista;
    def test_find(self):
        l = LinkedList()
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
        l = LinkedList()
        self.assertIsNone(l.remove(78))

        l.add(236)
        l.add(34)
        l.add(43)
        l.add(50)
        l.add(670)

        l.remove(670)
        self.assertEqual(l.length, 4)

        l.remove(43)
        self.assertEqual(l.length, 3)

        l.remove(236)
        self.assertEqual(l.length, 2)

        self.assertIsNone(l.remove(545))
        self.assertEqual(l.length, 2)

    # 9.Remover um determinado elemento da lista usando recursao;
    def test_remove_recursion(self):
        l = LinkedList()
        self.assertIsNone(l.remove(78))

        l.add(236)
        l.add(34)
        l.add(43)
        l.add(50)
        l.add(670)

        l.remove(670)
        self.assertEqual(l.length, 4)

        l.remove(43)
        self.assertEqual(l.length, 3)

        l.remove(236)
        self.assertEqual(l.length, 2)

        self.assertIsNone(l.remove(545))
        self.assertEqual(l.length, 2)

    # 10. Liberar a lista;
    def test_list_clean(self):
        l = LinkedList()
        self.assertEqual(l.length, 0)
        self.assertIsNone(l.head)

        l.add(5)
        l.add(34)
        l.add(980)
        l.clean()
        self.assertEqual(l.length, 0)
        self.assertIsNone(l.head)

        l.clean()
        self.assertEqual(l.length, 0)
        self.assertIsNone(l.head)


if __name__ == '__main__':
    unittest.main()
