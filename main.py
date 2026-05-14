from notas import agregar_nota, mostrar_notas, eliminar_nota

notas = []

while True:
    print("\n--- GESTOR DE NOTAS ---")
    print("1. Añadir nota")
    print("2. Mostrar notas")
    print("3. Eliminar nota")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        texto = input("Introduce la nota: ")
        agregar_nota(notas, texto)

    elif opcion == "2":
        mostrar_notas(notas)

    elif opcion == "3":
        eliminar_nota(notas)

    elif opcion == "4":
        print("Programa finalizado")
        break

    else:
        print("Opción incorrecta")