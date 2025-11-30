"""
Add a note to database
"""

from .database import Database

def add(title: str, content: str, due_date: str) -> None:
    """
    Add a note to database
    :param title:
    :param content:
    :param due_date:
    :return:
    """
    db = Database()
    notes = db.get_notes()

    if title == "":
        raise ValueError("title cannot be empty")
    if content == "":
        raise ValueError("content cannot be empty")
    if title in notes:
        raise ValueError("title already exists")

    if due_date:
        notes[title] = {
            "content": content,
            "due_date": due_date
        }
    else:
        notes[title] = {
            "content": content,
        }

    db.save_notes(notes)

    print("Added new note", title)
