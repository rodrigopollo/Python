# Detecta a velocidade do carro
# Se > 80km/h = voce foi multado
# A multa custara 7 reais para cada KM acima do limite.


velocidade_Carro = float(input("Qual velocidade atual do carro: "))

multa = (velocidade_Carro - 80) * 7

if velocidade_Carro > 80:
    print(f"Escesso de velocidade detectado, multa de R${multa:.2f} reais")
elif velocidade_Carro >= 77 and velocidade_Carro <= 80:
    print(f"Fique atento para nao receber multa!!!")
else:
    print("Parabens, continue dirigindo assim!")
