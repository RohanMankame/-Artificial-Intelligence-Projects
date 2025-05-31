# Project 2: Uninformed Search and Classical Problems

This project implements fundamental uninformed search algorithms and applies them to solve classic problems in Artificial Intelligence. It provides a framework for defining problems and finding solutions using Depth-First Search and Breadth-First Search.

---

## 📜 Table of Contents
* [About the Project](#about-the-project)
* [Algorithms Implemented](#algorithms-implemented)
* [Problems Formulated](#problems-formulated)
* [Prerequisites](#prerequisites)
* [Usage Examples](#usage-examples)
  * [Coin Puzzle](#coin-puzzle)
  * [N-Queens Problem](#n-queens-problem)
  * [Graph Problem](#graph-problem)

---

## 📖 About The Project

This project contains implementations of the following:
1.  **Uninformed Search Algorithms:** Generic search strategies that do not use any domain-specific knowledge to guide the search.
2.  **Problem Formulations:** Classic AI problems structured to be solved by these search algorithms. Each problem defines an initial state, possible actions, transition results, and a goal test.

---

## ⚙️ Algorithms Implemented

### Depth-First Search (DFS)
`depth_first_search(problem)`

A search algorithm that explores as far as possible along each branch before backtracking. It uses a Last-In, First-Out (LIFO) strategy via a stack (implemented with `collections.deque`).

### Breadth-First Search (BFS)
`breadth_first_search(problem)`

A search algorithm that explores all neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. It uses a First-In, First-Out (FIFO) strategy via a queue (implemented with `collections.deque`).

---

## 🧩 Problems Formulated

### Coin Puzzle
`class CoinPuzzle(Problem)`

This class formulates the problem of finding a combination of coins that sum up to a target value.
-   **State:** The remaining amount to be made.
-   **Actions:** Using one of the available coins.
-   **Goal:** The remaining amount is zero.

### N-Queens Problem
`class NQueensProblem(Problem)`

This class formulates the classic problem of placing N queens on an N×N chessboard so that no two queens threaten each other.
-   **State:** A tuple representing the column position of the queen in each row. A `-1` indicates an unplaced queen.
-   **Actions:** Placing a queen in a "safe" square in the next available column.
-   **Goal:** All N queens are placed on the board in safe positions.

### Graph Problem
`class GraphProblem(Problem)`

A generic problem formulation for finding a path between two nodes in a given graph.
-   **State:** The current node in the graph.
--  **Actions:** Moving to an adjacent node.
-   **Goal:** Reaching the specified destination node.

---

## ✅ Prerequisites

This project requires the `Utils` library, which should contain the base `Problem`, `Node`, and `Graph` classes.

```python
from hw2_utils import *
