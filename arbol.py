from nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)

    def _agregar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.derecho)
    

    def in_order_traversal(self):
        self._in_order_traversal_recursivo(self.raiz)

    def _in_order_traversal_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._in_order_traversal_recursivo(nodo_actual.izquierdo)
            print(nodo_actual.valor)
            self._in_order_traversal_recursivo(nodo_actual.derecho)
            
    def pre_order(self):
        self.pre_order_recursivo(self.raiz)
    
    def pre_order_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor)
            self.pre_order_recursivo(nodo_actual.izquierdo)
            self.pre_order_recursivo(nodo_actual.derecho)
        
    def post_order(self):
        self.post_order_recursivo(self.raiz)
        
    def post_order_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self.post_order_recursivo(nodo_actual.izquierdo)
            self.post_order_recursivo(nodo_actual.derecho)
            print(nodo_actual.valor)
            

    def search(self, valor):
        self.search_recursivo(self.raiz, valor)
        
    def search_recursivo(self, nodo_actual, valor):
        if nodo_actual is not None:
            if nodo_actual.valor == valor:
                print("Nodo encontrado")
                return True
            else:
                self.search_recursivo(nodo_actual.izquierdo, valor)
                
                self.search_recursivo(nodo_actual.derecho, valor)
                
    def search_min(self):
        self.search_min_recursivo(self.raiz)
        
    def search_min_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            if nodo_actual.izquierdo is None:
                print(nodo_actual.valor)
            else:
                self.search_min_recursivo(nodo_actual.izquierdo)
            
    def search_max(self):
        self.search_max_recursivo(self.raiz)
        
    def search_max_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            if nodo_actual.derecho is None:
                print(nodo_actual.valor)
            else:
                self.search_max_recursivo(nodo_actual.derecho)
        
    def update(self, valor, nuevo):
        self.delete(valor)
        print("Valor eliminado")
        self.agregar(nuevo)
        print("Nuevo valor agregado")
    
    def delete(self, valor):
        self.raiz = self._delete_recursivo(self.raiz, valor)

    def _delete_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierdo = self._delete_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._delete_recursivo(nodo.derecho, valor)
        else:
            # no tiene hijos
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            # tiene un solo hijo
            elif nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            # tiene dos hijos
            else:
                sucesor = self._encontrar_minimo(nodo.derecho)
                nodo.valor = sucesor.valor
                nodo.derecho = self._delete_recursivo(nodo.derecho, sucesor.valor)

        return nodo

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual