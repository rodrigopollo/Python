# Leia o sexo de uma pessoa
# So pode aceitar "m" e "f"
# Caso esteja errado, continue, ate ter a resposta correta.

sexo = ""
while sexo != "F" and sexo != "M":
    sexo = str(input("Qual o seu sexo [M/F]: ")).strip().upper()
    if "M" != sexo != "F":
        print("ERROR: Por favor resposta com (M) de masculino ou (F) de feminino.")
        print("=" * 80)

# Quando voce digita uma letra exemplo "A" ele verifica o while assim:
# sexo eh diferente de "F"? -→ True, voce digiteou "A"
# sexo eh diferente de "M"? -→ True, voce digiteou "A"

# Ou seja enquanto "F" e "M" forem = True, o programa continua.
# No momento que um deles se torna = False o programa para.