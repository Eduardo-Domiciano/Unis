
def inverter_letras_por_palavra(frase: str) -> str:
    # pega a frase e transforma em uma lista de palavras
    palavras = frase.split()
    palavras_invertidas = []
    
    #inverte as palavras
    for palavra in palavras:
        palavra_invertida = palavra[::-1]
        palavras_invertidas.append(palavra_invertida)
    nova_frase = " ".join(palavras_invertidas)
    return nova_frase


# Teste ###########################################################################

if __name__ == '__main__':
    
    frase_teste = "Python e Kivy sao poderosos"
    resultado = inverter_letras_por_palavra(frase_teste)
    
    print(f"Frase Original: {frase_teste}")
    print(f"Frase Invertida: {resultado}") 
    # Saída esperada: "nohtyP e yviK oas sosoredoP"

    print("-" * 20)

    frase_curta = "Eu sou Gemini"
    resultado_curto = inverter_letras_por_palavra(frase_curta)
    print(f"Frase Curta Original: {frase_curta}")
    print(f"Frase Curta Invertida: {resultado_curto}")
    # Saída esperada: "uE uos inimeG"