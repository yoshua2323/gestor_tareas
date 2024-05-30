from tarea import Tarea

def agregar_tarea(lista_tareas):
    try:
        titulo = input("Ingrese el título de la tarea: ").strip()
        descripcion = input("Ingrese la descripción de la tarea: ").strip()
        nueva_tarea = Tarea(titulo, descripcion)
        lista_tareas.append(nueva_tarea)
        print("Tarea agregada exitosamente.")
    except Exception as e:
        print(f"Error al agregar la tarea: {e}")

def mostrar_todas_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas para mostrar.")
    else:
        for tarea in lista_tareas:
            print(tarea)

def buscar_tarea(lista_tareas):
    try:
        titulo = input("Ingrese el título de la tarea a buscar: ").strip().lower()
        for tarea in lista_tareas:
            if tarea.titulo.lower() == titulo:
                print(tarea)
                return
        print("Tarea no encontrada.")
    except Exception as e:
        print(f"Error al buscar la tarea: {e}")

def actualizar_estado_tarea(lista_tareas):
    try:
        titulo = input("Ingrese el título de la tarea a actualizar: ").strip().lower()
        for tarea in lista_tareas:
            if tarea.titulo.lower() == titulo:
                tarea.estado = 'completada'
                print("Estado de la tarea actualizado a completada.")
                return
        print("Tarea no encontrada.")
    except Exception as e:
        print(f"Error al actualizar la tarea: {e}")

def eliminar_tarea(lista_tareas):
    try:
        titulo = input("Ingrese el título de la tarea a eliminar: ").strip().lower()
        for tarea in lista_tareas:
            if tarea.titulo.lower() == titulo:
                lista_tareas.remove(tarea)
                print("Tarea eliminada exitosamente.")
                return
        print("Tarea no encontrada.")
    except Exception as e:
        print(f"Error al eliminar la tarea: {e}")

def buscar_tareas_por_estado(lista_tareas):
    try:
        estado = input("Ingrese el estado de las tareas a buscar (pendiente/completada): ").strip().lower()
        tareas_encontradas = [tarea for tarea in lista_tareas if tarea.estado.lower() == estado]
        if tareas_encontradas:
            for tarea in tareas_encontradas:
                print(tarea)
        else:
            print(f"No se encontraron tareas con el estado '{estado}'.")
    except Exception as e:
        print(f"Error al buscar tareas por estado: {e}")

def mostrar_menu():
    print("\nSistema de Gestión de Tareas")
    print("1. Agregar nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea por título")
    print("4. Actualizar estado de una tarea")
    print("5. Eliminar tarea por título")
    print("6. Buscar tareas por estado")
    print("7. Salir")
