import requests
import json
import os

def obter_taxas_cambio():
    """Obtém as taxas de câmbio atuais de uma API pública"""
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        dados = response.json()
        if 'rates' in dados:
            # Salva os dados para uso offline
            with open('moedas.json', 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2)
            return dados['rates']
        else:
            print("Erro na API. Usando dados locais...")
            return carregar_dados_locais()
    except (requests.RequestException, json.JSONDecodeError) as e:
        print(f"Erro na API: {e}. Usando dados locais...")
        return carregar_dados_locais()

def carregar_dados_locais():
    """Carrega dados de câmbio de um arquivo local"""
    try:
        if os.path.exists('moedas.json'):
            with open('moedas.json', 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return dados.get('rates', dados_fallback())
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        pass
    return dados_fallback()

def dados_fallback():
    """Dados de fallback caso tudo falhe"""
    return {
        'BRL': 5.0,    # Real Brasileiro
        'EUR': 0.93,   # Euro
        'GBP': 0.80,   # Libra Esterlina
        'JPY': 147.0,  # Iene Japonês
        'USD': 1.0     # Dólar Americano
    }

def listar_moedas_disponiveis():
    """Lista os códigos das moedas disponíveis"""
    taxas = carregar_dados_locais()
    return list(taxas.keys())

if __name__ == "__main__":
    moedas = listar_moedas_disponiveis()
    print(moedas)