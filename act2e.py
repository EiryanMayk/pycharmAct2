def inverte_palavras(frase):

    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    return ' '.join(palavras_invertidas)

frase = input("Digite uma frase: ")
frase_invertida = inverte_palavras(frase)

print(f"Frase invertida: {frase_invertida}")