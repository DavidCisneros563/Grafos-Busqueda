# Grafo de rutas de un mapa
grafo_mapa = {
    'CiudadA': ['CiudadB', 'CiudadC'],
    'CiudadB': ['CiudadA', 'CiudadD', 'CiudadE'],
    'CiudadC': ['CiudadA', 'CiudadF'],
    'CiudadD': ['CiudadB'],
    'CiudadE': ['CiudadB', 'CiudadF'],
    'CiudadF': ['CiudadC', 'CiudadE']
}

def dfs_mapa(grafo, nodo, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(nodo)
    print(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs_mapa(grafo, vecino, visitado)

print("Recorrido DFS en el grafo de rutas de un mapa:")
dfs_mapa(grafo_mapa, 'CiudadA')