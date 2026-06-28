"""
Employee Directory

Loads employees from data/employees.json.
"""

import json
from pathlib import Path


class EmployeeDirectory:

    def __init__(self):

        data_file = (
            Path(__file__).parent.parent
            / "data"
            / "employees.json"
        )

        with open(data_file, "r", encoding="utf-8") as f:
            self.employees = json.load(f)

    def find_by_name(self, name: str):

        for employee in self.employees:

            if employee["name"].lower() == name.lower():
                return employee

        return None

    def find_by_chat_id(self, chat_id: int):

        for employee in self.employees:

            if employee["telegram_chat_id"] == chat_id:
                return employee

        return None

    def find_by_employee_id(self, employee_id: str):

        for employee in self.employees:

            if employee["employee_id"] == employee_id:
                return employee

        return None
