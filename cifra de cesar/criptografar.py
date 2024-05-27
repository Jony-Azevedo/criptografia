# Código criptográfico usando a cifra de césar[3]
# idioma Português

alfabeto = {'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O', 'M': 'P',
            'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C',
            'É':'H','È':'H','Ê':'H','Í':'L','Ì':'L','Î':'L','Á':'D','À':'D','Â':'D','Ã':'D','Ó':'R','Ò':'R','Ô':'R','Õ':'R',
            'Ú':'X','Ù':'X','Ç':'@'}

def criptografar(mensagem, alfabeto):
    # Guarda valores das chaves
    mensagem_criptografada = []

    # Itera sobre cada caractere da mensagem
    for caractere in mensagem:
        if caractere in alfabeto:
            mensagem_criptografada.append(alfabeto[caractere])
        else:
            mensagem_criptografada.append(caractere)  # mantém caractere original se não houver correspondencia no alfabeto usado

    return ''.join(mensagem_criptografada)

mensagem = input("Digite a mensagem que deseja criptografar: ").upper()

resultado = criptografar(mensagem, alfabeto)
print(f'Texto criptografado: {resultado.lower()}')
