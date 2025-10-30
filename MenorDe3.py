from typing import Union

def encontrar_menor_de_tres(num1: Union[int, float], num2: Union[int, float], num3: Union[int, float]) -> Union[int, float]:
    return min(num1, num2, num3)

# Teste #########################################################################
if __name__ == '__main__':
    
    # Teste 1
    a, b, c = 15, 8, 22
    menor = encontrar_menor_de_tres(a, b, c)
    print(f"Os números são: {a}, {b}, {c}")
    print(f"O menor número é: {menor}") # Saída: 8

    print("-" * 20)

    # Teste 2
    x, y, z = -5, 0, 100
    menor = encontrar_menor_de_tres(x, y, z)
    print(f"Os números são: {x}, {y}, {z}")
    print(f"O menor número é: {menor}") # Saída: -5