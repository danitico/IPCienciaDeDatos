from typing import List


def imprimir_matriz(matriz: List[List[int]]) -> None:
    for filas in matriz:
        for item in filas:
            print(item, end=' ')
        
        print()

def traspuesta(matriz: List[List[int]]) -> List[List[int]]:
    return [list(column) for column in zip(*matriz)]

matriz = [
    [1, 2],
    [3, 4]
]

print('Matriz original:')
imprimir_matriz(matriz)

matriz_traspuesta = traspuesta(matriz)

print('Matriz traspuesta:')
imprimir_matriz(matriz_traspuesta)
