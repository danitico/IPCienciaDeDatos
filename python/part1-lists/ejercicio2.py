import random
from typing import List

def generar_lista(n, lim1=1, lim2=-1) : 
    if (lim2 == -1) :
        lim2 = n
    l = []
    for i in range(n) :
        l.append(random.randint(lim1,lim2))
    
    return l

def contar_numeros_impares(numeros: List[int]) -> int:
    count = 0

    for item in numeros:
        if item % 2 == 1:
            count += 1

    return count

lista = generar_lista(10)

print(f'Lista: {lista}')
print(f'Hay {contar_numeros_impares(lista)} números impares')
