var islogedIN = localStorage.getItem("isSignedIn")
if (islogedIN != "true"){
  window.location.href = "/"
}
const input = document.getElementById("userMessage");
const chatContainer = document.getElementById("chatContainer");
// Store chat messages as plain text
const chatHistory = [];

// Append a message to the chat container
function appendMessage(text, sender) {
  const msgDiv = document.createElement("div");
  msgDiv.textContent = text;

  msgDiv.className = sender === "user" 
    ? "message user-message" 
    : "message ai-message";

  chatContainer.appendChild(msgDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight; // auto-scroll
  return msgDiv;
}

// Handle Enter key press
input.addEventListener("keydown", async (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    const message = input.value.trim();
    if (!message) return;

    // Show user message in chat
    appendMessage(message, "user");
    chatHistory.push({ role: "user", content: message });  // store user message
    input.value = "";

    // Show temporary AI "thinking" message
    const aiMsgDiv = appendMessage("Thinking...", "ai");

    try {
      // Send the full chat history to the backend
      const response = await fetch("http://127.0.0.1:5000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ history: chatHistory })
      });

      const data = await response.json();

      // Display AI response if available
      if (data.candidates?.[0]?.content?.parts?.[0]?.text) {
        const aiText = data.candidates[0].content.parts[0].text;
        aiMsgDiv.textContent = aiText;
        chatHistory.push({ role: "model", content: aiText });
      } else if (data.error) {
          aiMsgDiv.textContent = "Error from API: " + data.error.message;
      } else {
          aiMsgDiv.textContent = "Unexpected response: " + JSON.stringify(data);
      }


    } catch (err) {
      aiMsgDiv.textContent = "Error: " + err.message;
    }
  }
});
