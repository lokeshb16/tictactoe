# AI-Based Tic-Tac-Toe 

A professional, interactive Tic-Tac-Toe game built in Python where you play against an unbeatable AI opponent powered by the **Minimax Algorithm** with **Alpha-Beta Pruning**. This project was developed as part of the **Week 1 Internship Task**.

---

## Key Features

* **Unbeatable AI Brain:** Uses the recursive Minimax algorithm to evaluate every possible move and ensure the AI never makes a mistake.
* **Alpha-Beta Pruning:** Optimizes the AI's thinking process by cutting down unnecessary branches in the game tree, making it run instantly.
* **Multiple Difficulty Levels:** Supports `easy`, `medium`, and `hard` modes to test your skills.
* **Live Score Tracking:** Dynamically maintains and updates the scoreboard showing Wins, Losses, Draws, and your overall Win Rate (%) across multiple games.

---

## Core Components & Logic

1. **Board Representation:** The game board is represented as a flat list of 9 elements, mapped perfectly to a classic grid layout.
2. **Win Condition Checker (`WIN_COMBOS`):** Checks 8 specific winning combinations (3 rows, 3 columns, and 2 diagonals) after every turn.
3. **Minimax Engine:** * Scores the board dynamically: `+1` for an AI win, `-1` for a Human win, and `0` for a Draw.
   * Simulates future moves recursively to select the optimal position.

---

## Tech Stack Used

* **Language:** Python 
* **Core Concepts:** Recursion, Game Trees, Minimax Algorithm

---

##  How to Run the Project Locally

### Prerequisites
Make sure you have Python installed on your system. You can verify it by running:
```bash
python --version