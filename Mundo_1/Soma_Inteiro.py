
# Cria um programa que leia 2 numeros e mostre a soma entre eles.

numero1 = int(input('Insira um numero'))
numero2 = int(input('Insira um numero'))

resutlado = numero1 + numero2
print(f"{numero1} + {numero2} = {resutlado}")


# Explicando o INT
# Caso voce nao coloco o INT antes do INPUT o programa entende que voce esta inserindo texto e vai
# concatenar os valores inseridos (EX: n1 = 2, n2 = 3) o resultado seria 23 pq ele junta os
# numeros em vez de somar, pq voce nao especificou que os valores inseridos sao numeros.

# Para isso aqui usamos o TIPO PRIMITIVO INT (inteiro). Assim voce esta dizendo para o programa:
# - Oh programa, os valores que eu colocar aqui (numeros) vao ser numericos do TIPO INTEIRO e nao texto.
# ai ele entende que tem que somar em vez de concatenar.

# Entao, tudo que estiver dentro de INT(....) sera considerado um numero inteiro.


# NOTE.: Contatenar --> Eh juntar 2 strings.