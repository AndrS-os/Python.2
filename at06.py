import random

def lancar_dado():
    return random.randint(1, 6)

def main():
    input("Pressione Enter para lançar os dados...")
    
    dado1 = lancar_dado()
    dado2 = lancar_dado()
    
    print(f"Resultado do dado 1: {dado1}")
    print(f"Resultado do dado 2: {dado2}")
    print(f"Soma dos valores: {dado1 + dado2}")

if __name__ == "__main__":
    main()