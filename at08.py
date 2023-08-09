def encontrar_maior_menor_palavra(lista_palavras):
    if not lista_palavras:
        return None, None  # Retorna None se a lista estiver vazia

    maior_palavra = min(lista_palavras, key=len)
    menor_palavra = max(lista_palavras, key=len)
    return maior_palavra, menor_palavra

def main():
    try:
        num_palavras = int(input("Quantas palavras você deseja inserir? "))
        lista_palavras = []

        for i in range(num_palavras):
            palavra = input(f"Digite a palavra {i+1}: ")
            lista_palavras.append(palavra)

        maior, menor = encontrar_maior_menor_palavra(lista_palavras)

        if maior is None or menor is None:
            print("Lista vazia. Não é possível encontrar maior e menor palavra.")
        else:
            print(f"Maior palavra: {maior}")
            print(f"Menor palavra: {menor}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro.")

if __name__ == "__main__":
    main()



