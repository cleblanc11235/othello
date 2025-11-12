"""
board.py

Defines the ``Board`` class to represent and manipulate the state of an Othello game.

The responsibility of this module is to maintain the 8×8 board, determine legal
moves, apply moves, flip discs according to the rules, count pieces, and detect
when the game has concluded. None of the actual game logic is implemented here;
instead, function bodies have been left with ``TODO`` markers for you to fill
out as part of your assignment. See the project README for an overview of
expected behavior.

Classes
-------
Board
    Encapsulates the game state and provides methods to query and mutate it.

Note
----
The code you provide in this file must be your own work. Do not copy or
request complete implementations from others or generative systems.
"""

from __future__ import annotations

from typing import List, Tuple


class Board:
    """Represents an 8×8 Othello board and provides basic operations.

    The board uses a two-dimensional list to store the current positions. Each
    element is a single-character string: ``'B'`` for a black disc, ``'W'``
    for a white disc, and ``'.'`` for an empty square. Coordinates are
    represented as (row, column) pairs with zero-based indices.
    """

    BOARD_SIZE = 8
    DIRECTIONS = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def __init__(self, grid: List[List[str]] | None = None) -> None:
        """Initialize the board with the standard starting position."""

        if grid is not None:
            self.grid = [row[:] for row in grid]
            return

        self.grid = [["." for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        mid = self.BOARD_SIZE // 2
        self.grid[mid - 1][mid - 1] = "W"
        self.grid[mid - 1][mid] = "B"
        self.grid[mid][mid - 1] = "B"
        self.grid[mid][mid] = "W"

    def display(self) -> None:
        """Print an ASCII representation of the current board state."""

        header = "  " + " ".join(chr(ord("A") + c) for c in range(self.BOARD_SIZE))
        print(header)
        for idx, row in enumerate(self.grid, start=1):
            print(f"{idx} " + " ".join(row) + f" {idx}")
        print(header)

    def get_valid_moves(self, player: str) -> List[Tuple[int, int]]:
        """Return a list of legal moves for ``player``."""

        if player not in {"B", "W"}:
            raise ValueError("Player must be 'B' or 'W'.")

        opponent = "W" if player == "B" else "B"
        valid_moves: List[Tuple[int, int]] = []

        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                if self.grid[row][col] != ".":
                    continue
                flips = self._discs_to_flip(row, col, player, opponent)
                if flips:
                    valid_moves.append((row, col))

        return valid_moves

    def make_move(self, row: int, col: int, player: str) -> bool:
        """Place a disc for ``player`` at (``row``, ``col``) and flip discs."""

        if not self._is_on_board(row, col) or self.grid[row][col] != ".":
            return False

        opponent = "W" if player == "B" else "B"
        discs_to_flip = self._discs_to_flip(row, col, player, opponent)

        if not discs_to_flip:
            return False

        self.grid[row][col] = player
        for r, c in discs_to_flip:
            self.grid[r][c] = player
        return True

    def count_pieces(self) -> Tuple[int, int]:
        """Count the number of black and white discs on the board."""

        black = sum(cell == "B" for row in self.grid for cell in row)
        white = sum(cell == "W" for row in self.grid for cell in row)
        return black, white

    def is_game_over(self) -> bool:
        """Return True if neither player has a legal move remaining."""

        if self.get_valid_moves("B"):
            return False
        if self.get_valid_moves("W"):
            return False
        return True

    def copy(self) -> "Board":
        """Return a deep copy of the current board."""

        return Board(self.grid)

    def _is_on_board(self, row: int, col: int) -> bool:
        """Return True if (row, col) lies within the board boundaries."""

        return 0 <= row < self.BOARD_SIZE and 0 <= col < self.BOARD_SIZE

    def _discs_to_flip(
        self, row: int, col: int, player: str, opponent: str
    ) -> List[Tuple[int, int]]:
        """Return a list of opponent discs that would be flipped by a move."""

        discs_to_flip: List[Tuple[int, int]] = []

        for d_row, d_col in self.DIRECTIONS:
            r, c = row + d_row, col + d_col
            path: List[Tuple[int, int]] = []

            while self._is_on_board(r, c) and self.grid[r][c] == opponent:
                path.append((r, c))
                r += d_row
                c += d_col

            if not path:
                continue

            if self._is_on_board(r, c) and self.grid[r][c] == player:
                discs_to_flip.extend(path)

        return discs_to_flip
