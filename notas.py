def agregar_nota(lista, texto):
    lista.append(texto)
    print("Nota añadida correctamente")


def mostrar_notas(lista):
    if len(lista) == 0:
        print("No hay notas guardadas")
    else:
        print("\nLISTA DE NOTAS")
        for i, nota in enumerate(lista):
            print(f"{i + 1}. {nota}")


def eliminar_nota(lista):
    mostrar_notas(lista)

    if len(lista) > 0:
        indice = int(input("Número de nota a eliminar: ")) - 1

        if 0 <= indice < len(lista):
            lista.pop(indice)
            print("Nota eliminada")
        else:
            print("Número incorrecto")