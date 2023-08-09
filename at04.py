def eh_palindromo(palavra):
    palavra = palavra.lower()  # Converte a palavra para minúsculas
    palavra = palavra.replace(" ", "")  # Remove os espaços em branco

    return palavra == palavra[::-1]  # Compara a palavra original com ela invertida

def main():
    palavra = input("Digite uma palavra: ")
    if eh_palindromo(palavra):
        print(f"{palavra} é um palíndromo.")
    else:
        print(f"{palavra} não é um palíndromo.")

if __name__ == "__main__":
    main()