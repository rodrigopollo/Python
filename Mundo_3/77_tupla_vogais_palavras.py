# Trupla com varias palvras (sem acento)
# Mostras as vogais de cada palavra.

# Variaveis
palavras = ()
sair_programa = ""

# Loop infinito de verificaçao de vogais com condiçao de saida.
while True:
    print("-=" * 15)
    palavras = str(input("Digitue uma palavra (ou Sair para finalizar): ")).strip().title()

    # Verifica se o usuario quer continuar ou nao usando o programa. E agradece caso finalize.
    if palavras.upper()[0] == "S":
        print("-=" * 15)
        print("Obrigado por usar nosso programa!")
        break
    # Mostra as vogais de todas as palavras digitadas.
    else:
        print(f"As vogais de {palavras} sao:")
        for vogais in palavras:
            if vogais.lower() in "aeiou":
                print(vogais, end=" ")
        print("\n")



