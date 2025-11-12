"""
minimax.py

Provides a stub for the MiniMax algorithm with optional alpha–beta pruning used
to power the AI player in the Othello game. The function defined in this
module is responsible for exploring possible future game states to a given
depth, evaluating them with a heuristic, and returning the best move along
with its evaluation score.

Students should implement the core logic of MiniMax search, as well as
alpha–beta pruning if enabled. Refer to the assignment instructions and
lecture materials for guidance on how to structure the search tree, alternate
between maximizing and minimizing nodes, and prune branches when possible.

Functions
---------
minimax(board, depth, maximizing_player, player, alpha=None, beta=None,
        use_pruning=False, heuristic_fn=None)
    Perform a depth-limited search and return the best score and move.
"""

from __future__ import annotations

from math import inf
from typing import Callable, Optional, Tuple

from board import Board


def minimax(
    board: Board,
    depth: int,
    maximizing_player: bool,
    player: str,
    alpha: Optional[int] = None,
    beta: Optional[int] = None,
    use_pruning: bool = False,
    heuristic_fn: Optional[Callable[[Board, str], int]] = None,
    root_player: Optional[str] = None,
) -> Tuple[int, Optional[Tuple[int, int]]]:
    """Perform a minimax search and return the best heuristic score and move."""

    if heuristic_fn is None:
        raise ValueError("A heuristic function must be provided to minimax().")

    if root_player is None:
        root_player = player

    if depth == 0 or board.is_game_over():
        return heuristic_fn(board, root_player), None

    alpha_value = -inf if use_pruning and alpha is None else alpha
    beta_value = inf if use_pruning and beta is None else beta

    opponent = "W" if player == "B" else "B"
    valid_moves = board.get_valid_moves(player)

    if not valid_moves:
        if board.is_game_over() or depth == 0:
            return heuristic_fn(board, root_player), None
        score, _ = minimax(
            board,
            depth - 1,
            not maximizing_player,
            opponent,
            alpha_value,
            beta_value,
            use_pruning,
            heuristic_fn,
            root_player,
        )
        return score, None

    if maximizing_player:
        best_score = -inf
        best_move: Optional[Tuple[int, int]] = None

        for move in valid_moves:
            new_board = board.copy()
            new_board.make_move(move[0], move[1], player)
            score, _ = minimax(
                new_board,
                depth - 1,
                False,
                opponent,
                alpha_value,
                beta_value,
                use_pruning,
                heuristic_fn,
                root_player,
            )
            if score > best_score:
                best_score = score
                best_move = move
            if use_pruning:
                alpha_value = max(alpha_value, best_score)
                if beta_value is not None and alpha_value is not None and alpha_value >= beta_value:
                    break
        return best_score, best_move

    best_score = inf
    best_move = None

    for move in valid_moves:
        new_board = board.copy()
        new_board.make_move(move[0], move[1], player)
        score, _ = minimax(
            new_board,
            depth - 1,
            True,
            opponent,
            alpha_value,
            beta_value,
            use_pruning,
            heuristic_fn,
            root_player,
        )
        if score < best_score:
            best_score = score
            best_move = move
        if use_pruning:
            beta_value = min(beta_value, best_score)
            if alpha_value is not None and beta_value is not None and beta_value <= alpha_value:
                break

    return best_score, best_move
