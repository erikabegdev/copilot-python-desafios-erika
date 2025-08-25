# Programa que lê 3 números e calcula a soma deles

def soma_numeros(a, b, c):
    return a + b + c

if __name__ == "__main__":
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))

    resultado = soma_numeros(n1, n2, n3)
    print(f"A soma dos números é: {resultado}")

