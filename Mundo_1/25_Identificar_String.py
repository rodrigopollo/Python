# Leia um nome
# O programa ira dizer si esse Nome tem SILVIA ou nao com TRUE or FALSE

nome = input("Digite um nome: ").strip()

temSilvia = "silvia" in nome.lower()
print(f"O nome digitado tem Silvia nele: {temSilvia}")

#///////////////////////////////////////////////////////
#///////////////////////////////////////////////////////

print("=" * 40)
print("ALTERNATIVA")

# nome = input("Digite um nome: ").strip()
print(f"O nome digitado tem Silvia nele: {nome[:5] == "Silvia".lower()}")



# A alternativa 1 diz, que como SILVIA tem 5 letras e 6 posiçoes (zero conta), se a primeira
# palavra da string tiver 5 letras e for == a "Silvia", eh verdadeiro, si nao eh falso.
# Isso usamos no exercicio 24, aqui so serve de exemplo pq nao resolve o problema
# do exercicio. Se Silvia por o segundo nome vai dar errado.