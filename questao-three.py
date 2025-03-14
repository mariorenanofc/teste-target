import json

def analisar_faturamento(nome_arquivo):
    """
    Analisa o faturamento diário de um arquivo JSON.

    Args:
        nome_arquivo: O nome do arquivo JSON com os dados de faturamento.
    """
    # Abre o arquivo JSON para leitura
    with open(nome_arquivo, 'r') as arquivo:
        dados_faturamento = json.load(arquivo) #Carrega os dados em uma nova variável

    # Cria uma lista com os valores de faturamento maiores que 0
    valores = [dia['valor'] for dia in dados_faturamento if dia['valor'] > 0]

    # Calcula o menor valor de faturamento
    min_valor = min(valores)

    # Calcula o maior valor de faturamento
    max_valor = max(valores)

    # Calcula a média de faturamento
    media = sum(valores) / len(valores)
    
    # Conta os dias com faturamento acima da média
    dias_acima_media = len([valor for valor in valores if valor > media])

    # Imprime os resultados
    print(f"Menor faturamento: {min_valor}")
    print(f"Maior faturamento: {max_valor}")
    print(f"Dias acima da média: {dias_acima_media}")

# Chama a função com o nome do arquivo JSON
analisar_faturamento('faturamento.json')