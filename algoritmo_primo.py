# Programa que verifica se um número é primo

def eh_primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    numero = int(input("Digite um número: "))
    if eh_primo(numero):
        print(f"{numero} é primo")
    else:
        print(f"{numero} não é primo")

