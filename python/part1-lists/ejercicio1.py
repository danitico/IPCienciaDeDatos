import random
from typing import List


def generar_lista(n, lim1=1, lim2=-1) : 
    if (lim2 == -1) :
        lim2 = n
    l = []
    for i in range(n) :
        l.append(random.randint(lim1,lim2))
    
    return l

def sum_nums_lista(numeros: List[int]) -> int:
    suma = 0

    for item in numeros:
        suma += item
    
    return suma

lista = generar_lista(10)

print(f'Lista: {lista}')
print(f'La suma de los números es {sum_nums_lista(lista)}')
