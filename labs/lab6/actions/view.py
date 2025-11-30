"""
Returns the info for a specific note
"""

from .database import Database

def view(title: str) -> None:
    """
    Returns the info for a note with title
    :param title:
    :return None:
    """
    db = Database()
    notes = db.get_notes()

    if title == "":
        raise ValueError("title cannot be empty")
    if title not in notes:
        raise ValueError("title not in notes")

    print(title)
    print("---")
    print(notes[title]["content"])
    print("---")
    if "due_date" in notes[title]:
        print("Due:" + notes[title]["due_date"])
    else:
        print("No due date.")
