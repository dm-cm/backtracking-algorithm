from pila import Pila
from mapa import Mapa, Coord
from random import shuffle


def resolver_laberinto(mapa):
    """Funcion auxiliar que se generó para testear el codigo"""
    camino = Pila()
    visitadas = Pila()
    camino.apilar(mapa.origen())

    while camino.ver_tope() != mapa.destino():
        backtrack(camino, visitadas, mapa)
    return camino

def backtrack(camino, visitadas, mapa):
    """Algoritmo para resolver laberinto"""
    coord = camino.ver_tope()
    visitadas.apilar(coord)

    if mapa.destino() == coord:
        # llegamos!
        return

    vecina_adyacente = busca_vecinas(coord, mapa, 1)
    shuffle(vecina_adyacente) # le da un toque de aleatoriedad
    for v in vecina_adyacente:
        if not visitadas.contiene(v) and not mapa.celda_bloqueada(v):
            camino.apilar(v)
            return

    camino.desapilar()

def backtrack_inverso(camino, visitadas, mapa):
    """Algoritmo para generar laberinto"""
    
    coord = camino.ver_tope()
    visitadas.apilar(coord)

    if coord != mapa.destino():
        vector_unitario = busca_vecinas(Coord(0,0), mapa, 1)
        shuffle(vector_unitario)
        for v in vector_unitario:
            un_paso = coord + v
            dos_pasos = coord + v + v
            if not visitadas.contiene(dos_pasos) and mapa.es_coord_valida(dos_pasos):
                mapa.desbloquear(un_paso)
                mapa.desbloquear(dos_pasos)
                camino.apilar(dos_pasos)
                return

    camino.desapilar()


def busca_vecinas(coord, mapa, distancia):
    """Busca los cuatro vecinos [derecha, izquierda, arriba, abajo] a una distancia"""
    v1 = coord + Coord(distancia, 0)
    v2 = coord + Coord(-distancia, 0)
    v3 = coord + Coord(0, distancia)
    v4 = coord + Coord(0, -distancia)

    return [v1, v2, v3, v4]
