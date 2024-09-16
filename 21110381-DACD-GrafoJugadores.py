# Grafo de jugadores y posiciones
grafo_jugadores = {
    'Portero': ['Jugador1', 'Jugador2'],
    'Defensores': ['Jugador3', 'Jugador4', 'Jugador5'],
    'Centrocampistas': ['Jugador6', 'Jugador7', 'Jugador8'],
    'Delanteros': ['Jugador9', 'Jugador10'],
    'Jugador1': [],
    'Jugador2': [],
    'Jugador3': [],
    'Jugador4': [],
    'Jugador5': [],
    'Jugador6': [],
    'Jugador7': [],
    'Jugador8': [],
    'Jugador9': [],
    'Jugador10': []
}

def dfs_jugadores(grafo, nodo, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(nodo)
    print(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs_jugadores(grafo, vecino, visitado)

print("Recorrido DFS en el grafo de jugadores y posiciones:")
dfs_jugadores(grafo_jugadores, 'Portero')
