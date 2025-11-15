# Usar modulos.
# Cadastra NOME e IDADE das pessoas e armazena em algum lugar.
# Fazer um menu que o usuario possa escolher oq quer fazer, VER PESSOAS CADASTRADAS, Cadastrar ou sair.

from cadastros.nome.nomes_cadastrados import valida_nome
from cadastros.idade.idade_cadastradas import valida_idade
from cadastros.menu.opcao import mostrar_menu, ler_opcao_menu

novo_cadastro = dict()
pessoas_cadastradas = list()

while True:
    mostrar_menu()
    escolha = ler_opcao_menu()

    if escolha == 1:
        if not pessoas_cadastradas:
            print("\033[0;31mERRO: Ainda nao foi cadastrado nenhuma pessoa.\033[0m")
        else:
            print("-=" * 20)
            print(f"{'PESSOAS CADASTRADAS':^35}")
            print("-=" * 20)
            for pessoa in pessoas_cadastradas:
                print(f"{pessoa['nome']:<30}{pessoa['idade']} anos")

    elif escolha == 2:
        nome_input = valida_nome("Digite seu nome: ")
        idade_input = valida_idade("Digite sua idade: ")

        novo_cadastro['nome'] = nome_input
        novo_cadastro['idade'] = idade_input
        pessoas_cadastradas.append(novo_cadastro.copy())

    elif escolha == 3:
        break