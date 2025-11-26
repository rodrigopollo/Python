# So aceito numeros INT ou FLOAT, texto da ERRO
def so_numeros(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        if entrada.replace(".", "", 1).isdigit():
            return float(entrada)
        else:
            print("ERRO: Digite apenas numeros validos.")
            print('-' * 35)


# Nao aceita numeros, somente letras e palvras q estao na CONDIÇAO,  se nao da ERRO.
def so_letra(mensagem):
    while True:
        escolha = input(mensagem).strip().upper()

        if escolha in ("N", "NAO", "NÃO"):
            return "N"
        elif escolha in ("S", "SIM"):
            return "S"
        else:
            print("ERRO: Digite apenas S, SIM, N ou NÃO.")