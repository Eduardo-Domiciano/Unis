from typing import Tuple

def converter_dias_para_idade(dias_totais: int) -> Tuple[int, int, int]:
    
    if dias_totais < 0:
        raise ValueError("A idade em dias não pode ser negativa.")

    # 1. Anos
    # // divide por anos
    anos = dias_totais // 365
    # O resto, vai ser usado para meses e dias
    dias_restantes = dias_totais % 365

    # 2.meses
    # // divide por meses
    meses = dias_restantes // 30
    
    # 3. Dias
    # São os dias que sobraram
    dias = dias_restantes % 30
    
    return anos, meses, dias

# Teste ##########################################################################################################3

if __name__ == '__main__':
    # testar
    try:
        entrada_dias = input("Digite a idade da pessoa em dias: ")
        dias = int(entrada_dias)
        
        anos, meses, dias_finais = converter_dias_para_idade(dias)
        
        print("\n--- Resultado da Conversão ---")
        print(f"Idade em dias: {dias}")
        print(f"Idade Convertida: {anos} anos, {meses} meses e {dias_finais} dias.")
        print("------------------------------")
        
    except ValueError as e:
        print(f"Erro: Entrada inválida. {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")