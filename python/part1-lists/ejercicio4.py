import random
from typing import List

def generar_lista(n, lim1=1, lim2=-1) : 
    if (lim2 == -1) :
        lim2 = n
    l = []
    for i in range(n) :
        l.append(random.randint(lim1,lim2))
    
    return l

def combinar_listas(lista1: List[int], lista2: List[int]) -> List[int]:
    return lista1 + lista2


lista1 = generar_lista(5)
lista2 = generar_lista(5)

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'La función devuelve {combinar_listas(lista1, lista2)}')
