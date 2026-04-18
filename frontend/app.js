const API_URL = "http://localhost:8000";

let chatHistory = [];

// ── DOM refs ──
const messagesEl = document.getElementById("messages");
const chatForm = document.getElementById("chat-form");
const queryInput = document.getElementById("query-input");
const sendBtn = document.getElementById("send-btn");
const docList = document.getElementById("doc-list");
const btnIngestDir = document.getElementById("btn-ingest-dir");
const btnClear = document.getElementById("btn-clear");
const btnNewChat = document.getElementById("btn-new-chat");
const fileUpload = document.getElementById("file-upload");
const toast = document.getElementById("toast");

// ── Marked setup ──
marked.setOptions({
  breaks: true,
  highlight: (code, lang) => {
    if (lang && hljs.getLanguage(lang)) {
      return hljs.highlight(code, { language: lang }).value;
    }
    return hljs.highlightAuto(code).value;
  },
});

// ── Toast ──
let toastTimer;
function showToast(message, type = "info") {
  clearTimeout(toastTimer);
  toast.textContent = message;
  toast.className = `toast ${type}`;
  toastTimer = setTimeout(() => { toast.className = "toast hidden"; }, 3500);
}

// ── Document list ──
async function loadDocuments() {
  try {
    const res = await fetch(`${API_URL}/documents`);
    const { sources } = await res.json();
    if (sources.length === 0) {
      docList.innerHTML = '<li class="empty-state">No documents ingested</li>';
    } else {
      docList.innerHTML = sources.map(s => `<li title="${s}">${s}</li>`).join("");
    }
  } catch {
    docList.innerHTML = '<li class="empty-state">Backend offline</li>';
  }
}

// ── Ingest directory ──
btnIngestDir.addEventListener("click", async () => {
  btnIngestDir.disabled = true;
  btnIngestDir.textContent = "Ingesting…";
  try {
    const res = await fetch(`${API_URL}/ingest/directory`, { method: "POST" });
    const data = await res.json();
    if (res.ok) {
      showToast(`${data.message} (${data.chunks} chunks)`, "success");
      await loadDocuments();
    } else {
      showToast(data.detail || "Ingestion failed", "error");
    }
  } catch {
    showToast("Could not reach backend", "error");
  } finally {
    btnIngestDir.disabled = false;
    btnIngestDir.textContent = "Ingest docs/";
  }
});

// ── Upload file ──
fileUpload.addEventListener("change", async () => {
  const file = fileUpload.files[0];
  if (!file) return;
  const formData = new FormData();
  formData.append("file", file);
  try {
    const res = await fetch(`${API_URL}/ingest/file`, { method: "POST", body: formData });
    const data = await res.json();
    if (res.ok) {
      showToast(`${data.message} (${data.chunks} chunks)`, "success");
      await loadDocuments();
    } else {
      showToast(data.detail || "Upload failed", "error");
    }
  } catch {
    showToast("Could not reach backend", "error");
  }
  fileUpload.value = "";
});

// ── Clear documents ──
btnClear.addEventListener("click", async () => {
  if (!confirm("Clear all ingested documents?")) return;
  try {
    await fetch(`${API_URL}/documents`, { method: "DELETE" });
    await loadDocuments();
    showToast("All documents cleared");
  } catch {
    showToast("Could not reach backend", "error");
  }
});

// ── New chat ──
btnNewChat.addEventListener("click", () => {
  chatHistory = [];
  messagesEl.innerHTML = `
    <div class="welcome">
      <h1>Ask your documents</h1>
      <p>Ingest markdown files from the sidebar, then start chatting.</p>
    </div>`;
});

// ── Add message bubble to DOM ──
function addMessage(role, content = "") {
  // Remove welcome screen on first message
  const welcome = messagesEl.querySelector(".welcome");
  if (welcome) welcome.remove();

  const msg = document.createElement("div");
  msg.className = `message ${role}`;

  const avatar = document.createElement("div");
  avatar.className = "avatar";
  avatar.textContent = role === "user" ? "You" : "AI";

  const bubble = document.createElement("div");
  bubble.className = "bubble";

  if (role === "assistant" && !content) {
    bubble.classList.add("cursor");
  }

  if (content) {
    bubble.innerHTML = role === "assistant" ? marked.parse(content) : escapeHtml(content);
  }

  msg.appendChild(avatar);
  msg.appendChild(bubble);
  messagesEl.appendChild(msg);
  messagesEl.scrollTop = messagesEl.scrollHeight;

  return bubble;
}

function escapeHtml(text) {
  return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// ── Auto-resize textarea ──
queryInput.addEventListener("input", () => {
  queryInput.style.height = "auto";
  queryInput.style.height = Math.min(queryInput.scrollHeight, 160) + "px";
});

// ── Submit on Enter (Shift+Enter for newline) ──
queryInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    chatForm.requestSubmit();
  }
});

// ── Chat submit ──
chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const query = queryInput.value.trim();
  if (!query) return;

  queryInput.value = "";
  queryInput.style.height = "auto";
  sendBtn.disabled = true;

  addMessage("user", query);

  const assistantBubble = addMessage("assistant", "");

  let fullResponse = "";

  try {
    const res = await fetch(`${API_URL}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query, history: chatHistory }),
    });

    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || "Request failed");
    }

    const reader = res.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      fullResponse += decoder.decode(value, { stream: true });
      assistantBubble.innerHTML = marked.parse(fullResponse);
      assistantBubble.classList.add("cursor");
      messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    assistantBubble.classList.remove("cursor");

    // Update history
    chatHistory.push({ role: "user", content: query });
    chatHistory.push({ role: "assistant", content: fullResponse });

    // Re-highlight code blocks
    assistantBubble.querySelectorAll("pre code").forEach(hljs.highlightElement);

  } catch (err) {
    assistantBubble.classList.remove("cursor");
    assistantBubble.textContent = `Error: ${err.message}`;
    showToast(err.message, "error");
  } finally {
    sendBtn.disabled = false;
    queryInput.focus();
  }
});

// ── Init ──
loadDocuments();
