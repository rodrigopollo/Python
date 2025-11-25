def mostrar_menu():
    print('-'*30)
    print("1. Ver pessoas cadastradas")
    print("2. Cadastrar uma nova pessoa")
    print("3. Sair do programa")
    print('-'*30)


def ler_opcao_menu():
    while True:
        try:
            opcao = int(input('Digite uma opcao desejada (1 - 3): '))
            if opcao in (1, 2, 3):
                return opcao
            print("ERRO: Opçao invalida!")
        except ValueError:
            print("ERROR: Digite apenas numeros inteiros!")


