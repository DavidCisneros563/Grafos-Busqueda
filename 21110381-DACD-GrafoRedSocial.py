# Grafo de red social
grafo_red_social = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David', 'Eve'],
    'Charlie': ['Alice', 'Eve'],
    'David': ['Bob'],
    'Eve': ['Bob', 'Charlie']
}

def dfs_red_social(grafo, nodo, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(nodo)
    print(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs_red_social(grafo, vecino, visitado)

print("Recorrido DFS en el grafo de red social:")
dfs_red_social(grafo_red_social, 'Alice')