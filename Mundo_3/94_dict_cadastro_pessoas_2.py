# Configurações (constantes no início do código)
LIMITE_MIN_IDADE = 0
LIMITE_MAX_IDADE = 150

# Lista para armazenar todas as pessoas
lista_pessoas = []

# Variáveis para estatísticas
total_pessoas = 0
soma_idades = 0
mulheres_cadastradas = []

print("\n=== CADASTRO DE PESSOAS ===")

while True:
    # Dicionário para armazenar os dados da pessoa atual
    pessoa = {}

    # 1. Cadastro do NOME (com validação básica)
    while True:
        nome = input("\nNome: ").strip().title()
        if nome.replace(" ", "").isalpha() and len(nome) > 0:  # Verifica se tem apenas letras e não está vazio
            pessoa["nome"] = nome
            break
        print("Erro: Use apenas letras e espaços no nome.")

    # 2. Cadastro da IDADE (com validação numérica e faixa etária)
    while True:
        idade_cadastrada = input("Idade: ").strip()
        if idade_cadastrada.isdigit():  # Verifica se é número
            idade = int(idade_cadastrada)
            if LIMITE_MIN_IDADE <= idade <= LIMITE_MAX_IDADE:
                pessoa["idade"] = idade
                break
            print(f"Erro: Idade deve ser entre {LIMITE_MIN_IDADE} e {LIMITE_MAX_IDADE}.")
        else:
            print("Erro: Digite um número válido para idade.")

    # 3. Cadastro do SEXO (padronizado para M/F)
    while True:
        sexo = input("Sexo [M/F]: ").strip().lower()
        if sexo in ("m", "masculino"):
            pessoa["sexo"] = "M"
            break
        elif sexo in ("f", "feminino"):
            pessoa["sexo"] = "F"
            mulheres_cadastradas.append(pessoa["nome"])  # Adiciona à lista de mulheres
            break
        else:
            print("Erro: Digite 'M' para masculino ou 'F' para feminino.")

    # Atualiza estatísticas
    lista_pessoas.append(pessoa)
    total_pessoas += 1
    soma_idades += pessoa["idade"]

    # 4. Pergunta se deseja continuar
    while True:
        continuar = input("\nCadastrar outra pessoa? [S/N]: ").strip().lower()
        if continuar in ("s", "sim", "n", "não"):
            break
        print("Erro: Digite 'S' para continuar ou 'N' para sair.")

    if continuar in ("n", "nao"):
        break

# Calcula média de idades
media_idades = soma_idades / total_pessoas if total_pessoas > 0 else 0

# Exibe resultados finais
print("\n=== RESULTADOS ===")
print(f"Total de pessoas cadastradas: {total_pessoas}")
print(f"Média de idades: {media_idades:.1f} anos")
print(f"Mulheres cadastradas: {', '.join(mulheres_cadastradas) if mulheres_cadastradas else 'Nenhuma'}")