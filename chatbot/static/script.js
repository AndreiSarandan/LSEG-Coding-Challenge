async function sendMessage(text, showUser = true) {
    if (text == null)
        return;

    // Append message send by user
    if (showUser) appendMessage("You", text);

    // Wait for server response
    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    });

    const data = await res.json();

    // Parse server response
    const message = data.message || "No response from server.";
    var options = [];
    if (Array.isArray(data.options))
        options = data.options;

    appendMessage("LSEG Chat Bot", message, options);
}


// Append message to HTML page
function appendMessage(sender, text, options = []) {
    const chat = document.getElementById("chat");
    const message = document.createElement("div");

    // Check if messasge was send by user
    const isUser = sender.toLowerCase() === "you";

    //Set message HTML class
    if (isUser)
        message.className = "message user_message"
    else
        message.className = "message chat_message";

    let content = `<div class="bubble"><strong>${sender}:</strong> ${text}`;

    //insert options if message comes from chat
    if (options.length && !isUser) {
        content += "<ul>";
        options.forEach(opt => {
            content += `<li>${opt}</li>`;
        });
        content += "</ul>";
    }

    // Append message to HTML page
    message.innerHTML = content;

    chat.appendChild(message);
    chat.scrollTop = chat.scrollHeight;
}


// Reterieve user inpt from HTML page and send it to the server
function sendMessageToServer() {
    const input = document.getElementById("textInput");
    const message = input.value.trim();
    input.value = "";
    sendMessage(message);
}

window.onload = () => {
    // Initiate conversation
    sendMessage("Hello!");
    appendMessage("LSEG Chat Bot", "Hello! Welcome to LSEG. I'm here to help you.");
};
