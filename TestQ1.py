import unittest
from datastructure.list.LinkedList import LinkedList

class TestQ1(unittest.TestCase):

#1. Criar uma lista vazia;
    def test_creation(self):
        list = LinkedList()
        self.assertIsNotNone(list)
        self.assertIsNone(list.head)


#2. Inserir elemento no inicio;
    def test_insertion(self):
        list = LinkedList()
        list.add(5)
        self.assertEqual(list.length, 1)

        list.add(67)
        self.assertEqual(list.length, 2)

#3. Imprimir os valores armazenados na lista;
    def test_print(self):
        list = LinkedList()
        list.add(98)
        list.add(12)
        list.add(6)
        self.assertEqual("6 12 98", list.__str__())


#4 Imprimir os valores armazenados na lista usando recursao;
    def test_recursive_print(self):
        list = LinkedList()
        list.add(8)
        list.add(23)
        list.add(112)
        self.assertEqual("112 23 8", list.printRecursive())


#5.Imprimir os valores armazenados na lista em ordem reversa (da cauda para a cabeca da lista);
    def test_print_reverse(self):
        list = LinkedList()
        list.add(76)
        list.add(2)
        list.add(150)
        self.assertEqual("76 2 150", list.printReverse())


#6.Verificar se a lista esta vazia (retorna 1 se vazia ou 0 se nao vazia);
    def test_is_empty(self):
        list = LinkedList()
        self.assertTrue(list.isEmpty())


#7.Recuperar/Buscar um determinado elemento da lista;
    def test_find(self):
        list = LinkedList()
        list.add(236)
        list.add(34)
        list.add(50)
        list.add(670)
        self.assertEquals(50, list.find(50))
        self.assertEquals(670, list.find(670))
        self.assertEquals(236, list.find(236))

#.8 Remover um determinado elemento da lista;
    def test_remove(self):
        list = LinkedList()
        list.add(236)
        list.add(34)
        list.add(50)
        list.add(670)
        self.assertEqual(list.length, 4)

        list.remove(670)
        self.assertEqual(list.length, 3)
        self.assertIsNone(list.find(670))

        list.remove(236)
        self.assertEqual(list.length, 2)
        self.assertIsNone(list.find(236))

        list = LinkedList()
        self.assertIsNone(list.remove(545))

#9.Remover um determinado elemento da lista usando recursao;
    def test_remove_recursion(self):
        list = LinkedList()
        list.add(45)
        list.add(33)
        list.add(323)
        list.add(76)
        self.assertEqual(list.length, 4)

        list.removeRecursive(76)
        self.assertEqual(list.length, 3)
        self.assertIsNone(list.find(76))

        list.removeRecursive(45)
        self.assertEqual(list.length, 2)
        self.assertIsNone(list.find(45))


#10. Liberar a lista;
    def test_list_clean(self):
        list = LinkedList()
        list.add(5)
        list.add(34)
        list.add(980)
        list.clean()
        self.assertEqual(list.length, 0)
        self.assertIsNone(list.head)

        list.clean()
        self.assertEqual(list.length, 0)


if __name__ == '__main__':
    unittest.main()