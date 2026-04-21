import logging
from typing import Generator

from google import genai
from google.genai import types

from config import GOOGLE_API_KEY, GEMINI_MODEL
from tools import execute_tool

log = logging.getLogger("rag")

_client = None


def get_client():
    global _client
    if _client is None:
        _client = genai.Client(api_key=GOOGLE_API_KEY)
    return _client


SYSTEM_TEMPLATE = """You are a helpful assistant that answers questions based on the provided document context and available tools.

Use the context below to answer. If the user asks about specific configurations, VO steps, or VO actions for a client/module, use the get_configs tool to fetch the actual JSON config.

If the answer isn't in the context or configs, say you don't have enough information.

Context:
{context}"""


GET_CONFIGS_TOOL = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="get_configs",
            description="""Fetches the JSON configuration file for a specific client, module, and config type.

Use this tool when:
- User asks about VO steps or VO actions for a client journey
- User asks about configuration details for a specific client/module
- User asks how a specific onboarding journey or module is configured
- You need to reference actual JSON to give an accurate answer

Available clients: abcapital, global
Available modules per client: global, absli_bp7m6i-recruitment_leads_124r3a (under abcapital)
Available config types: vo_steps, vo_actions

If unsure about exact names, make your best guess — the tool will return what's available if not found.""",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "client": types.Schema(
                        type=types.Type.STRING,
                        description="Client folder name e.g. 'abcapital' or 'global'",
                    ),
                    "module": types.Schema(
                        type=types.Type.STRING,
                        description="Module folder name e.g. 'global' or 'absli_bp7m6i-recruitment_leads_124r3a'",
                    ),
                    "config_type": types.Schema(
                        type=types.Type.STRING,
                        description="Config file name without extension: 'vo_steps' or 'vo_actions'",
                    ),
                },
                required=["client", "module", "config_type"],
            ),
        )
    ]
)

MAX_TOOL_ROUNDS = 5


def stream_response(query: str, context: str, history: list[dict]) -> Generator[str, None, None]:
    client = get_client()
    system = SYSTEM_TEMPLATE.format(context=context)

    # Build contents from history + current query
    contents = []
    for msg in history:
        role = "model" if msg["role"] == "assistant" else "user"
        contents.append(types.Content(role=role, parts=[types.Part(text=msg["content"])]))
    contents.append(types.Content(role="user", parts=[types.Part(text=query)]))

    config = types.GenerateContentConfig(
        system_instruction=system,
        tools=[GET_CONFIGS_TOOL],
        max_output_tokens=4096,
    )

    # Multi-step tool call loop
    for round_num in range(1, MAX_TOOL_ROUNDS + 1):
        log.info(f"LLM | Round {round_num}")

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=contents,
            config=config,
        )

        candidate = response.candidates[0]

        # Separate tool calls from text parts
        tool_calls = []
        text_parts = []
        for part in candidate.content.parts:
            if hasattr(part, "function_call") and part.function_call:
                tool_calls.append(part.function_call)
            elif hasattr(part, "text") and part.text:
                text_parts.append(part.text)

        if not tool_calls:
            # No more tool calls — yield final answer
            log.info(f"LLM | Final answer after {round_num} round(s)")
            for text in text_parts:
                yield text
            return

        # Log and execute each tool call
        log.info(f"LLM | {len(tool_calls)} tool call(s) requested")
        contents.append(candidate.content)

        function_response_parts = []
        for fc in tool_calls:
            log.info(f"LLM | Calling tool: {fc.name}({dict(fc.args)})")
            result = execute_tool(fc.name, dict(fc.args))
            log.info(f"LLM | Tool result: {result[:150]}...")
            function_response_parts.append(
                types.Part(
                    function_response=types.FunctionResponse(
                        name=fc.name,
                        response={"result": result},
                    )
                )
            )

        contents.append(types.Content(role="user", parts=function_response_parts))

    yield "I reached the maximum reasoning steps. Please try rephrasing your question."
