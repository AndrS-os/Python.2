import string
from collections import Counter

def contar_palavras(texto):
    texto = texto.lower()  # Converter para minúsculas para considerar palavras iguais independentemente de maiúsculas/minúsculas
    texto = texto.translate(str.maketrans("", "", string.punctuation))  # Remover pontuação
    palavras = texto.split()

    contador = Counter(palavras)
    return contador

def main():
    texto = input("Digite um texto: ")
    contador_palavras = contar_palavras(texto)

    print("Contagem de ocorrências de palavras:")
    for palavra, quantidade in contador_palavras.items():
        print(f"{palavra}: {quantidade}")

if __name__ == "__main__":
    main()