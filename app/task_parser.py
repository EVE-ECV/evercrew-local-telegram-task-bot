"""
Task Parser

Converts natural language instructions into
structured task information.
"""

from llm import ask_llm


def parse_task(message: str) -> str:
    """
    Ask the LLM to convert a boss's instruction
    into structured task information.
    """

    prompt = f"""
You are an AI assistant helping a business owner.

Extract the following information.

Employee:
Task:
Deadline:
Priority:
Summary:

Instruction:

{message}
"""

    return ask_llm(prompt)
