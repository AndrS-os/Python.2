def calcular_mediana(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    tamanho = len(lista_ordenada)

    if tamanho % 2 == 0:
        meio1 = lista_ordenada[tamanho // 2 - 1]
        meio2 = lista_ordenada[tamanho // 2]
        mediana = (meio1 + meio2) / 2
    else:
        mediana = lista_ordenada[tamanho // 2]

    return mediana

    def main():
    try:
        numeros_str = input("Digite uma lista de números separados por espaço: ")
        lista_numeros = [float(numero) for numero in numeros_str.split()]

        mediana = calcular_mediana(lista_numeros)
        print(f"A mediana dos números é: {mediana:.2f}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar uma lista válida de números.")

if __name__ == "__main__":
    main()