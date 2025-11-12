"""
utils.py

Miscellaneous utility functions for the Othello project. These helpers
facilitate tasks such as parsing user input and converting between human-
friendly board coordinates (e.g. "D3") and zero-based array indices.

These functions are intentionally left unimplemented for you to complete.

Functions
---------
parse_move(move_str)
    Convert a move string like 'D3' into a (row, column) tuple.
format_move(row, col)
    Convert a (row, column) tuple into a human-readable move string.
"""

from typing import Tuple


def parse_move(move_str: str) -> Tuple[int, int]:
    """Convert a move such as 'D3' to a zero-based (row, column) tuple."""

    if move_str is None:
        raise ValueError("Move string cannot be None.")

    cleaned = move_str.strip().upper()
    if len(cleaned) != 2:
        raise ValueError(f"Invalid move '{move_str}'. Expected format like 'D3'.")

    column_char, row_char = cleaned[0], cleaned[1]
    if column_char < "A" or column_char > "H":
        raise ValueError(f"Invalid column '{column_char}'. Must be between A and H.")

    if row_char < "1" or row_char > "8":
        raise ValueError(f"Invalid row '{row_char}'. Must be between 1 and 8.")

    col_index = ord(column_char) - ord("A")
    row_index = int(row_char) - 1
    return row_index, col_index


def format_move(row: int, col: int) -> str:
    """Convert a zero-based (row, column) pair into a human-readable move."""

    if not (0 <= row < 8 and 0 <= col < 8):
        raise ValueError("Row and column must be between 0 and 7 inclusive.")

    column_char = chr(ord("A") + col)
    row_char = str(row + 1)
    return f"{column_char}{row_char}"
