# Leia 2 valores
# Mostre os seguintes itens no menu:
# Soma, multiplicar, maior, novos numeros, sair.

opcao = None

while opcao != 5:
    print("Digite 2 numeros!")
    n1 = int(input("1º numero: "))
    n2 = int(input("2º numero: "))
    print("=" * 40)
    print('''Escolha a operaçao:
    [1] - Soma
    [2] - Multiplicaçao
    [3] - Verificar o maior numero
    [4] - Inserir novos numeros
    [5] - Sair do Programa. ''')
    print("=" * 40)

    opcao = int(input("Qual operaçao deseja realizar: "))

    if opcao == 1:
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")
        print("-" * 40)
    elif opcao == 2:
        mult = n1 * n2
        print(f"{n1} x {n2} = {mult}")
        print("-" * 40)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f"O maior numero eh o {n1}")
            print("-" * 40)
        else:
            maior = n2
            print(f"O maior numero eh o {n2}")
            print("-" * 40)
    elif opcao == 4:
        print("-" * 40)
        continue
    elif opcao == 5:
        print("\nEstou fechando o programa.")
        exit()
    else:
        print("ERROR: Opçao invalida, selecione as opçoes entre 1 e 5 do menu.")
        print("-" * 40)





