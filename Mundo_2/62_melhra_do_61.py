print("Gerador de pa: ")
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao pa: "))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    while contador <= 10:
        print(f"O termo eh {termo}")
        termo += razao
        contador += 1
    print("Pausa")
    mais = int(input("Quantos termos voce quer mostrar a mais: "))

print(f"{total} termos mostrados")
