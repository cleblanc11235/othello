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
    """Convert a move such as 'D3' to a zero-based (row, column) tuple.

    Parameters
    ----------
    move_str : str
        A two-character string consisting of a column letter (A–H or a–h)
        followed by a row number (1–8). Whitespace should be ignored.

    Returns
    -------
    Tuple[int, int]
        A tuple ``(row_index, col_index)`` with zero-based indices.

    Raises
    ------
    ValueError
        If ``move_str`` does not denote a valid board coordinate.

    ``TODO``: Implement move parsing with appropriate validation and error
    handling.
    """
    # TODO: implement move parsing
    return (0, 0)


def format_move(row: int, col: int) -> str:
    """Convert a zero-based (row, column) pair into a human-readable move.

    Parameters
    ----------
    row, col : int
        Zero-based indices representing a square on the board.

    Returns
    -------
    str
        A two-character string such as 'D3'. This is the inverse of
        ``parse_move``.

    ``TODO``: Implement move formatting.
    """
    # TODO: implement move formatting
    return "A1"