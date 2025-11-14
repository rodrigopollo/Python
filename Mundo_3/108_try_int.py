
def valida_numero_inteiro(mensagem: str) -> int:
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            return 0

        try:
            numero = int(entrada)

            if numero >= 0:
                return numero
            else:
                numero_negativo = "\033[0;31mERROR: Numero negativo.\033[0m"
                print(numero_negativo)
                print("-" * len(numero_negativo))
        except ValueError:
            texto = "\033[0;31mERROR: Digite apenas numeros inteiros com valor igual ou maior que Zero.\033[0m"
            print(texto)
            print("-" * len(texto))


def valida_numero_real(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).replace(',', '.').strip()

        if not entrada:
            return 0

        try:
            numero = float(entrada)
            if numero >= 0:
                return numero
            else:
                numero_negativo = "\033[0;31mERROR: Numero negativo.\033[0m"
                print(numero_negativo)
                print("-" * len(numero_negativo))
        except ValueError:
            texto = "\033[0;31mERROR: Digite apenas numeros com valor igual ou maior que Zero.\033[0m"
            print(texto)
            print("-" * len(texto))


numero_inteiro = valida_numero_inteiro("Digite um numero inteiro: ")
numero_real = valida_numero_real("Digite um numero real: ")
print("-=" * 13)
print(f"Numero inteiro: {numero_inteiro}")
print(f"Numero real: {numero_real}")










