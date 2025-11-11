"""
main.py

Entry point for the Othello game. This module orchestrates gameplay,
including human player interaction and AI moves using the minimax algorithm
defined in ``minimax.py``. By running this script directly, you can play
Othello against a computer opponent or observe AI-versus-AI matches.

To maintain academic integrity, the primary game loop and AI integration are
provided only as function stubs. You must implement the game logic
yourself, including managing turns, handling user input, invoking the
minimax search, and updating the board state.

Usage example::

    python main.py --depth 4 --debug --prune

Functions
---------
play_game(depth, debug, use_pruning)
    Run a full game between a human and the AI with specified search settings.
main()
    Parse command-line arguments and start the game.
"""

import argparse
from typing import Optional

from board import Board
from minimax import minimax
from heuristic import simple_heuristic
from utils import parse_move, format_move


def play_game(depth: int = 3, debug: bool = False, use_pruning: bool = False) -> None:
    """Play a game of Othello between a human and the AI.

    Parameters
    ----------
    depth : int, optional
        Search depth for the AI (default is 3).
    debug : bool, optional
        If True, print debug information about the AI's search (default is False).
    use_pruning : bool, optional
        If True, enable alpha–beta pruning (default is False).

    Notes
    -----
    This function should create a Board instance, prompt the user to choose a
    color (black moves first), then alternate between human and AI moves
    until the game ends. After each move, display the board and current
    score. When the game is over, announce the winner. If ``debug`` is
    enabled, you may call the ``minimax`` function with instrumentation to
    display explored nodes and heuristic values.

    ``TODO``: Implement the main game loop.
    """
    # TODO: implement game loop
    pass


def main() -> None:
    """Parse command-line arguments and start an Othello game."""
    parser = argparse.ArgumentParser(description="Play Othello against an AI using the minimax algorithm.")
    parser.add_argument(
        "--depth",
        type=int,
        default=3,
        help="Search depth for the AI (default: 3)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode to display search details",
    )
    parser.add_argument(
        "--prune",
        action="store_true",
        help="Enable alpha–beta pruning",
    )
    args = parser.parse_args()

    play_game(depth=args.depth, debug=args.debug, use_pruning=args.prune)


if __name__ == "__main__":
    main()