from modulos_moeda.formata_texto.funcao_format import formatado
from modulos_moeda.verificacao.valida_entrada import so_numeros, so_letra

# Programa Principal
entrada = so_numeros('Digite um valor: R$')
escolha = so_letra("Ver texto formatado? [S/N]: ")
formatado(entrada, escolha)


'''
passo a passo (call stack)

    1) main.py chama so_letra("...").
    2) Pausa o main e executa so_letra no arquivo valida_entrada.py.
    3) Dentro de so_letra:
        * roda o while True;
        * faz input;
        * se inválido → imprime erro e repete;
        * se válido → return "S" ou return "N".

    4) Volta para main.py e atribui: escolha recebe o valor retornado.
    
    por isso ela “garante” "S" ou "N"

Porque só existe return quando for "S"/"SIM" ou "N"/"NAO"/"NÃO".
Se digitar qualquer outra coisa, não retorna: continua no while perguntando de novo.
Logo, em main.py, após a chamada, escolha sempre será "S" ou "N" — você não precisa 
fazer .strip().upper() de novo.

'''