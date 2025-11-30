"""
Deletes a note
"""

from .database import Database


def delete(title: str) -> None:
    """
    Deletes a note
    :param title:
    :return none:
    """
    db = Database()
    notes = db.get_notes()

    if title == "":
        raise ValueError("Title is required")
    if title not in notes:
        raise ValueError("Title not found")

    del notes[title]

    db.save_notes(notes)

    print("Deleted.")
