def selection_sort(desordeado: list[int]):
    tamanho = len(desordeado)
    # Segue o vetor inteiro
    for i in range(tamanho-1):
        # Seleciona o primeiro do array que não foi mudado ainda
        indice_menor: int = i
        # Segue pelo array procurando o menor valor que ainda não foi ordenado
        for index in range(i, tamanho):
            # Seleciona o indice do menor valor do array
            if desordeado[index] < desordeado[indice_menor]:
                indice_menor = index
        # Apenas muda o lugar dos dois
        mudar_valor(desordeado, i, indice_menor)


def mudar_valor(desordenado: list[int], primeiro: int, segundo: int):
    desordenado[primeiro], desordenado[segundo] = desordenado[segundo], desordenado[primeiro]


if __name__ == "__main__":
    des = [9, 20, 17, 10, 18, 25, 25, 15, 2, 15, 17, 17, 16, 11, 3, 11, 25, 16, 12, 22, 24, 14, 8, 16, 21, 27, 27, 18, 1, 29, 16, 10, 0, 2, 2, 26, 19, 9, 12, 24, 20, 3, 16, 4, 4, 11, 9, 21, 25,
           6, 25, 10, 29, 20, 17, 23, 3, 26, 0, 30, 4, 20, 7, 11, 11, 19, 21, 4, 24, 13, 9, 29, 10, 22, 6, 28, 29, 28, 22, 10, 17, 3, 1, 1, 18, 2, 3, 11, 12, 28, 28, 7, 30, 25, 17, 28, 21, 12, 5, 12]
    print(des)

    selection_sort(des)
    print(des)
