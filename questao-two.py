def fibonacci(numero):
    """
    Verifica se um número pertence à sequência de Fibonacci.

    Args:
        numero: O número a ser verificado.

    Returns:
        Uma string informando se o número pertence ou não à sequência.
    """
    fib = [0, 1]  # Inicializa a sequência com os primeiros dois números
    
    # Loop para gerar a sequência até que o último número seja >= ao número dado
    while fib[-1] < numero:  
        proximo_numero = fib[-1] + fib[-2]  # Calcula o próximo número
        fib.append(proximo_numero)  # Adiciona à sequência
    
    # Verifica se o número dado está na sequência gerada
    if numero in fib:
        return f"{numero} pertence à sequência de Fibonacci."
    else:
        return f"{numero} não pertence à sequência de Fibonacci."

# Testa a função com um exemplo
numero_teste = 21
resultado = fibonacci(numero_teste)
print(resultado)