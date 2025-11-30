"""
Бележник
"""

import argparse

from labs.lab6.actions.add import add
from labs.lab6.actions.view import view
from labs.lab6.actions.delete import delete
from labs.lab6.actions.list import list_notes
from labs.lab6.actions.edit import edit


def load_parser() -> argparse.ArgumentParser:
    """
    Loads the parser with the correct command and arguments.

    :return: Parser that can interpret add, view, delete, list, edit notes.
    """

    parser = argparse.ArgumentParser(description="Command-line Note-Taking Application")
    parser.add_argument("action",
                        choices=["add", "view", "delete", "list", "edit"],
                        help="What do you want to do?")
    parser.add_argument("--title", help="Title of the note")
    parser.add_argument("--content", help="Content of the note (only for `add` action)")
    parser.add_argument("--due-date", help="Optional due date (only for `add` action)")
    return parser


if __name__ == "__main__":
    command_parser = load_parser()
    args = command_parser.parse_args()

    try:
        if args.action == "add":
            add(args.title, args.content, args.due_date)
        elif args.action == "view":
            view(args.title)
        elif args.action == "delete":
            delete(args.title)
        elif args.action == "list":
            list_notes()
        elif args.action == "edit":
            edit(args.title, args.content, args.due_date)
        else:
            raise ValueError("Invalid action.")

    except ValueError as e:
        raise ValueError(f"Error processing action:. {e}") from e
