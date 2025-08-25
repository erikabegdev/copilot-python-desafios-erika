# Programa que calcula o fatorial de um número

def fatorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

if __name__ == "__main__":
    numero = int(input("Digite um número: "))
    print(f"O fatorial de {numero} é {fatorial(numero)}")
