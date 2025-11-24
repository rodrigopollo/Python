
def valida_nome(mensagem: str) -> str:
    while True:
        entrada = input(mensagem).strip().capitalize()

        if entrada.replace(" ", "").isalpha():
            return entrada
        print("\033[0;31mERROR: Digite um nome valido (apenas letras).\033[0m")
        print("-" * 45)

