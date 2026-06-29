"""
Session Manager

Stores temporary workflow sessions.

Version 0.2

Current storage:
- In-memory

Future upgrade path:
- SQLite
- PostgreSQL
- Redis
"""

import uuid
from datetime import datetime


class SessionManager:

    def __init__(self):
        self.sessions = {}

    def create(self, task):
        """
        Create a new workflow session.
        """

        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {
            "task": task,
            "state": "waiting_boss_confirmation",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }

        return session_id

    def get(self, session_id):
        """
        Return a session by ID.
        """

        return self.sessions.get(session_id)

    def exists(self, session_id):
        """
        Check whether a session exists.
        """

        return session_id in self.sessions

    def update_state(self, session_id, state):
        """
        Update workflow state.
        """

        if session_id not in self.sessions:
            return False

        self.sessions[session_id]["state"] = state
        self.sessions[session_id]["updated_at"] = datetime.now()

        return True

    def delete(self, session_id):
        """
        Remove a session.
        """

        self.sessions.pop(session_id, None)

    def find_assigned_task_by_employee(self, employee_name: str):
        """
        Find the latest assigned task for an employee.
        """

        employee_name = employee_name.lower()

        latest_session = None
        latest_session_id = None
        latest_time = None

        for session_id, session in self.sessions.items():

            task = session["task"]

            if (
                task.employee.lower() == employee_name
                and session["state"] == "assigned"
            ):

                created = session["created_at"]

                if latest_time is None or created > latest_time:
                    latest_time = created
                    latest_session = session
                    latest_session_id = session_id

        return latest_session_id, latest_session

    def get_sessions_by_state(self, state):
        """
        Return all sessions matching a workflow state.
        """

        return {
            session_id: session
            for session_id, session in self.sessions.items()
            if session["state"] == state
        }

    def get_all_sessions(self):
        """
        Return all workflow sessions.
        """

        return self.sessions

    def count(self):
        """
        Return total number of active sessions.
        """

        return len(self.sessions)

    def clear(self):
        """
        Remove all sessions.
        """

        self.sessions.clear()
