def inverter_string(texto):
    """
    Inverte os caracteres de uma string.

    Args:
        texto: A string a ser invertida.

    Returns:
        A string com os caracteres invertidos.
    """
    texto_invertido = ''  # Inicializa a string invertida vazia

    # Loop para percorrer a string de trás para frente
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]  # Adiciona cada caractere à string invertida

    return texto_invertido

# String de teste
texto_teste = "exiep remoc somaV"

# Chama a função para inverter a string
resultado = inverter_string(texto_teste)

# Imprime o resultado
print(resultado)