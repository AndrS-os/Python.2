def calcular_soma_ate_100():
    soma = 0
    for numero in range(1, 101):
        soma += numero
    return soma

soma_ate_100 = calcular_soma_ate_100()
print(f"A soma dos números de 1 a 100 é: {soma_ate_100}")