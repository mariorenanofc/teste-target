async function calcularSoma() {
  const response = await fetch('/questao1');
  const data = await response.json();
  document.getElementById('resultado1').textContent = data.resultado; 
}

async function verificarFibonacci() {
  const numero = document.getElementById('numeroFibonacci').value;
  const response = await fetch(`/questao2?numero=${numero}`);
  const data = await response.json();
  document.getElementById('resultado2').textContent = data.resultado;
}

async function analisarFaturamento() {
  const response = await fetch('/questao3');
  const data = await response.json();
  document.getElementById('resultado3').textContent = `Menor: ${data.menor}, Maior: ${data.maior}, Acima da média: ${data.acima_media}`;
}

async function calcularPercentual() {
  const response = await fetch('/questao4');
  const data = await response.json();
  let resultado = "";
  for (const estado in data) {
      resultado += `${estado}: ${data[estado]}%, `;
  }
  document.getElementById('resultado4').textContent = resultado;
}

async function inverterString() {
  const texto = document.getElementById('stringInverter').value;
  const response = await fetch(`/questao5?texto=${texto}`);
  const data = await response.json();
  document.getElementById('resultado5').textContent = data.resultado; 
}

function showChallenges() {
  document.getElementById('challenges').style.display = 'flex'; 
  document.getElementById('challenges').scrollIntoView({ behavior: 'smooth' }); 
  document.getElementById('challenges').classList.add('show');
}