# Leia uma frase e diga se ela eh polindromo ou nao (retire espaço no programa)
# Polindromo sao frases que se lem igual de tras pra frente ou normal.
# Ex: Apos a Sopa
# A sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona


# Entrada de Dados
frases = str(input("Digite uma frase: ")).strip().upper()
split_frase = frases.split() #Divide a frase que voce digitar
frase_sem_espaco = "".join(split_frase) #Junta a frase mas sem espaços "". Como vc ve ai
inverso = ""

# Condiçao = Leitura inversa
for letra in frase_sem_espaco[::-1]: #le de tras para a frente a frase sem espaços
    inverso += letra

# Decisao
print("Original:", frase_sem_espaco)
print("Invertida:", inverso)

if frase_sem_espaco == inverso:
    print("A frase eh polindromo")
else:
    print("A frase nao eh polindromo")

