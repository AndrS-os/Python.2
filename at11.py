import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Tente um número maior.")
            elif palpite > numero_secreto:
                print("Tente um número menor.")
            else:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def main():
    jogo_adivinhacao()

if __name__ == "__main__":
    main()