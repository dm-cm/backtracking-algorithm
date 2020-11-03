from mapa import Mapa, Coord
from backtracking import backtrack_inverso
from pila import Pila

def generar_laberinto(filas, columnas):
    """Genera un laberinto.

    Argumentos:
        filas, columnas (int): Tamaño del mapa

    Devuelve:
        Mapa: un mapa nuevo con celdas bloqueadas formando un laberinto
              aleatorio
    """

    if es_par(filas):
    	filas = filas-1
    if es_par(columnas):
    	columnas = columnas-1

    mapa = Mapa(filas,columnas)
    mapa.asignar_origen(Coord(1,1))
    mapa.asignar_destino(Coord(filas-2,columnas-2))
    mapa.bloquear_todo()
    visitados_v = Pila()
    camino_v = Pila()
    camino_v.apilar(mapa.origen())
    mapa.desbloquear(mapa.origen())
    while len(camino_v) > 0:
    	backtrack_inverso(camino_v, visitados_v, mapa)
    return mapa 

def es_par(n):
	"""Devuelve True si es par, False si no"""
	return n % 2 == 0

