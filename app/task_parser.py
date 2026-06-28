"""
Task Parser

Converts natural language instructions into
structured task information.
"""

from pathlib import Path

from llm import ask_llm


PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "task_prompt.txt"


def load_task_prompt() -> str:
    """
    Load the task parsing prompt from the prompts folder.
    """

    return PROMPT_PATH.read_text(encoding="utf-8")


def parse_task(message: str) -> str:
    """
    Ask the LLM to convert a boss's instruction
    into structured task information.
    """

    prompt_template = load_task_prompt()
    prompt = prompt_template.replace("{message}", message)

    return ask_llm(prompt)
