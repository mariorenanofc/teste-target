from flask import Flask, jsonify, request, send_from_directory
import json

app = Flask(__name__)

#Coloque aqui o código das questões ja desenvolvidas.
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
soma_questao1 = SOMA

def fibonacci(numero):
    fib = [0, 1]
    while fib[-1] < numero:
        fib.append(fib[-1] + fib[-2])
    
    if numero in fib:
        return f"{numero} pertence à sequência de Fibonacci."
    else:
        return f"{numero} não pertence à sequência de Fibonacci."
    
with open('faturamento.json', 'r') as f:
    faturamento = json.load(f)

valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media = sum(valores) / len(valores)
dias_acima_media = len([valor for valor in valores if valor > media])

faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento_estados.values())
percentuais = {}

for estado, valor in faturamento_estados.items():
    percentual = (valor / total) * 100
    percentuais[estado] = round(percentual, 2)

def inverter_string(texto):
    texto_invertido = ''
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

@app.route('/questao1')
def questao1():
    return jsonify({'resultado': soma_questao1})

@app.route('/questao2')
def questao2():
    numero = int(request.args.get('numero'))
    resultado = fibonacci(numero)
    return jsonify({'resultado': resultado})

@app.route('/questao3')
def questao3():
    return jsonify({'menor': menor_valor, 'maior': maior_valor, 'acima_media': dias_acima_media})

@app.route('/questao4')
def questao4():
  return jsonify(percentuais)

@app.route('/questao5')
def questao5():
  texto = request.args.get('texto')
  resultado = inverter_string(texto)
  return jsonify({'resultado': resultado})

@app.route('/')
def index():
    return send_from_directory('web', 'index.html')

# Rota estática para servir arquivos da pasta 'web'
@app.route('/web/<path:filename>')
def serve_static(filename):
    return send_from_directory('web', filename)

if __name__ == '__main__':
    app.run(debug=True)