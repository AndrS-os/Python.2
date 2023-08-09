def ordenar_crescente(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    return lista_ordenada

def main():
    try:
        numeros_str = input("Digite uma lista de números separados por espaço: ")
        lista_numeros = [float(numero) for numero in numeros_str.split()]

        lista_ordenada = ordenar_crescente(lista_numeros)
        print("Lista ordenada de forma crescente:", lista_ordenada)

        except ValueError:
        print("Entrada inválida. Certifique-se de digitar uma lista válida de números.")

if __name__ == "__main__":
    main()