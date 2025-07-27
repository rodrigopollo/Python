import math

angulo = float(input("Digite o angulo que voce deseja: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O angulo {angulo} tem o seno de {seno:.2f}")
print(f"O angulo {angulo} tem o coseno de {cosseno:.2f}")
print(f"O angulo {angulo} tem o tangente de {tangente:.2f}")