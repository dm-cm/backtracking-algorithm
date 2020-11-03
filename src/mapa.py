class Coord:
    """
    Representa las coordenadas de una celda en una grilla 2D, representada
    como filas y columnas. Las coordendas ``fila = 0, columna = 0`` corresponden
    a la celda de arriba a la izquierda.

    Las instancias de Coord son inmutables.
    """

    def __init__(self, fila=0, columna=0):
        """Constructor.

        Argumentos:
            fila (int), columna (int): Coordenadas de la celda
        """
        self.fila = validar_entero(fila)
        self.columna = validar_entero(columna)

    def trasladar(self, df, dc):
        """Trasladar una celda.

        Devuelve una nueva instancia de Coord, correspondiente a las coordenadas
        de la celda que se encuentra ``df`` filas y ``dc`` columnas de distancia.

        Argumentos:
            df (int): Cantidad de filas a trasladar
            dc (int): Cantidad de columnas a trasladar

        Devuelve:
            Coord: Las coordenadas de la celda trasladada
        """

        return self + Coord(df, dc) 

    def distancia(self, otro):
        """Distancia cuadrada entre dos celdas.

        Argumentos:
            otro (Coord)

        Devuelve:
            int: El cuadrado de la distancia entre las dos celdas (no negativo)
        """
        dfila = self.fila - otro.fila
        dcol = self.columna - otro.columna
        return (dfila*dfila + dcol*dcol)**0.5

    def __eq__(self, otro):
        """Determina si dos coordenadas son iguales"""
        return self.fila == otro.fila and self.columna == otro.columna

    def __iter__(self):
        """Iterar las componentes de la coordenada.

        Devuelve un iterador
        """
        self.n = 0
        return self

    def __next__(self):
        """Complemento del Iter.

        Devuelve un iterador
        """
        if self.n < 2:
            if self.n == 0:
                result = self.fila
            else:
                result = self.columna
            self.n += 1
            return result
        else:
            raise StopIteration

    def __hash__(self):
        """Código "hash" de la instancia inmutable."""
        return hash((self.fila, self.columna))

    def __repr__(self):
        """Representación de la coordenada como cadena de texto (formal)"""
        return "Coord({}, {})".format(self.fila, self.columna)

    def __str__(self):
        """Representación de la coordenada como cadena de texto (informal)"""
        return "({}, {})".format(self.fila, self.columna)

    def __add__(self, otro):
        """Suma entre dos celdas.

        Argumentos:
            otro (Coord)

        Devuelve:
            int|float: La suma de dos celdas
        """
        return Coord(self.fila + otro.fila, self.columna + otro.columna)

class Mapa:
    """
    Representa el mapa de un laberinto en una grilla 2D con:

    * un tamaño determinado (filas y columnas)
    * una celda origen
    * una celda destino
    * 0 o más celdas "bloqueadas", que representan las paredes del laberinto

    Las instancias de Mapa son mutables.
    """
    def __init__(self, filas=10, columnas=10):
        """Constructor.

        El mapa creado tiene todas las celdas desbloqueadas, el origen en la celda
        de arriba a la izquierda y el destino en el extremo opuesto.

        Argumentos:
            filas, columnas (int): Tamaño del mapa
        """
        self.filas = validar_entero(filas)
        self.columnas = validar_entero(columnas)
        self.asignar_origen(Coord(1, 1))
        self.asignar_destino(Coord(self.filas - 2, self.columnas - 2))
        self.bloqueadas = [[False for j in range(self.columnas)] for i in range(self.filas)]
        self.coordenadas = [[Coord() for j in range(self.columnas)] for i in range(self.filas)]
        for i in range(self.filas):
            for j in range(self.columnas):
                self.coordenadas[i][j] = Coord(i,j)

    def dimension(self):
        """Dimensiones del mapa (filas y columnas).

        Devuelve:
            (int, int): Cantidad de filas y columnas
        """
        return (self.filas, self.columnas)

    def origen(self):
        """Celda origen.

        Devuelve:
            Coord: Las coordenadas de la celda origen
        """
        return self.origen_v

    def destino(self):
        """Celda destino.

        Devuelve:
            Coord: Las coordenadas de la celda destino
        """
        return self.destino_v

    def asignar_origen(self, coord):
        """Asignar la celda origen.

        Argumentos:
            coord (Coord): Coordenadas de la celda origen
        """
        self.origen_v = coord

    def asignar_destino(self, coord):
        """Asignar la celda destino.

        Argumentos:
            coord (Coord): Coordenadas de la celda destino
        """
        self.destino_v = coord

    def celda_bloqueada(self, coord):
        """¿La celda está bloqueada?

        Argumentos:
            coord (Coord): Coordenadas de la celda

        Devuelve:
            bool: True si la celda está bloqueada o no existe
        """
        if self.es_coord_valida(coord):
            return self.bloqueadas[coord.fila][coord.columna]
        return True

    def bloquear(self, coord):
        """Bloquear una celda.

        Si la celda estaba previamente bloqueada, no hace nada.

        Argumentos:
            coord (Coord): Coordenadas de la celda a bloquear
        """
        if self.es_coord_valida(coord):
            self.bloqueadas[coord.fila][coord.columna] = True

    def bloquear_todo(self):
    	"""Bloquea todas las celdas"""
    	for coord in self:
    		self.bloquear(coord)

    def desbloquear(self, coord):
        """Desbloquear una celda.

        Si la celda estaba previamente desbloqueada, no hace nada.

        Argumentos:
            coord (Coord): Coordenadas de la celda a desbloquear
        """
        if self.es_coord_valida(coord):
            self.bloqueadas[coord.fila][coord.columna] = False

    def alternar_bloque(self, coord):
        """Alternar entre celda bloqueada y desbloqueada.

        Si la celda estaba previamente desbloqueada, la bloquea, y viceversa.

        Argumentos:
            coord (Coord): Coordenadas de la celda a alternar
        """
        if self.es_coord_valida(coord):
            self.bloqueadas[coord.fila][coord.columna] = not self.bloqueadas[coord.fila][coord.columna]

    def es_coord_valida(self, coord):
        """¿Las coordenadas están dentro del mapa?

        Argumentos:
            coord (Coord): Coordenadas de una celda

        Devuelve:
            bool: True si las coordenadas corresponden a una celda dentro del mapa
        """
        if coord.fila >= self.filas or coord.columna >= self.columnas or coord.fila < 0 or coord.columna < 0:
            return False
        return True

    def trasladar_coord(self, coord, df, dc):
        """Trasladar una coordenada, si es posible.

        Argumentos:
            coord: La coordenada de una celda en el mapa
            df, dc: La traslación a realizar

        Devuelve:
            Coord: La coordenada trasladada si queda dentro del mapa. En caso
                   contrario, devuelve la coordenada recibida.
        """
    
        coord_nueva = coord.trasladar(df, dc)
        if self.es_coord_valida(coord_nueva):
            return coord_nueva
        return coord

    def __iter__(self):
        """Iterar por las coordenadas de todas las celdas del mapa.

        Se debe garantizar que la iteración cubre todas las celdas del mapa, en
        cualquier orden.
        """
        self.n = 0
        return self

    def __next__(self):
        """Complemento del Iter.

        Se debe garantizar que la iteración cubre todas las celdas del mapa, en
        cualquier orden.

        """
        if self.n < self.filas * self.columnas:
            f = self.n // self.columnas
            c = (self.n - self.columnas * f)
            self.n += 1
            return self.coordenadas[f][c]
        else:
            raise StopIteration

    def __repr__(self):
        """Representación de la coordenada como cadena de texto (formal)"""
        texto = "Mapa de {} filas y {} columnas\n".format(self.filas, self.columnas)
        texto = texto + "Inicio: {}\n".format(self.origen()) + "Fin: {}\n\n".format(self.destino())  
        for i in range(0, self.filas):
            for j in range(0, self.columnas):
                if self.bloqueadas[i][j]:
                    texto = texto + "1"
                else:
                    texto = texto + "0"
            texto = texto + "\n"
        return texto

    def __str__(self):
        """Representación de la coordenada como cadena de texto (formal)"""
        texto = "[{}, {}][".format(self.filas, self.columnas)
        for i in range(0, self.filas):
            texto = texto + "["
            for j in range(0, self.columnas):
                if self.bloqueadas[i][j]:
                    texto = texto + "1, "
                else:
                    texto = texto + "0, "
            texto = texto.rstrip(", ") + "]"
        texto = texto + "]"
        return texto

def validar_entero(valor):
    #Si el valor es entero, lo devuelve. En caso contrario lanza TypeError.
    if not isinstance(valor, (int)):
        raise TypeError("{} no es un valor entero".format(valor))
    return valor
