# Contagem regresiva de 10 segundos.
# Pausa de 1 segundo entre cada numero.
from datetime import date
from time import sleep

# Saida de dados
print(f"{" Contagem Regresiva a Virada do Ano ":=^50}")
print(f"Faltando poucos segundos para começar a contagem regresiva para o final de", date.today().year)
sleep(3)

# Condiçao
for i in range(10, 0, -1):
    sleep(0.5)
    print(i)

# Decisao
print(f"FELIZ ANO NOVO!")
print(f"Feliz ", date.today().year + 1)