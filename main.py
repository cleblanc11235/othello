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

from board import Board
from minimax import minimax
from heuristic import simple_heuristic
from utils import parse_move, format_move


def _opponent(player: str) -> str:
    return "W" if player == "B" else "B"


def _prompt_player_color() -> str:
    while True:
        choice = input("Choose your color (B for black, W for white): ").strip().upper()
        if choice in {"B", "W"}:
            return choice
        print("Invalid choice. Please enter 'B' or 'W'.")


def _print_scores(board: Board) -> None:
    black, white = board.count_pieces()
    print(f"Score -> Black: {black}  White: {white}")


def play_game(depth: int = 3, debug: bool = False, use_pruning: bool = False) -> None:
    """Play a game of Othello between a human and the AI."""

    board = Board()
    human_player = _prompt_player_color()
    ai_player = _opponent(human_player)

    current_player = "B"
    board.display()
    _print_scores(board)

    while not board.is_game_over():
        valid_moves = board.get_valid_moves(current_player)

        if not valid_moves:
            print(f"{current_player} has no valid moves and must pass.")
            current_player = _opponent(current_player)
            continue

        if current_player == human_player:
            while True:
                move_input = input("Enter your move (e.g., D3) or 'quit' to exit: ").strip()
                if move_input.lower() in {"quit", "exit"}:
                    print("Exiting game.")
                    return
                try:
                    move = parse_move(move_input)
                except ValueError as exc:
                    print(exc)
                    continue
                if move not in valid_moves:
                    print("Illegal move. Available moves:", ", ".join(format_move(r, c) for r, c in valid_moves))
                    continue
                board.make_move(move[0], move[1], current_player)
                break
        else:
            if debug:
                print(f"AI ({ai_player}) is thinking...")
            score, best_move = minimax(
                board,
                depth,
                True,
                ai_player,
                use_pruning=use_pruning,
                heuristic_fn=simple_heuristic,
            )
            if best_move is None:
                print("AI must pass.")
                current_player = _opponent(current_player)
                continue
            board.make_move(best_move[0], best_move[1], current_player)
            if debug:
                print(f"AI selects {format_move(best_move[0], best_move[1])} with score {score}")

        board.display()
        _print_scores(board)
        current_player = _opponent(current_player)

    black, white = board.count_pieces()
    print("Game over!")
    if black > white:
        print("Black wins!")
    elif white > black:
        print("White wins!")
    else:
        print("The game is a draw.")


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

    try:
        play_game(depth=args.depth, debug=args.debug, use_pruning=args.prune)
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")


if __name__ == "__main__":
    main()
