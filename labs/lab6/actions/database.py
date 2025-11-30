"""
Database functionality
"""

import os

import json

class Database:
    """
    Database class
    """
    def __init__(self):
        self.db_file = "notes.json"

    def get_notes(self) -> dict[str, dict[str, str]]:
        """
        Gets notes from json file
        :return dict with notes {"title" : {"content" : "note", ["due_date" : "string"] }}:
        """
        if os.path.exists(self.db_file):
            with open(self.db_file, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.decoder.JSONDecodeError:
                    return {}
        else:
            return {}

    def save_notes(self, notes: dict[str, dict[str, str]]) -> None:
        """
        Saves notes to json file
        :param notes:
        :return None:
        """

        with open(self.db_file, "w", encoding="utf-8") as f:
            f.write(json.dumps(notes))
