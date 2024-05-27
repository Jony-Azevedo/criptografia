# Código criptográfico usando a cifra de césar[3]
# idioma Português
alfabeto = {'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O', 'M': 'P',
            'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C'}

def descriptografar(mensagem, alfabeto):
    # Guarda valores das chaves
    mensagem_verdadeira = []

    # Itera sobre cada caractere da mensagem
    for caractere in mensagem:
        if caractere in alfabeto.values():
            for chave,valor in alfabeto.items():
                # encontra a chave correspondente ao valor
                if valor == caractere:
                    mensagem_verdadeira.append(chave)
                    break
        else:
            mensagem_verdadeira.append(caractere)  # mantém caractere original se não houver correspondencia no alfabeto usado

    return ''.join(mensagem_verdadeira)

mensagem = input("Digite a mensagem que deseja descriptografar: ").upper()

resultado = descriptografar(mensagem, alfabeto)
print(f'Texto descriptografado: {resultado.lower()}')
