from funciones import agregar_tarea, mostrar_todas_tareas, buscar_tarea, actualizar_estado_tarea, eliminar_tarea, buscar_tareas_por_estado, mostrar_menu

def main():
    lista_tareas = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            agregar_tarea(lista_tareas)
        elif opcion == '2':
            mostrar_todas_tareas(lista_tareas)
        elif opcion == '3':
            buscar_tarea(lista_tareas)
        elif opcion == '4':
            actualizar_estado_tarea(lista_tareas)
        elif opcion == '5':
            eliminar_tarea(lista_tareas)
        elif opcion == '6':
            buscar_tareas_por_estado(lista_tareas)
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
