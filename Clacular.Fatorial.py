def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero < 0:
            print("O fatorial não está definido para números negativos.")
        else:
            fatorial = calcular_fatorial(numero)
            print(f"O fatorial de {numero} é: {fatorial}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro.")

if __name__ == "__main__":
    main()
