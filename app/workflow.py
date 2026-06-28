"""
Workflow Engine

Coordinates the flow between the Telegram bot,
task parser, and local LLM.
"""


class WorkflowEngine:

    def process_message(self, message: str):

        print("Received message:")

        print(message)

        return {
            "status": "received",
            "message": message
        }
