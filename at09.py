def converter_para_maiusculas(lista_strings):
    lista_maiusculas = [palavra.upper() for palavra in lista_strings]
    return lista_maiusculas

def main():
    try:
        num_strings = int(input("Quantas strings você deseja inserir? "))
        lista_strings = []

        for i in range(num_strings):
            string = input(f"Digite a string {i+1}: ")
            lista_strings.append(string)

        lista_maiusculas = converter_para_maiusculas(lista_strings)

        print("Lista em maiúsculas:", lista_maiusculas)

        except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro.")

if __name__ == "__main__":
    main()