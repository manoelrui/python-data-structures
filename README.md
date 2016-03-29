# Resumo

Implementação em python de vários tipos de estruturas de dados como listas, hashs e árvores.

# Organização do código

* No módulo 'datastructure' encontra-se a implementação das estruturas de dados.
* No módulo 'application' encontra-se a implementação de alguns Tipo Abstratos de Dados(TADs) utilizados em aplicações conhencidas como contas bancárias.
* No módulo 'test' encontra-se todos os testes unitários que validam cada um dos módulos implementados.

# Execução dos testes

Para executar todos os testes de todos os módulos de uma só vez no modo verboso, basta executar o script 'run_tests.py' da seguinte maneira:

    python -m unittest -v run_tests
  
Se não quise executar no modo verboso basta executar o script 'run_tests.py' diretamente:

    python run_tests.py
    
# Visualização dos dados (LINUX)

Para visualizar graficamente as estruturas de dados é preciso instalar a API Graphviz para python e seus binários com dependências. Para instalar o módulo graphviz basta utilizar a ferramenta pip. Caso a ferramenta ainda não estiver instalada, basta instalar executando:

    sudo apt-get install python-pip

Com a ferramenta pip já isntalada, para instalar o módulo graphviz basta executar:

    pip install graphviz
    
Finalmente, para instalar os binários execute:

    sudo apt-get install graphviz
    
## Código testes

No módulo 'graphic' existe uma classe responsável por exibir as estruturas de dados implementadas no módulo 'datastructure'. O código abaixo é um exemplo de como instanciar uma lista encadeada e passar para um objeto do tipo 'Graphic' a responsabilidade gerar uma imagem do tipo 'png' localizadas no diretório 'images'.

    from datastructure.list.LinkedList import *
    from graphic.Graphic import *
    l = LinkedList()
    l.add(34)
    l.add(3)
    l.add(78)
    l.add(66)
    g = Graphic(l)
    g.show()

O resultado esperado para o código anterior é mostrado a seguir:

![alt text](https://github.com/manoelrui19/python-data-structures/blob/master/images/LinkedList.png "Linked List output")






