"""
Edit a note in the database
"""

from .database import Database

def edit(title: str, content: str, due_date: str) -> None:
    """
    Edit a note
    :param title:
    :param content:
    :param due_date:
    :return:
    """
    db = Database()
    notes = db.get_notes()

    if title not in notes:
        raise ValueError(f"Note with title '{title}' does not exist.")

    if not content and due_date is None:
        raise ValueError("No content or due date provided - no changes made to the note.")

    if content:
        notes[title]["content"] = content

    if due_date is not None:
        if due_date.lower() == "none":
            if "due_date" in notes[title]:
                del notes[title]["due_date"]
        else:
            notes[title]["due_date"] = due_date

    db.save_notes(notes)

    print("Note successfully edited.")
