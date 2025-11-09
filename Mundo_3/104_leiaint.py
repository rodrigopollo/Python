# Uma funçao que aceita somente numeros INT
# Mostre: erro enquanto nao for digitado um numero INT

def numero_inteiro(mensagem):
    while True:
        # Se o valor inserido nao for 0 ou numero positivos, sempre dara mensagem de erro.
        numero_input = input(mensagem).strip()
        if numero_input.isnumeric():
            return int(numero_input)
        else:
            print("ERRO: Digite um numero inteito valido.")
            print("-=" * 20)

# Atribui o argumento da funçao. Variavel numero que recebe o retun da Funçao
numero = numero_inteiro("Digite um numero: ")
print(f"Voce acabou de digitar o numero {numero}")