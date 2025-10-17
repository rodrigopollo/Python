# Leia nome, sexo e idade de varias pessoas.
# Cada cadastro em um dicionario e todos os dicionarios dentro de 1 lista.
# Mostre: quantas pessoas foram cadastradas
# Mostre: A media de idade das pessoas entrevistadas
# Mostre: Uma lista de todas as mulheres.
# Mostre: Uma lista om as pessoas com idade acima da media.

pessoa = dict()
lista_de_pessoas = list()
contador = 0
soma_idade = 0

while True:
    pessoa.clear()
    nome = str(input("Nome: ")).strip().title()
    idade = int(input("Idade: "))

    # Condiçao da idade estar entre 0 e 150
    while idade < 0 or idade > 150:
        print("Idade deve estar entra 0 e 150!")
        idade = int(input("Idade: "))

    # Condiçao do sexo cadastrado.
    while True:
        sexo = str(input("Sexo: [M/F]: ")).strip().lower()
        if sexo in ("m", "masculino", "f", "feminino"):
            if sexo in ("m", "masculino"):
                sexo = "M"
            else:
                sexo = "F"
            break
        else:
            print("Opçao invalida: Digite M ou F.")
    contador += 1

    # Adiciona a informaçao da pessoa em 1 dicionario, depois em uma lista com todos os entrevistados.
    pessoa = {"nome": nome, "idade": idade, "sexo": sexo}
    lista_de_pessoas.append(pessoa.copy())

    # Verifica a media da idade das pessoas entrevistadas.
    soma_idade += idade
    media_idade = soma_idade / contador

    # Condiçao de saida.
    sair = None
    while sair not in ("s", "n", "sim", "nao"):
        sair = str(input("Deseja continuar? [S/N]: ")).strip().lower()

    if sair in ("n", "nao"):
        break

print("-=" * 50)
print(f"Durante o evento foram cadastradas {contador} pessoas.")
print(f"Media de idade dos entrevistados: {media_idade:.0f} anos.")

print("As mulheres cadastradas foram: ")
for pessoa in lista_de_pessoas:
    if pessoa["sexo"] == "F":
        print(f" - {pessoa['nome']} com {pessoa['idade']} anos de idade")
print()
print("Pessoas com idade maior que a media das pessoas entrevistadas: ")
for pessoa in lista_de_pessoas:
    if pessoa["idade"] > media_idade:
        print(f" - {pessoa['nome']} com {pessoa['idade']} anos do sexo({pessoa['sexo']})")
print("-=" * 50)
