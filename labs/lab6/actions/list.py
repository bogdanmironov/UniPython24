"""
Lists all notes
"""

from .database import Database


def list_notes() -> None:
    """
    List all notes from json
    :return:
    """
    db = Database()
    notes = db.get_notes()

    print("Listing notes...")
    if len(notes) == 0:
        print("Nothing to list.")
    else:
        for title in notes:
            print("- "
                  + title
                  + " (Due: " + (notes[title]["due_date"] if "due_date" in notes[title] else "None")
                  + ")")
