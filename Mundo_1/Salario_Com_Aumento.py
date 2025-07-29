# Leia o salario atual do funcionario.
# Mostre o novo salario apos ele ter ganho um 15% de aumento.

salario = float(input("O salario atual do funcionario = "))

aumento = salario * 0.15
salarioFinal = salario + aumento

print(f"\nO salario do funcionario aumentou de R${salario:.2f} reais para R${salarioFinal:.2f} reais "
      f"apos o aumento de 15%")


#       ---------  ALTERNATIVA ---------

aumento = salario + (salario * 0.15)

print(f"\nO salario do funcionario aumentou de R${salario:.2f} reais para R${aumento:.2f} reais "
      f"apos o aumento de 15%")
