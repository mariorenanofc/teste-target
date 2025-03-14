def calcular_percentual_faturamento(faturamento_estados):
    """
    Calcula o percentual de faturamento por estado.

    Args:
        faturamento_estados: Um dicionário com o faturamento por estado.
    """
    # Calcula o total do faturamento
    total = sum(faturamento_estados.values())

    # Imprime o total do faturamento
    print(f"A soma total de todos os estados é de: {total:.2f}")

    # Loop para calcular e imprimir o percentual de cada estado
    for estado, valor in faturamento_estados.items():
        percentual = (valor / total) * 100
        print(f"Porcentagem {estado}: {percentual:.1f}%")

# Dados de faturamento por estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Chama a função para calcular os percentuais
calcular_percentual_faturamento(faturamento_estados)