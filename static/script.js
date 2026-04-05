/**
 * GroceryBot Chat Frontend
 * TODO: Implement the chat logic
 */

async function sendMessage() {
    const input = document.getElementById('userInput');
    const message = input.value.trim();
    if (!message) return;

    // Add user message to chat
    addMessage(message, 'user');
    input.value = '';

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        addMessage(data.response, 'bot');
    } catch (error) {
        addMessage('Sorry, something went wrong. Please try again.', 'bot');
    }
}

function addMessage(text, sender) {
    const messages = document.getElementById('messages');
    const div = document.createElement('div');
    div.className = `message ${sender}`;
    div.innerHTML = `<div class="message-content">${text}</div>`;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
}
