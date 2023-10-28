pip install pycosat

import pycosat

# Definir un problema SAT en forma CNF (Forma Normal Conjuntiva)
def problema_satplan():
    # Variables proposicionales
    a = 1
    b = 2

    # Cl�usulas CNF
    clausulas = [
        [a],          # Cl�usula 1: a
        [-a, b],      # Cl�usula 2: no a o b
        [-b]          # Cl�usula 3: no b
    ]

    return clausulas

# Resolver el problema SAT utilizando pycosat
clausulas = problema_satplan()
solucion = pycosat.solve(clausulas)

# Mostrar el resultado
if solucion is not None:
    print("Plan encontrado:")
    plan = [variable for variable in solucion if variable > 0]
    for variable in plan:
        print(f"Variable {variable} es verdadera en el plan.")
else:
    print("No se encontr� un plan.")
