pip install graphplan

from graphplan import Action, Problem

# Definir acciones
acciones = [
    Action('Acci�n1', precondiciones={'A'}),
    Action('Acci�n2', precondiciones={'B'}),
    Action('Acci�n3', precondiciones={'A', 'B'}, efectos={'C'}),
    Action('Acci�n4', precondiciones={'C'}, efectos={'D'}),
]

# Definir un problema
problema = Problem(
    acciones,
    estado_inicial={'A', 'B'},
    estado_objetivo={'D'}
)

# Resolver el problema utilizando GRAPHPLAN
solucion = problema.graphplan()

# Mostrar la soluci�n
if solucion:
    print("Plan encontrado:")
    for nivel, acciones in enumerate(solucion):
        print(f"Nivel {nivel}: {', '.join(acciones)}")
else:
    print("No se encontr� un plan.")
