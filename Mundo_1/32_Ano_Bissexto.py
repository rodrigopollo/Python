# Insira um ano qualquer
# O programa tem que detectar se eh bisexto ou nao.

ano = int(input("Digite o ano: "))

bissexto = ano % 4
excecao = ano % 100

if bissexto == 0 and excecao == 0 or bissexto != 0:
    print(f"O ano {ano} nao eh un ano bissexto")
else:
    print(f"O ano {ano} eh un ano bissexto")
