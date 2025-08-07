# Pergunte a distancia total da viagem em KM
#  Calcule o preço da passagem, 0.50 ate 200km, 0,45 por mais de 200 km

distancia = float(input("Qual a distancia dessa viagem: "))

menor_200km = 0.50 * distancia
maior_200km = 0.45 * distancia

if distancia <= 200:
    print(f"A viagem de {distancia}KM fica R${menor_200km:.2f} reais")
else:
    print(f"A viagem de {distancia}KM fica R${maior_200km:.2f} reais")