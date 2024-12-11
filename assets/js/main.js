async function loadCard() {
  try {
    const response = await fetch('components/html/card.html');

    if (!response.ok) throw new Error('Failed to load card');

    const cardHtml = await response.text();
    
    document.querySelector('.card').innerHTML = cardHtml;
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