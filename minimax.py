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
) -> Tuple[int, Optional[Tuple[int, int]]]:
    """Perform a minimax search and return the best heuristic score and move.

    Parameters
    ----------
    board : Board
        The current game state to evaluate.
    depth : int
        The remaining depth of the search tree. At depth zero or when the game
        is over, the heuristic function is applied to evaluate the position.
    maximizing_player : bool
        True if the current node is maximizing (AI's turn), False if
        minimizing (opponent's turn).
    player : str
        The color of the player ('B' or 'W') whose turn it is at this node.
    alpha : Optional[int], default None
        Alpha value for pruning; best already explored option along the path
        to the root for the maximizer. Only used if ``use_pruning`` is True.
    beta : Optional[int], default None
        Beta value for pruning; best already explored option along the path
        to the root for the minimizer. Only used if ``use_pruning`` is True.
    use_pruning : bool, default False
        Enable alpha–beta pruning if True.
    heuristic_fn : Optional[Callable[[Board, str], int]], default None
        Function that takes a Board and a player symbol and returns an
        evaluation score. If None, the caller must ensure a valid heuristic
        function is passed.

    Returns
    -------
    Tuple[int, Optional[Tuple[int, int]]]
        A pair ``(best_score, best_move)`` where ``best_move`` is a (row,
        column) tuple for the chosen move or None if no legal moves exist.

    ``TODO``: Implement the minimax algorithm with optional alpha–beta pruning.
    """
    # TODO: implement minimax search
    return 0, None