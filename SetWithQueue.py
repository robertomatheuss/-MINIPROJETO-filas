from Fila_Array import *
class ExceptionSetEmpty(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
    
class SetWithQueue():
    def __init__(self):
        self.fila = FilaArray()
        self.set = []
        
    def add(self, element):
        if element not in self.set:
            self.set.append(element)
            self.fila.enqueue(element)
        
    def remove(self,element):
        if self.fila.is_empty():
           raise ExceptionSetEmpty("Set is empty")
        elif not self.contains(element):
            raise ValueError("Element not found")
        else:
            novaFila = FilaArray()
            while not self.fila.is_empty():
                item = self.fila.dequeue() 
                if item != element:
                    novaFila.enqueue(item) 
            self.fila = novaFila  
            self.set.remove(element)
    
    def contains(self,element):
        return element in self.set 
    
    def size(self):
        return len(self.fila)
    
    def list(self):
        return self.set  