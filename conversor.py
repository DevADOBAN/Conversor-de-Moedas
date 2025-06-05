def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    """
    Converte um valor entre duas moedas usando as taxas fornecidas
    
    Args:
        valor: Valor a ser convertido (float)
        moeda_origem: Moeda de origem (código de 3 letras)
        moeda_destino: Moeda de destino (código de 3 letras)
        taxas: Dicionário com as taxas de câmbio
        
    Returns:
        Valor convertido (float)
    """
    # Se as moedas forem iguais, retorna o mesmo valor
    if moeda_origem == moeda_destino:
        return valor
    
    try:
        # Converte para USD primeiro (moeda base da API)
        valor_em_usd = valor / taxas[moeda_origem]
        
        # Converte de USD para moeda de destino
        valor_convertido = valor_em_usd * taxas[moeda_destino]
        
        return valor_convertido
    
    except KeyError as e:
        raise ValueError(f"Moeda não suportada: {e}")

def formatar_valor(valor, moeda):
    """Formata o valor monetário para exibição"""
    simbolos = {
        'USD': '$',
        'BRL': 'R$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥'
    }
    
    simbolo = simbolos.get(moeda, moeda + " ")
    return f"{simbolo}{valor:,.2f}"