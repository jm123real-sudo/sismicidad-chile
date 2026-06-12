def merge_sort(lista):

    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2

    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return combinar(izquierda, derecha)


def combinar(izquierda, derecha):

    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):

        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1

        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado