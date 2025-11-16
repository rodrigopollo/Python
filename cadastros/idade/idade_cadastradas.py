
def valida_idade(mensagem: str) -> int:
    while True:
        entrada = input(mensagem).strip()

        try:
            idade = int(entrada)
            if 0 < idade < 140:
                return idade
            else:
                print("\033[0;31mERROR: Digite uma idade valida (entre 0 e 140).\033[0m")
        except ValueError:
            print("\033[0;31mERROR: Digite apenas numeros sem nenhum tipo de sinal.\033[0m")
