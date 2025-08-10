# Pergunte o salario do funcionario
# Se > 1250 = 10% de aumento
# Se < 1250 = 15% aumento

salario_Funcionario = float(input("Qual o salario do funcionario: "))

maior_1250 = salario_Funcionario + (salario_Funcionario * 0.10)
menor_1250 = salario_Funcionario + (salario_Funcionario * 0.15)

if salario_Funcionario >= 1250:
    print(f"Salario: R${salario_Funcionario:.2f}, apos aumento de 10% o salario foi para R${maior_1250:.2f}")
else:
    print(f"Salario: R${salario_Funcionario:.2f}, apos aumento de 15% o salario foi para R${menor_1250:.2f}")


