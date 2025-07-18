
# Um programa que leia 2 notas de um aluno:
# Calcule e mostre a media entre as 2 notas.

nome = input("Nome do aluno: ")
nota1 = float(input("Insira a 1º nota do aluno: "))
nota2 = float(input("Insira a 2º nota do aluno: "))

media = (nota1 + nota2) /2
print("Nome: ", nome)
print("1º nota = ", nota1)
print("2º nota = ", nota2)

print(f"\nA media do(a) {nome} eh de {media:.1f}")