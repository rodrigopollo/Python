JUROS = 0.15            # 15% de juros padrao do modulo
DESCONTO = 0.10         # 10% de desconto padrao do modulo

def preco_com_juros(preco: float = 0) -> float:
    """
    Aplica a taxa de juros(usa a constante de JUROS) no preço base.

    Parameters
    ----------
    preco : float, optional
        Preço base. Padrao e 0.


    Returns
    --------
    float
        Valor final com juros aplicado
    """
    valor_com_juros = preco * (1 + JUROS)
    return valor_com_juros


def preco_com_desconto(preco: float = 0) -> float:
    """
    Aplica desconto (usa a constante de modulo DESCONTO) no preço base.

    Parameters
    ----------
    preco : float, optional
        Preço base. O padrao eh 0

    Returns
    -------
    float
        Valor final com desconto aplicado

    Notes
    -----
    - Desconto aplicado: DESCONTO (0.15 = 15%)
    - Como 'preco = 0' eh o padrao, função roda sem erro mesmo que o usuario esqueça de passar
     o argumento ou digite 0.
    """
    valor_com_desconto = preco * (1 - DESCONTO)
    return valor_com_desconto


def dobro_preco(preco: float = 0) -> float:
    """
    Retorn o dobro do preço base.

    Parameters
    ----------
    preco : float, optional
        Preço base. Padrao e 0.

    Returns
    -------
    float
        Valor dobrado
    """
    return preco * 2


def metade_preco(preco: float = 0) -> float:
    """
    Retorna a metade do preço base.

    Parameters
    ----------
    preco : float, optional

    Returns
    -------
    float
        Metade do preço base.
    """
    return  preco / 2
