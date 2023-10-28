class Tarea:
    def __init__(self, nombre, subtareas=None):
        self.nombre = nombre
        self.subtareas = subtareas if subtareas is not None else []

    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)

    def __str__(self):
        return self.nombre

# Crear tareas y organizarlas en una red jer�rquica
tarea_principal = Tarea("Tarea Principal")
subtarea_1 = Tarea("Subtarea 1")
subtarea_2 = Tarea("Subtarea 2")
subtarea_3 = Tarea("Subtarea 3")

tarea_principal.agregar_subtarea(subtarea_1)
tarea_principal.agregar_subtarea(subtarea_2)
subtarea_2.agregar_subtarea(subtarea_3)

# Funci�n para imprimir la jerarqu�a de tareas
def imprimir_jerarquia(tarea, nivel=0):
    print("  " * nivel + f"- {tarea}")
    for subtarea in tarea.subtareas:
        imprimir_jerarquia(subtarea, nivel + 1)

# Imprimir la jerarqu�a de tareas
print("Jerarqu�a de tareas:")
imprimir_jerarquia(tarea_principal)
