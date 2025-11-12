def ajuda(comando):
    help(comando)


def titulo(mensagem):
    tamanho = len(mensagem)
    print('-' * tamanho)
    print(mensagem)
    print('-' * tamanho)


while True:
    titulo('SISMTEMA DE AJUDA PyHELP')
    comando = input("Função ou Biblioteca: ")
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)



