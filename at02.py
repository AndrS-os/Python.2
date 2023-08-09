def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0  # Retorna 0 se a lista estiver vazia para evitar divisão por zero

    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    return media

def main():
    try:
        numeros_input = input("Digite uma lista de números separados por espaço: ")
        numeros_str = numeros_input.split()
        numeros = [float(numero) for numero in numeros_str]

        media_resultado = calcular_media(numeros)
        print(f"A média dos números é: {media_resultado:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar uma lista de números válida.")

if __name__ == "__main__":
    main()





