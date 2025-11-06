import math

def eh_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    # testar se divide por 2
    if n % 2 == 0:
        return False
        
    # Busquei na IA como chegar nos numeros primos e me devolveu esse teste. Eu realmente falhei em entener coomo ele conse4gue fazer o teste de divisão e checar se de fato sobra. os testes passaram, então funciona, mas mesmo os videos que ue vi nao conseguiram me ajudar a entender o que acontece aqui.
    limite = int(math.sqrt(n))
    
    
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False
    # Se passar é primo
    return True


# teste #############################################################################

if __name__ == '__main__':
    
    # Teste para 17 (Primo)
    num1 = 17
    print(f"O número {num1} é primo? {eh_primo(num1)}") # Saída: True

    print("-" * 20)
    
    # Teste para 15 (Não Primo)
    num2 = 15
    print(f"O número {num2} é primo? {eh_primo(num2)}") # Saída: False
    
    print("-" * 20)
    
    # Teste para 1 (Não Primo)
    num3 = 1
    print(f"O número {num3} é primo? {eh_primo(num3)}") # Saída: False