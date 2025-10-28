def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} ate {fim} de {passo} em {passo}")

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont} ", end='')
            cont += passo
        print("FIM")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end='')
            cont -= passo
        print("FIM")


contador(1, 10, 1)
contador(10, 0, 2)

print("Agora eh sua vez de personalizar a contagem!")
inicio_input = int(input("Inicio: "))
fim_input = int(input("Fim: "))
passo_input = int(input("Passo: "))
contador(inicio_input, fim_input, passo_input)