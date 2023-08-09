def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    try:
        escolha = int(input("Escolha a conversão:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n"))

        if escolha == 1:
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"{celsius:.2f}°C é igual a {fahrenheit:.2f}°F")

            elif escolha == 2:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit:.2f}°F é igual a {celsius:.2f}°C")

        else:
            print("Escolha inválida. Digite 1 ou 2 para escolher a conversão.")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número válido.")

if __name__ == "__main__":
    main()