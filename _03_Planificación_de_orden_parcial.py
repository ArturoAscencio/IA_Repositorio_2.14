import networkx as nx

# Crear un grafo dirigido ac�clico (DAG) para representar las tareas y las restricciones
G = nx.DiGraph()

# Agregar nodos (tareas)
G.add_node("Tarea A")
G.add_node("Tarea B")
G.add_node("Tarea C")
G.add_node("Tarea D")

# Agregar arcos dirigidos (restricciones)
G.add_edge("Tarea A", "Tarea B")
G.add_edge("Tarea A", "Tarea C")
G.add_edge("Tarea B", "Tarea D")

# Encontrar un plan parcial utilizando el algoritmo topol�gico
try:
    plan_parcial = list(nx.topological_sort(G))
    print("Plan parcial encontrado:")
    for tarea in plan_parcial:
        print(tarea)
except nx.NetworkXUnfeasible:
    print("No se puede encontrar un plan parcial debido a las restricciones.")

# Agregar m�s tareas o restricciones seg�n sea necesario
G.add_node("Tarea E")
G.add_edge("Tarea D", "Tarea E")

# Volver a encontrar un plan parcial
try:
    plan_parcial = list(nx.topological_sort(G))
    print("\nPlan parcial actualizado:")
    for tarea in plan_parcial:
        print(tarea)
except nx.NetworkXUnfeasible:
    print("No se puede encontrar un plan parcial debido a las restricciones.")
