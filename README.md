# Othello AI Project

This repository provides a **scaffold** for implementing the classical two-player
board game **Othello** (also known as Reversi) along with an AI opponent
powered by the Mini‑Max heuristic search algorithm and optional alpha–beta
pruning. The purpose of this scaffold is to guide your development while
respecting academic integrity policies.

## Overview

The goal of this project is to build a complete Othello game engine and AI
player. The assignment can be broken into two main parts:

1. **Implement the mechanics of the game Othello.** This includes
   representing the board, initializing play, accepting player moves (and
   rejecting illegal ones), computing which discs should be flipped,
   displaying the board after each move, keeping score, and recognizing
   when the game is complete.
2. **Implement the Mini‑Max algorithm**, with optional alpha–beta pruning and
   one or more reasonable heuristics to evaluate game states.

Language of implementation is up to you; this scaffold uses Python to
illustrate a possible structure. You are free to choose another language
provided you satisfy the assignment requirements.

## Repository Contents

| File        | Description |
|------------ |------------|
| `board.py`  | Defines a `Board` class to represent and manipulate the game state. Function bodies are placeholders for you to complete. |
| `minimax.py`| Contains a stub for the Mini‑Max search function with optional alpha–beta pruning. |
| `heuristic.py` | Provides templates for heuristic evaluation functions. |
| `utils.py`  | Includes helper functions such as parsing and formatting moves. |
| `main.py`   | Skeleton entry point that parses command‑line options and runs the game loop. |
| `README.md` | This documentation file. |

## How to Use This Scaffold

Each Python module contains function definitions and docstrings with
``TODO`` markers. Replace these markers with your own implementation code.
The skeleton is intentionally minimal so that you have the opportunity to
design and code the logic yourself. Remember to:

- Add comments and docstrings where appropriate.
- Keep your code organized and readable.
- Cite any external resources you reference for understanding concepts or
  algorithms (but do not copy code). You might keep a `worklog` file to
  document your research process if required by your instructor.

### Running the Game

Once you have implemented the necessary logic, you can play your Othello
game by running:

```bash
python main.py --depth 3 --debug --prune
```

This example runs the AI with a search depth of 3, prints debug
information about the search, and uses alpha–beta pruning. Omit the
`--debug` or `--prune` flags to disable these features.

## Academic Integrity

This scaffold is provided solely for educational purposes. **Do not** use
generative models to produce assignment code or share your completed
implementation with others. The functions in this repository are left
unfinished so that you can complete them yourself. If you seek external
information to learn about Othello rules, Mini‑Max, heuristics, or Python
constructs, be sure to paraphrase and cite sources appropriately.

## License

This project scaffold is provided without any specific license. You may
modify it for your own educational use.