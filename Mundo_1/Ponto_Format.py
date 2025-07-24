a = input("Digite algo: ")

print("A informaçao inserida eh do tipo", type(a))

print("So tem espaços? ", a.isspace())
print("Eh numerico? ", a.isnumeric())
print("Eh alfabetico? ", a.isalpha())
print("Eh alfanumerico? ", a.isalnum())
print("Esta tudo em maiuscula? ", a.isupper())
print("Esta tudo em minuscula? ", a.islower())
print("Esta capitalizada? ", a.istitle()) #Capitalizada = Primeira letra maiscula. Como um titulo mesmo.


# O (a) aqui eh o OBJETO, e como estamos trabalhando sempre abrindo e fechando ()
# isso eh um METODO, estamos chamando um METODO de verificaçao neste exercicio.
# Como voce pode ver estamos verificando se esta td em Letra maiusculas, minusculas etc.

# Todo objete tem caracteristicas e realizam uma funçao ou seja, eles tem atributos e metodos.

