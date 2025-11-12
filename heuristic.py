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

from board import Board


def _opponent(player: str) -> str:
    return "W" if player == "B" else "B"


def simple_heuristic(board: Board, player: str) -> int:
    """Return a simple heuristic value based on piece count difference."""

    black, white = board.count_pieces()
    if player == "B":
        return black - white
    return white - black


def mobility_heuristic(board: Board, player: str) -> int:
    """Return a heuristic value based on the difference in legal moves."""

    opponent = _opponent(player)
    player_moves = len(board.get_valid_moves(player))
    opponent_moves = len(board.get_valid_moves(opponent))
    return player_moves - opponent_moves


def corner_heuristic(board: Board, player: str) -> int:
    """Return a heuristic value based on control of the corners."""

    corners = [
        (0, 0),
        (0, board.BOARD_SIZE - 1),
        (board.BOARD_SIZE - 1, 0),
        (board.BOARD_SIZE - 1, board.BOARD_SIZE - 1),
    ]
    opponent = _opponent(player)
    score = 0

    for row, col in corners:
        if board.grid[row][col] == player:
            score += 1
        elif board.grid[row][col] == opponent:
            score -= 1

    return score
