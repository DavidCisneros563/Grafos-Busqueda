# Grafo de organización empresarial
grafo_organizacion = {
    'CEO': ['CTO', 'CFO'],
    'CTO': ['LeadDev', 'Dev1', 'Dev2'],
    'CFO': ['Accountant'],
    'LeadDev': ['Dev3'],
    'Dev1': [],
    'Dev2': [],
    'Accountant': [],
    'Dev3': []
}

def dfs_organizacion(grafo, nodo, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(nodo)
    print(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs_organizacion(grafo, vecino, visitado)

print("Recorrido DFS en el grafo de organización empresarial:")
dfs_organizacion(grafo_organizacion, 'CEO')