print("Gerador de pa: ")
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao pa: "))
termo = primeiro
contador = 1

while contador <= 10:
    print(f"O termo eh {termo}")
    termo += razao
    contador += 1

print("FIM")
