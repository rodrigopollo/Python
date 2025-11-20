from ..calculos.calculos_preco import (
    preco_com_juros,
    preco_com_desconto,
    dobro_preco,
    metade_preco
)


# Opçao para exibir texto formatado em modo moeda e 2 casas decimais, ou nao.
def formatado(preco: float = 0, opcao: str = "") -> None:

    while True:
        if opcao in ('S', 'N', 'SIM', 'NAO'):
            print("-" * 33)
            print(f"{'TIPO':<25}{'PREÇO':<10}")
            print("-" * 33)

        if opcao in ('S', 'SIM'):
            print(f"{'Preço com juros:':<24} R${preco_com_juros(preco):.2f}")
            print(f"{'Preço com desconto:':<24} R${preco_com_desconto(preco):.2f}")
            print(f"{'Dobro do preco:':<24} R${dobro_preco(preco):.2f}")
            print(f"{'Metade do preço:':<24} R${metade_preco(preco):.2f}")
            print("-" * 33)
            break

        elif opcao in ('N', 'NAO'):
            print(f"{'Preço com juros:':<24} {preco_com_juros(preco)}")
            print(f"{'Preço com desconto:':<24} {preco_com_desconto(preco)}")
            print(f"{'Dobro do preco:':<24} {dobro_preco(preco)}")
            print(f"{'Metade do preço:':<24} {metade_preco(preco)}")
            print("-" * 33)
            break
        else:
            print("ERRO: Digite apenas S ou N.")
            print("-" * 33)
            opcao = input("Ver texto formatado [S/N]: ").strip().upper().replace("Ã", "A")
