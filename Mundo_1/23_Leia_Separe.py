# Leia um numero de 0 a 9999
# Mostre os digitos todos separados em linhas diferentes.


numero = int(input("Digite um numero: "))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"1º numero: {unidade}")
print(f"2º numero: {dezena}")
print(f"2º numero: {centena}")
print(f"2º numero: {milhar}")



