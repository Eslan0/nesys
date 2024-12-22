async function loadCard() {
  try {
    const response = await fetch('components/html/card.html');

    if (!response.ok) throw new Error('Failed to load card');

    const cardHtml = await response.text();
    
    document.querySelector('.cardNormal').innerHTML = cardHtml;
  } catch (error) {
    console.error('Error loading the card:', error);
  }
}
loadCard();

async function loadCardEmphas() {
  try {
    const response = await fetch('components/html/card_emphas.html');

    if (!response.ok) throw new Error('Failed to load card');

    const cardHtml = await response.text();
    
    document.querySelector('.cardEmphas').innerHTML = cardHtml;
  } catch (error) {
    console.error('Error loading the card:', error);
  }
}
loadCardEmphas();

/* Função para gerar Seções dinamicamete */
function addSection(containerId, id, className, content) {
  const container = document.getElementById(containerId);

  if (!container) {
    console.error('Contêiner não encotrado!');
    return;
  }

  const section = document.createElement('section');
  if (id) section.id = id;
  if (className) section.className = className;
  if (content) section.innerHTML = content;

  container.appendChild(section);
}

document.getElementById('add-section-btn').addEventListener('click', () => { addSection('container', `section-${Date.now()}`, 'dynamic-section',`<div class = "card"><h2>Seção adicionada</h2> <p>Tempo ${new Date().toLocaleTimeString()}.</p></div>`);
});