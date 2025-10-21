# Funçao chamada AREA ira receber largura e comprimento do terreno
# Mostre: A quantos m² tem o terreno
# Calcula os m² do terreno com os valores inseridos em comprimento e largura

def calcular_area(comprimento, largura):
    return comprimento * largura

# Funçao que impede valores negativos.
def pedir_valor(mensagem):
    while True:
        valor = float(input(mensagem))
        while valor <= 0:
            print("  --> ERRO: Digite numeros maiores que 0")
            print("-" * 35)
            valor = float(input(mensagem))
        break
    return valor

# Atribui a uma VAR o valor que sera inserido na funçao PEDIR VALOR.
comprimento_input = pedir_valor("Qual o comprimento do terreno?: ")
largura_input = pedir_valor("Qual a largura do terreno?: ")

area = calcular_area(comprimento_input, largura_input)

print("-" * 30)
print(f"{'Controle de Terrenos':^30}")
print("-" * 30)
print(f"Largura: {largura_input} m")
print(f"Comprimento: {comprimento_input} m")
print(f"O terreno tem {area:.2f} m².")






#     Resposta que antes de alterar isso para a funcao pedir_valor
'''    
Programa Principal
 while True:
     comprimento_input = float(input("Qual o comprimento do terreno?: "))
     while comprimento_input <= 0:
         print("  --> ERRO: Digite numeros maiores que 0")
         print("-"* 35)
         comprimento_input = float(input("Qual o comprimento do terreno?: "))

     largura_input = float(input("Qual a largura do terreno?: "))
     while largura_input <= 0:
         print("  --> ERRO: Digite numeros maiores que 0")
         print("-"* 35)
         largura_input = float(input("Qual o comprimento do terreno?: "))
     break

'''
#