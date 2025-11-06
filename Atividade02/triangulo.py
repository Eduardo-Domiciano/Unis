from typing import Union, Tuple
import math

# Função que verifica

def eh_triangulo(a: int, b: int, c: int) -> bool:
    # Verifica se os valores sao inteiros e positivos antes do role todo começar
    if a <= 0 or b <= 0 or c <= 0:
        return False
        
    # Verifica caso desigualdade triangular nos valores
    condicao1 = a < (b + c)
    condicao2 = b < (a + c)
    condicao3 = c < (a + b)
    return condicao1 and condicao2 and condicao3

# Calcula area

def calcular_area_herao(a: int, b: int, c: int) -> float:
    """
    Sa porra toda é IA, eu nnunca tinha ouvido falar, Mas FORMULA DE HERÃO, ta na minha lista de estudo
    
    Calcula a área de um triângulo utilizando a Fórmula de Herão.
    
    A Fórmula de Herão exige o semi-perímetro (s): s = (a + b + c) / 2
    Área = sqrt(s * (s - a) * (s - b) * (s - c))

    Args:
        a, b, c: Comprimentos dos lados.

    Returns:
        A área do triângulo (float).
    """
    # Calcula o semi-perímetro (s)
    s = (a + b + c) / 2
    
    # Calcula o valor dentro da raiz quadrada
    area_quadrado = s * (s - a) * (s - b) * (s - c)
    
    # Nota: Se eh_triangulo for True, area_quadrado deve ser >= 0.
    return math.sqrt(area_quadrado)

# --- 3. FUNÇÃO PRINCIPAL QUE INTEGRA A LÓGICA ---

def processar_triangulo(a: int, b: int, c: int) -> Union[Tuple[int, int, int], float]:
    """
    Verifica se os valores formam um triângulo e calcula a área, se for o caso.

    Args:
        a, b, c: Os três valores lidos (inteiros positivos).

    Returns:
        - A área do triângulo (float) se formar um triângulo.
        - Uma tupla (a, b, c) com os valores lidos se NÃO formar um triângulo.
    """
    try:
        # Garante que os valores são positivos antes de continuar
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Todos os valores devem ser inteiros e positivos.")

        if eh_triangulo(a, b, c):
            # Se formar, calcula a área
            area = calcular_area_herao(a, b, c)
            return area
        else:
            # Se não formar, retorna os valores lidos
            return (a, b, c)
            
    except ValueError as e:
        # Retorna o erro para ser tratado pela função chamadora (opcional)
        return str(e)


# Teste ###########################################################################################

if __name__ == '__main__':
    
    print("--- Teste 1: Forma um Triângulo (3, 4, 5) ---")
    lado_a, lado_b, lado_c = 3, 4, 5
    resultado = processar_triangulo(lado_a, lado_b, lado_c)
    
    if isinstance(resultado, float):
        print(f"Os valores {lado_a}, {lado_b}, {lado_c} formam um triângulo.")
        print(f"Área Calculada: {resultado:.2f}")
    else:
        print(f"Os valores {resultado} não formam um triângulo.")
        
    print("\n--- Teste 2: Não Forma Triângulo (10, 2, 3) ---")
    lado_a, lado_b, lado_c = 10, 2, 3
    resultado = processar_triangulo(lado_a, lado_b, lado_c)
    
    if isinstance(resultado, float):
        print(f"Os valores {lado_a}, {lado_b}, {lado_c} formam um triângulo.")
        print(f"Área Calculada: {resultado:.2f}")
    elif isinstance(resultado, tuple):
        print(f"Os valores {resultado} não formam um triângulo.")
    else:
        print(f"Erro: {resultado}")