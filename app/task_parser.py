"""
Task Parser

Converts natural language instructions into
structured task information.
"""

import json
from pathlib import Path

from llm import ask_llm
from models import Task


PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "task_prompt.txt"


def load_task_prompt() -> str:
    """
    Load the task parsing prompt from the prompts folder.
    """

    return PROMPT_PATH.read_text(encoding="utf-8")


def parse_task(message: str) -> Task:
    """
    Ask the LLM to convert a boss's instruction
    into a structured Task object.
    """

    prompt_template = load_task_prompt()
    prompt = prompt_template.replace("{message}", message)

    llm_response = ask_llm(prompt)

    try:
        task_data = json.loads(llm_response)
        return Task(**task_data)

    except Exception:
        return Task(
            employee="Not specified",
            task="Unable to parse task",
            deadline="Not specified",
            priority="Normal",
            summary="The AI response could not be converted into a structured task.",
            confirmation_question="Do you want to review this instruction manually?"
        )
