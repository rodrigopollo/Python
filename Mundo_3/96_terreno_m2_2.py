# Funçao chamada AREA ira receber largura e comprimento do terreno
# Mostre: A quantos m² tem o terreno
# Calcula os m² do terreno com os valores inseridos em comprimento e largura

def calculo_area_quadrada(largura, comprimento):
    area_quadrada = largura * comprimento
    print(f"O terreno tem {area_quadrada}m².")


# Programa Principal
print(f"{'Controle de terreno':^30}")
print("-" * 30)

largura_input = float(input("Largura: "))
comprimento_input = float(input("Comprimento: "))

calculo_area_quadrada(largura_input, comprimento_input)