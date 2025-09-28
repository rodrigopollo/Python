# Leia 5 numeros e coloque em uma lista.
# Cadastre os numeros inseridos ja na posiçao correta (sem usar sort())
# Mostre a lista em ordenada.

lista = []

for i in range(0, 5):
    while True:
        try:
            valor = int(input("Digite um numero: "))
            break
        except ValueError:
            print("ERRO: Digite apenas numeros inteiros.")

    index = 0

    # Encontra a posição correta que o numero digitado deve ser inserido.
    # Verifica se o NUM digitado eh maior que o valor do INDEX atual, se for ele continua.
    for numero in lista:
        if valor > numero:
            index += 1
        else:
            break
    # Insere o valor no INDEX que ele verificou ele parou.
    lista.insert(index, valor)

print(f"O resultado final foi: {lista}")

"""
Explicaçao do exercicio pq eu nao consegui fazer com oq o curso estava ensinando.

  Faz uma repetiçao 5x contando com index de 0, 5   
            -> for index in range(5): 
 
  Usa a VARIAVEL (POSICAO) pra verificar em qual posicao(index) da lista ele vai ter que inserir
  o novo numero, ou seja, voce vai colocar 5 numeros INT com index (0, 1, 2, 3)
  Ele vai usar a posicao para saber aonde o numero que voce digitou tem q entrar, mas pra isso
  vai ter que usar o IF que vem logo depois disso.
  
            -> valor = int(input("Digite um numero: "))
                posicao = 0 

    Aqui ele vai usar esse (2º FOR) para percorrer e CADA NUMERO DENTRO DA LISTA, e em cada verificação
    ele vai usar o IF que vem abaixo.
    Exemplo de lista......... lista [5, 3, 8]
    Na primeira vez vai verificar o numero 5, depis o 3 e por ultimo o 8
    
             -> for numero in lista:
    
    Lista eh percorrida do começo pro fim, se nao for especificado de uma maneira diferente.
    A cada vez q o FOR percorra os numeros da lista ele vai verificar IF o numero que voce digitou
    eh maior que o o numero do index que ele esta agora, ou seja, (NUMERO ATUAL DA LISTA) 
    Exemplo de lista......... lista [5, 3, 8]
    
    Exemplo numero digitado = 6
    Numero que voce digitou eh maior que 5? Ai ele faz a verificação do IF.
    Pos (0)  ==>  6 > 5? = SIM..... nao vai na posiçao 0, entao, posicao 0 + 1 = 1
    Pos (1)  ==>  6 > 3? = SIM..... nao vai na posiçao 1, entao, posicao 1 + 1 = 2
    Pos (2)  ==>  6 > 8? = NAO..... vai na posiçao 2 e empurra o 8 para posicao 3, entao, breack(pare)
    
            if valor > numero:
                posicao += 1
            else:
                break

    Como o 6 eh menor que o 8, adicione o 6 na posicao que esta agora, como vimos no exemplo acima
    a posiçao que ele achou foi a Pos(2), entao agora posicao 2 = 6 e o numero 8 para a ser posicao (3)
    
            -> lista.insert(posicao, valor)
                lista.sort()
                print(lista)
                Resultado = [5, 3, 6, 8]
                








"""
