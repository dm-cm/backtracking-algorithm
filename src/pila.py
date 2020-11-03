class Pila:
    '''
    Representa una pila con operaciones de apilar, desapilar y
    verificar si está vacía.
    '''

    def __init__(self):
        '''
        Crea una pila vacía.
        '''
        self.items = []

    def esta_vacia(self):
        '''
        Devuelve True si la lista está vacía, False si no.
        '''
        return len(self.items) == 0

    def contiene(self, x):
        '''
        Revisa si contiene un elemento x.
        '''
        for elemento in self.items:
            if elemento == x:
                return True
        return False

    def apilar(self, x):
        '''
        Apila un elemento en la pila.
        '''
        self.items.append(x)

    def desapilar(self):
        '''
        Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción.
        '''
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()

    def ver_tope(self):
        """devuelve el tope de la pila"""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items[len(self)-1]

    def ver_n(self, n):
        """devuelve el n-esimo elemento"""
        if n >= len(self.items):
            raise IndexError("La pila no tiene tantos elementos")
        return self.items[n]

    def apilar_muchos(self, iterable):
        '''
        Apila todos los elementos del iterable en la pila.
        '''
        for elem in iterable:
            self.apilar(elem)

    def __len__(self):
        return len(self.items)

    # Este método está para simplificar las pruebas
    def __str__(self):
        '''
        Devuelve una representación de la pila en la forma: 
        | e1, e2, ..., <TOPE
        '''
        return '| ' + ', '.join(map(str, self.items)) + ' <TOPE'

    def __repr__(self):
        '''
        Devuelve la representación formal de str
        '''
        return str(self)


