import time

# Funci�n que representa una tarea a vigilar
def tarea_a_vigilar():
    for i in range(5):
        print(f"Ejecutando paso {i + 1} de la tarea...")
        time.sleep(1)  # Simula una espera de 1 segundo por paso
    print("Tarea completada")

# Funci�n de vigilancia de ejecuci�n
def vigilancia_ejecucion():
    tarea_iniciada = False
    while True:
        if not tarea_iniciada:
            print("Iniciando la tarea a vigilar...")
            tarea_iniciada = True
            tarea_a_vigilar()  # Iniciar la tarea
        else:
            print("La tarea est� en progreso...")
            time.sleep(1)  # Esperar 1 segundo
            estado = "completada" if tarea_completada() else "en progreso"
            print(f"Estado de la tarea: {estado}")

            if tarea_completada():
                break

# Funci�n que simula verificar si la tarea ha sido completada
def tarea_completada():
    # En este ejemplo, asumimos que la tarea se ha completado despu�s de 5 segundos.
    return time.time() - inicio_tiempo >= 5

inicio_tiempo = time.time()
vigilancia_ejecucion()

#Vigilancia de replanificaci�n

import time

# Funci�n que representa una tarea a ejecutar
def tarea():
    for i in range(3):
        print(f"Ejecutando paso {i + 1} de la tarea...")
        time.sleep(1)  # Simula una espera de 1 segundo por paso
    print("Tarea completada")

# Funci�n de vigilancia y replanificaci�n
def vigilancia_replanificacion():
    tarea_iniciada = False
    intentos = 0

    while True:
        if not tarea_iniciada:
            print("Iniciando la tarea...")
            tarea_iniciada = True
            tarea()  # Iniciar la tarea
        else:
            print("La tarea est� en progreso...")
            time.sleep(1)  # Esperar 1 segundo
            estado = "completada" if tarea_completada() else "en progreso"
            print(f"Estado de la tarea: {estado}")

            if tarea_completada():
                print("Tarea completada con �xito.")
                break
            else:
                print("�Se ha detectado un problema!")
                intentos += 1

                if intentos < 3:
                    print(f"Intento {intentos}: Replanificando la tarea...")
                    replanificar_tarea()
                else:
                    print("Se han agotado los intentos. La tarea no se puede completar.")
                    break

# Funci�n que simula verificar si la tarea ha sido completada
def tarea_completada():
    # En este ejemplo, asumimos que la tarea se ha completado despu�s de 3 segundos.
    return time.time() - inicio_tiempo >= 3

# Funci�n de replanificaci�n
def replanificar_tarea():
    print("Realizando una replanificaci�n...")
    # En un caso real, podr�as llamar a un sistema de planificaci�n para generar un nuevo plan.

inicio_tiempo = time.time()
vigilancia_replanificacion()
