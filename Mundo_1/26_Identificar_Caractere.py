# Leia um nome
# Quantas vezes aparece A
# Em que posiçao A aparece pela primeira vez
# E em qual posiçao aparece a letra "a" pela ultima vez.


nome = input("Digite um nome: ").strip().lower()

qntas_Letras = len(nome)
qntos_A = nome.count("a")
primeiro_A = nome.find("a")
ultimo_A = nome.rfind("a")

print(f"O nome digitado tem: {qntas_Letras} letras")
print(f"O nome digitado tem {qntos_A} letras A")
print(f"A index da primeira letra A no nome eh: {primeiro_A}")
print(f"O index da ultima letra A no nome eh: {ultimo_A}")
