(function () {
    const toggle = document.getElementById('chatbot-toggle');
    const panel = document.getElementById('chatbot-panel');
    const closeBtn = document.getElementById('chatbot-close');
    const form = document.getElementById('chatbot-form');
    const input = document.getElementById('chatbot-input');
    const messages = document.getElementById('chatbot-messages');

    if (!toggle || !panel || !form) return;

    const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
    const botAvatarUrl = document.querySelector('.chatbot-toggle-icon').src;
    const history = [];

    function addMessage(text, sender) {
        const row = document.createElement('div');
        row.className = 'chatbot-message-row chatbot-message-row-' + sender;

        if (sender === 'bot') {
            const avatar = document.createElement('img');
            avatar.src = botAvatarUrl;
            avatar.alt = '';
            avatar.className = 'chatbot-avatar';
            row.appendChild(avatar);
        }

        const bubble = document.createElement('div');
        bubble.className = 'chatbot-message chatbot-message-' + sender;
        bubble.textContent = text;
        row.appendChild(bubble);

        messages.appendChild(row);
        messages.scrollTop = messages.scrollHeight;
        return bubble;
    }

    function setOpen(open) {
        panel.hidden = !open;
        toggle.setAttribute('aria-expanded', String(open));
        if (open) input.focus();
    }

    toggle.addEventListener('click', () => setOpen(panel.hidden));
    closeBtn.addEventListener('click', () => setOpen(false));

    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        const message = input.value.trim();
        if (!message) return;

        addMessage(message, 'user');
        history.push({ role: 'user', content: message });
        input.value = '';
        input.disabled = true;

        const pending = addMessage('Digitando...', 'bot');

        try {
            const response = await fetch('/api/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ message, history: history.slice(0, -1) }),
            });
            const data = await response.json();

            if (!response.ok) {
                pending.textContent = data.error || 'Não foi possível responder agora. Tente novamente mais tarde.';
            } else {
                pending.textContent = data.reply;
                history.push({ role: 'assistant', content: data.reply });
            }
        } catch (err) {
            pending.textContent = 'Erro de conexão. Verifique sua internet e tente novamente.';
        } finally {
            input.disabled = false;
            input.focus();
        }
    });
})();
