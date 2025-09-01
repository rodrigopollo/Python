# leia nome, idade e sexo de 2 pessoas
# Mostre: A media da idade
# Mostre: Nome do homem mais velho (se tiver)
# Mostre: Quantas mulheres tem mais de 20 anos.

qtd_pessoas = 2  # numero de vezes que o for ira funcionar

idade_total = 0
mais_velho = -1
nome_velho = None
mulher = 0

for i in range(qtd_pessoas):
    nome = input("Insira um nome: ").strip()
    idade = int(input("Qual a idade: "))
    sexo = input("Qual o sexo (m/f): ").strip().lower()
    print("-" * 20)

    # valida idade antes de usar
    if idade <= 0:
        print("ERRO: IDADE INVÁLIDA (TEM QUE SER MAIOR QUE 0)")
        continue  # volta para o próximo cadastro sem considerar este

    # acumula idade só se válida
    idade_total += idade

    # atualiza homem mais velho
    if sexo == "m" and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome

    # conta mulheres com mais de 20
    if sexo == "f" and idade > 20:
        mulher += 1

# média com base na quantidade configurada
media = idade_total / qtd_pessoas if qtd_pessoas > 0 else 0

print("\n" + " Resultado da pesquisa ".center(30) + "\n")
print("-=" * 30)
print(f"A média de idade do grupo é de {media:.1f}")

if nome_velho is not None:
    print(f"O homem mais velho foi {nome_velho} com {mais_velho} anos")
else:
    print("Não houve homens cadastrados.")

print(f"Nesta pesquisa encontramos {mulher} mulher(es) com mais de 20 anos de idade.")
print("-=" * 30)





