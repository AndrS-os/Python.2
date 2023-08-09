def imprimir_numeros_naturais(n):
    if n < 0:
        print("O número precisa ser positivo.")
    else:
        for i in range(n + 1):
            print(i, end=" ")

def main():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        imprimir_numeros_naturais(numero)
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro positivo.")

if __name__ == "__main__":
    main()