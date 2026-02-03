document.addEventListener('DOMContentLoaded', () => {
    const chatHistory = document.getElementById('chat-history');
    const messageInput = document.getElementById('message-input');
    const sendBtn = document.getElementById('send-btn');

    function appendMessage(text, isUser) {
        const div = document.createElement('div');
        div.classList.add('message', isUser ? 'user-message' : 'claude-message');
        div.textContent = text;
        chatHistory.appendChild(div);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    async function sendMessage() {
        const text = messageInput.value.trim();
        if (!text) return;

        appendMessage(text, true);
        messageInput.value = '';
        messageInput.disabled = true;
        sendBtn.disabled = true;

        try {
            const response = await fetch('http://localhost:8000/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: text })
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const data = await response.json();
            appendMessage(data.reply, false);
        } catch (error) {
            appendMessage(`Error: ${error.message}`, false);
        } finally {
            messageInput.disabled = false;
            sendBtn.disabled = false;
            messageInput.focus();
        }
    }

    sendBtn.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
});
