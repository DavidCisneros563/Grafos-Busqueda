# Grafo de partidos y rivalidades
grafo_partidos = {
    'Chivas': ['Atlas', 'América', 'Cruz Azul'],
    'Atlas': ['Chivas', 'Pumas'],
    'América': ['Chivas', 'Pachuca'],
    'Cruz Azul': ['Chivas', 'Toluca'],
    'Pumas': ['Atlas', 'Tigres'],
    'Pachuca': ['América'],
    'Toluca': ['Cruz Azul'],
    'Tigres': ['Pumas']
}

def dfs_partidos(grafo, nodo, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(nodo)
    print(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs_partidos(grafo, vecino, visitado)

print("Recorrido DFS en el grafo de partidos y rivalidades:")
dfs_partidos(grafo_partidos, 'Chivas')