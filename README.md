# Lista encadeada ordenada com persistência parcial

## Objetivo

Implementar lista encadeada ordenada com persistência parcial.
O seu programa deve receber como entrada um arquivo de texto com um conjunto de operações e deve escrever como saída um arquivo de texto com o resultado das operações.

## Versões da estrutura

As versões da estrutura serão identificadas por inteiros não negativos onde a estrutura inicial vazia terá valor 0. Cada operação de inclusão ou remoção cria uma nova versão identificada pelo próximo inteiro da versão modificada pela operação.

## Formato do arquivo de entrada

Cada linha do arquivo de entrada contém exatamente uma operação como descrita a seguir.

## Operações

### Inclusão

Uma operação de inclusão será descrita por "INC" seguida de um espaço e depois um inteiro. Este elemento deve ser incluído na sua estrutura de dados.
_Exemplo de linha de inclusão:_
INC 13

### Remoção

Uma operação de remoção será descrita por "REM" seguida de um espaço e depois um inteiro. Um nó com este valor deve ser removido (apenas um). Caso não tenha nenhum nó com este valor, a estrutura não será modificada, mas um novo identificador da estrutura será criado.
_Exemplo de linha de remoção:_
REM 42

### Sucessor

Uma operação de sucessor será descrita por "SUC" seguida de dois inteiros, separados por espaços. O primeiro inteiro será o valor para obter o sucessor e o segundo inteiro será a versão da estrutura em que a operação de sucessor será realizada. Caso esta versão não exista, a operação deve ser realizada na última versão da estrutura. O sucessor de um valor x será o menor valor que tem na estrutura com valor estritamente maior que x, e infinito (INF) caso não haja valor maior que x na estrutura. Deve ser escrito no arquivo de saída a linha da operação realizada seguida por uma linha com o resultado da operação.
Exemplo de linha de sucessor:
SUC 50 65
Exemplo no arquivo de saída:
SUC 50 65
52

### Imprimir

Imprimir:
Uma operação de impressão será descrita por "IMP" seguida de um espaço e um inteiro. O inteiro indica a versão da estrutura que deve ser impressa e, caso esta versão não exista, a operação deve ser realizada na última versão da estrutura. O arquivo de saída deve ter uma cópia da operação de impressão seguido por uma linha com a a estrutura impressa. Para a lista encadeada, basta imprimir os valores em ordem, separados por espaços. Para a árvore rubro-negra, os valores devem ser impressos em ordem e cada valor será seguido da sua profundidade na árvore e pela sua cor, separados por vírgulas.
Exemplo de linha de impressão:

IMP 65
Exemplo no arquivo de saída para lista encadeada:
IMP 65
13 42 50 52 65

Exemplo no arquivo de saída para árvore rubro-negra:
IMP 65
13,2,R 42,1,N 50,0,N 52,2,R 65,1,N
