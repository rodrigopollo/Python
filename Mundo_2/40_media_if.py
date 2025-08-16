# Insira 2 notas e faça a media
# Media < 5 = reprovado
# Media > 5 e < 6.9 = recuperaçao
# Medaia >= 7 = aprovado


print("   INSIRA AS NOTAS DO ALUNO")
print("=" * 35)

nota1 = float(input("1º nota do aluno: "))
nota2 = float(input("2º nota do aluno: "))

media_notas = (nota1 + nota2) / 2

if media_notas >= 7:
    print(f"A media foi de {media_notas:.1f}, voce foi aprovado, PARABENS!")
elif 5 < media_notas < 6.9:
    print(f"Com a media de {media_notas:.1f}, voce esta de recuperaçao")
elif nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("MEDIA INVALIDA, POR FAVOR VERIQUE NOVAMENTE AS NOTAS INSERIDAS")
else:
    print(f"A media foi de {media_notas:.1f}, reprovado")



# elif 5 < media_notas < 6.9:
# Isso eh o modo que se segue no python de forma abreviada o AND
# entao o melhor eh se acostumar.
# eh diferente, se le do meio pra frete e pra tras e nao como normalmente se faria.