# Funçao ira recerber um texto como parameter
# Mostre: Uma mensagem com uma linha separadora que se adapte ao tamanho da mensagem escrita.

def escreva(mensagem):
    tamanho_mensagem = len(mensagem) + 4
    print('-' * tamanho_mensagem)
    print(f"  {mensagem}")
    print('-' * tamanho_mensagem)


escreva("rodrigo pollo cardoso.".title())
escreva("Estudando Python com Guanabara.")
escreva("Objeto: Ser um Engenheiro de Dados")







