from api_handler import obter_taxas_cambio
from conversor import converter_moeda, formatar_valor
import json

def main():
    taxas = obter_taxas_cambio()
    
    print("\n" + "="*50)
    print("        CONVERSOR DE MOEDAS INTERNACIONAL")
    print("="*50)
    
    # Mostra data de atualização
    try:
        with open('moedas.json', 'r') as f:
            dados = json.load(f)
            if 'date' in dados:
                print(f"  Taxas atualizadas em: {dados['date']}")
    except:
        print("  Usando taxas locais/fallback")
    
    print("="*50)
    
    while True:
        try:
            # Exibe moedas populares
            print("\nMoedas populares:")
            print("USD | EUR | GBP | JPY | BRL | CAD | AUD | CHF | CNY")
            
            # Obtém entrada do usuário
            valor = float(input("\nDigite o valor a ser convertido: "))
            moeda_origem = input("Moeda de origem (código 3 letras): ").upper()
            moeda_destino = input("Moeda de destino (código 3 letras): ").upper()
            
            # Verifica se moedas são válidas
            if moeda_origem not in taxas:
                print(f"\nErro: Moeda de origem '{moeda_origem}' inválida!")
                print("Use códigos de 3 letras (ex: USD, BRL, EUR)")
                continue
                
            if moeda_destino not in taxas:
                print(f"\nErro: Moeda de destino '{moeda_destino}' inválida!")
                print("Use códigos de 3 letras (ex: USD, BRL, EUR)")
                continue
            
            # Realiza a conversão
            resultado = converter_moeda(valor, moeda_origem, moeda_destino, taxas)
            
            # Exibe resultado formatado
            print("\n" + "-"*50)
            print(f"RESULTADO: {formatar_valor(valor, moeda_origem)} = {formatar_valor(resultado, moeda_destino)}")
            print("-"*50)
            
            # Pergunta se deseja continuar
            continuar = input("\nDeseja fazer outra conversão? (s/n): ").lower()
            if continuar != 's':
                print("\nObrigado por usar o Conversor de Moedas!")
                break
                
        except ValueError as e:
            print(f"\nErro: {e}")
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário.")
            break

def carregar_dados_locais():
    """Carrega os dados de moedas do arquivo local moedas.json"""
    with open('moedas.json', 'r') as f:
        return json.load(f).get('rates', {})

def listar_moedas_disponiveis():
    """Lista os códigos das moedas disponíveis"""
    taxas = carregar_dados_locais()
    return list(taxas.keys())

if __name__ == "__main__":
    main()