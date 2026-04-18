from typing import Generator
import google.generativeai as genai
from config import GOOGLE_API_KEY, GEMINI_MODEL

genai.configure(api_key=GOOGLE_API_KEY)

SYSTEM_TEMPLATE = """You are a helpful assistant that answers questions based on the provided document context.
Use only the context below to answer. If the answer isn't in the context, say you don't have enough information.

Context:
{context}"""


def stream_response(query: str, context: str, history: list[dict]) -> Generator[str, None, None]:
    system = SYSTEM_TEMPLATE.format(context=context)

    model = genai.GenerativeModel(
        model_name=GEMINI_MODEL,
        system_instruction=system,
    )

    # Convert {role, content} history to Gemini {role, parts} format
    gemini_history = []
    for msg in history:
        role = "model" if msg["role"] == "assistant" else "user"
        gemini_history.append({"role": role, "parts": [msg["content"]]})

    chat = model.start_chat(history=gemini_history)
    response = chat.send_message(query, stream=True)

    for chunk in response:
        if chunk.text:
            yield chunk.text
