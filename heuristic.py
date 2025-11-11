"""
heuristic.py

Defines placeholder heuristic functions for evaluating Othello board states.
These functions take a ``Board`` instance and a player symbol ('B' or 'W')
and return an integer representing the desirability of the position from the
perspective of the given player. Positive values indicate advantage to the
player, while negative values favor the opponent.

You are encouraged to experiment with different heuristics and combine them
using weights. Typical considerations include piece difference, mobility
(number of legal moves), corner occupancy, edge control, and stability of
discs. The stubs provided here illustrate a few basic ideas but contain no
implementation.

Functions
---------
simple_heuristic(board, player)
    Evaluate based on the difference in piece counts.
mobility_heuristic(board, player)
    Evaluate based on the difference in the number of legal moves.
corner_heuristic(board, player)
    Evaluate based on control of the four corners.
"""

from typing import Any
from board import Board


def simple_heuristic(board: Board, player: str) -> int:
    """Return a simple heuristic value based on piece count difference.

    Parameters
    ----------
    board : Board
        Current game state.
    player : str
        Player symbol ('B' or 'W') for whom the heuristic is being
        calculated.

    Returns
    -------
    int
        Positive if ``player`` has more pieces than the opponent, negative
        if fewer.

    ``TODO``: Implement piece difference heuristic.
    """
    # TODO: implement piece count heuristic
    return 0


def mobility_heuristic(board: Board, player: str) -> int:
    """Return a heuristic value based on the difference in legal moves.

    The idea is that a position where you have more options than your
    opponent is generally better.

    Parameters
    ----------
    board : Board
        Current game state.
    player : str
        Player symbol ('B' or 'W').

    Returns
    -------
    int
        Positive if ``player`` can move to more squares than the opponent,
        negative if fewer.

    ``TODO``: Implement mobility heuristic.
    """
    # TODO: implement mobility heuristic
    return 0


def corner_heuristic(board: Board, player: str) -> int:
    """Return a heuristic value based on control of the corners.

    The four corners of the Othello board are particularly valuable because
    discs placed there cannot be outflanked. Occupying a corner is usually
    advantageous, while allowing your opponent to do so is disadvantageous.

    Parameters
    ----------
    board : Board
        Current game state.
    player : str
        Player symbol ('B' or 'W').

    Returns
    -------
    int
        A positive value if ``player`` occupies more corners than the
        opponent; negative if fewer.

    ``TODO``: Implement corner control heuristic.
    """
    # TODO: implement corner control heuristic
    return 0