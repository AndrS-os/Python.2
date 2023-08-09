def numeros_pares(lista):
    lista_pares = [numero for numero in lista if numero % 2 == 0]
    return lista_pares

def main():
    try:
        numeros_str = input("Digite uma lista de números separados por espaço: ")
        lista_numeros = [int(numero) for numero in numeros_str.split()]
        
        lista_pares = numeros_pares(lista_numeros)
        print("Números pares:", lista_pares)
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar uma lista de números válida.")

if __name__ == "__main__":
    main()



