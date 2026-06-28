"""
LLM Interface

Handles communication with the local Ollama server.
"""

import ollama

from config import (
    OLLAMA_HOST,
    OLLAMA_MODEL
)

client = ollama.Client(host=OLLAMA_HOST)


def ask_llm(prompt: str) -> str:
    """
    Send a prompt to the local LLM.
    """

    response = client.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
