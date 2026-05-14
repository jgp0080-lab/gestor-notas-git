from notas import agregar_nota, mostrar_notas, eliminar_nota, contar_notas
from utilidades import mostrar_titulo # Importación del Commit 1

notas = []

# Llamada a la función del archivo utilidades (Commit 1)
mostrar_titulo()

while True:
    print("\n========================")
    print("--- GESTOR DE NOTAS ---")
    print("========================")
    print("1. Añadir nota")
    print("2. Mostrar notas")
    print("3. Eliminar nota")
    print("4. Ver total de notas") # Opción para el Commit 5
    print("5. Salir")

    opcion = input("\nSelecciona una opción: ") # Diseño mejorado (Commit 3)

    if opcion == "1":
        texto = input("Introduce la nota: ")
        agregar_nota(notas, texto)

    elif opcion == "2":
        mostrar_notas(notas)

    elif opcion == "3":
        eliminar_nota(notas)

    elif opcion == "4":
        contar_notas(notas) # Uso de la nueva función (Commit 5)

    elif opcion == "5":
        print(">>> Programa finalizado. ¡Hasta pronto! <<<")
        break

    else:
        print("!!! Opción incorrecta, intenta de nuevo !!!") # Diseño (Commit 3)


def buscar_nota(lista):
    termino = input("Introduce el texto a buscar: ").lower()
    encontradas = [n for n in lista if termino in n.lower()]
    print(f"Resultados: {encontradas}")