# Función para añadir una nueva nota a la lista (Commit 2)
def agregar_nota(lista, texto):
    lista.append(texto)
    print("Nota añadida correctamente")

# Función para visualizar todas las notas guardadas (Commit 2)
def mostrar_notas(lista):
    if len(lista) == 0:
        print("No hay notas guardadas")
    else:
        print("\nLISTA DE NOTAS")
        for i, nota in enumerate(lista):
            print(f"{i + 1}. {nota}")

# Función para eliminar una nota con validación de errores (Commit 4)
def eliminar_nota(lista):
    mostrar_notas(lista)

    if len(lista) > 0:
        try:
            indice = int(input("Número de nota a eliminar: ")) - 1
            if 0 <= indice < len(lista):
                lista.pop(indice)
                print("Nota eliminada")
            else:
                print("Número incorrecto: la nota no existe")
        except ValueError:
            # Si el usuario introduce letras en lugar de números (Commit 4)
            print("Error: Debes introducir un número válido")

# Nueva funcionalidad: Cuenta el total de notas (Commit 5)
def contar_notas(lista):
    total = len(lista)
    print(f"Tienes un total de {total} notas.")