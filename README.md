# Estrutura_de_dados

### 1)Implementar SetWithQueue

[SetWithQueue implementação](/SetWithQueue.py)

### 2) Vamos discutir o desempenho de cada função na classe SetWithQueue:

    def add(element)

Essa função tem desenpenho O(n) pois **(element not in self.set)**   percorre toda a lista e a função **(self.set.append(element))** tem desempenho O(1) porém dependendo do tamanho da lista pode ter O(n)

    def remove(element)

Essa função tem O(n) ou pode se falar também O(3n) pois **(not self.contains(element))** com essa verificação já percorrer a lista ou seja O(n) e nessa função também foi implementando um loop while que percorre toda a fila ou seja O(n) e por fim o **(self.set.remove(element))** na pior das hipoteses pode percorrer toda a lista para a remoção

    def contains(element)

Essa função também é O(n) pois no pior caso percorre toda a lista para fazer a verificação

    def size()

Essa função tem O(1) pois ela executa apenas uma operação constante **(len(self.fila))**

    def list()

Por fim essa função é uma operação constante que retorna a lista


### Referencia 

Usei apenas uma publicação no StackOverFlow para ter algumas ideias

[stackoverflow](https://stackoverflow.com/questions/2319086/a-queue-that-ensure-uniqueness-of-the-elements?newreg=5defe1a3ad9b4162acd82a0c34f341f1)