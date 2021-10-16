import random
from typing import List

def generar_lista(n, lim1=1, lim2=-1) : 
    if (lim2 == -1) :
        lim2 = n
    l = []
    for i in range(n) :
        l.append(random.randint(lim1,lim2))
    
    return l

def numeros_pares(numeros: List[int]) -> int:
    return [item for item in numeros if item % 2 == 0]


lista = generar_lista(10)

print(f'Lista: {lista}')
print(f'Los números pares son {numeros_pares(lista)}')
