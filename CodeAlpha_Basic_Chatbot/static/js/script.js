const chatForm = document.querySelector("#chat-form");
const messageInput = document.querySelector("#message-input");
const chatMessages = document.querySelector("#chat-messages");

function addMessage(text, sender) {
    const row = document.createElement("div");
    const bubble = document.createElement("div");
    row.className = `message-row ${sender}-row`;
    bubble.className = `message ${sender}-message`;
    bubble.textContent = text;
    row.appendChild(bubble);
    chatMessages.appendChild(row);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const message = messageInput.value.trim();
    if (!message) return;
    addMessage(message, "user");
    messageInput.value = "";
    messageInput.focus();
    try {
        const response = await fetch("/chat", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({ message }) });
        const data = await response.json();
        addMessage(response.ok ? data.response : (data.error || "Something went wrong."), "bot");
    } catch (error) {
        addMessage("Unable to reach the chatbot right now.", "bot");
    }
});