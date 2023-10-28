from queue import Queue

# Definir una funci�n para verificar si un estado es objetivo
def es_objetivo(estado):
    return estado == "Objetivo"

# Definir una funci�n para generar sucesores de un estado dado
def generar_sucesores(estado):
    # En este ejemplo, simplemente generamos sucesores agregando un n�mero
    return [estado + 1, estado + 2]

# Definir el estado inicial
estado_inicial = 0

# Crear una cola para la b�squeda en amplitud
cola = Queue()
cola.put(estado_inicial)

# Realizar una b�squeda en amplitud en el espacio de estados
while not cola.empty():
    estado_actual = cola.get()

    if es_objetivo(estado_actual):
        print(f"Se encontr� el estado objetivo: {estado_actual}")
        break

    sucesores = generar_sucesores(estado_actual)
    for sucesor in sucesores:
        cola.put(sucesor)
