"""
Employee Directory

Loads employee information from data/employees.json
and provides helper methods for employee lookup.
"""

import json
from pathlib import Path


class EmployeeDirectory:

    def __init__(self):
        """
        Load employees from employees.json.
        """

        data_file = (
            Path(__file__).parent.parent
            / "data"
            / "employees.json"
        )

        with open(data_file, "r", encoding="utf-8") as file:
            self.employees = json.load(file)

    def get_all(self):
        """
        Return all employees.
        """

        return self.employees

    def find_by_name(self, name: str):
        """
        Find employee by name.
        """

        if not name:
            return None

        name = name.strip().lower()

        for employee in self.employees:

            employee_name = employee.get(
                "name",
                ""
            ).strip().lower()

            if employee_name == name:
                return employee

        return None

    def find_by_chat_id(self, chat_id: int):
        """
        Find employee by Telegram Chat ID.
        """

        if chat_id is None:
            return None

        try:
            chat_id = int(chat_id)
        except (TypeError, ValueError):
            return None

        for employee in self.employees:

            employee_chat_id = employee.get(
                "telegram_chat_id"
            )

            if employee_chat_id == chat_id:
                return employee

        return None

    def find_by_employee_id(self, employee_id: str):
        """
        Find employee by Employee ID.
        """

        if not employee_id:
            return None

        employee_id = employee_id.strip().upper()

        for employee in self.employees:

            current_id = employee.get(
                "employee_id",
                ""
            ).strip().upper()

            if current_id == employee_id:
                return employee

        return None

    def employee_exists(self, chat_id: int):
        """
        Return True if Telegram Chat ID belongs
        to a registered employee.
        """

        return self.find_by_chat_id(chat_id) is not None

    def employee_name_exists(self, name: str):
        """
        Return True if employee name exists.
        """

        return self.find_by_name(name) is not None
