# Project 3: Informed (Heuristic) Search Algorithms

This project implements informed search algorithms that leverage problem-specific knowledge to find solutions more efficiently than uninformed methods. It provides implementations of Best-First Search and Uniform-Cost Search and applies them to solve complex problems like the N-Queens puzzle, graph traversal, and the Eight Puzzle.

---

## 📖 Table of Contents
* [About The Project](#-about-the-project)
* [Algorithms Implemented](#-algorithms-implemented)
* [Problem Formulations](#-problem-formulations)
* [Prerequisites](#-prerequisites)
* [Usage Examples](#-usage-examples)

---

## 🌟 About The Project

This project expands on the search framework from previous assignments by introducing **informed search** strategies. These algorithms use a **heuristic function**, `h(n)`, which estimates the cost of the cheapest path from a node `n` to a goal state. This allows the search to prioritize more promising paths, often finding solutions much faster.

---

## ⚙️ Algorithms Implemented

### Best-First Search
`best_first_search(problem)`

A greedy search algorithm that always expands the node that appears to be closest to the goal, as determined by the heuristic function `h(n)`. It does not consider the cost of the path taken so far.

### Uniform-Cost Search (UCS)
`uniform_cost_search(problem)`

An algorithm that finds the path with the lowest total cost by always expanding the node with the minimum path cost, `g(n)`. UCS is optimal and complete, meaning it's guaranteed to find the cheapest solution if one exists.

---

## 🧩 Problem Formulations

The classic problems from the previous project have been enhanced with cost and heuristic functions, and the new Eight Puzzle has been introduced.

### N-Queens Problem
`class NQueensProblem(Problem)`
This problem is now equipped with:
-   **Path Cost `g(n)`:** Each step (placing a queen) has a uniform cost of 1.
-   **Heuristic `h(n)`:** The heuristic value is the **total number of conflicts** on the board (i.e., the number of pairs of queens that are attacking each other).

### Graph Problem
`class GraphProblem(Problem)`
The graph problem now uses more sophisticated cost and heuristic calculations:
-   **Path Cost `g(n)`:** The cumulative cost is calculated using the actual weights of the edges in the graph.
-   **Heuristic `h(n)`:** The heuristic is determined dynamically:
    1.  It uses pre-defined heuristic values if the graph has a `heuristics` dictionary.
    2.  It calculates the **Euclidean (straight-line) distance** to the goal if the graph has a `locations` dictionary with (x, y) coordinates.
    3.  It defaults to infinity if no heuristic information is available.

### Eight Puzzle
`class EightPuzzle(Problem)`
This is a new formulation of the classic sliding tile puzzle.
-   **State:** A tuple representing the 3x3 grid, with `0` as the blank space.
-   **Path Cost `g(n)`:** Each move (sliding a tile) has a uniform cost of 1.
-   **Heuristic `h(n)`:** The heuristic is the sum of the **Manhattan distances** of all misplaced tiles from their goal positions. The Manhattan distance is the total number of horizontal and vertical steps required to move a tile to its correct spot.

---

## ✅ Prerequisites

This project requires the `Proj3_utils.py` file, which should contain the base `Problem` and `Node` classes used by the algorithms and problem formulations.
```python
from Proj3_utils import *
```


## 🚀 Usage Examples
To use the framework, instantiate a problem and pass it to one of the search functions.

Example for N-Queens
eight_queens_problem = NQueensProblem(8)
solution_node = best_first_search(eight_queens_problem)

Example for the Eight Puzzle
Initial state might be (1,0,3,4,2,5,7,8,6)
Goal state is (1,2,3,4,5,6,7,8,0)
puzzle = EightPuzzle(init_state=(1,0,3,4,2,5,7,8,6), goal_state=(1,2,3,4,5,6,7,8,0))
solution_node = uniform_cost_search(puzzle)

Example for Graph Traversal
Assuming romania_map is a Graph object with edge costs and locations
romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
solution_node = best_first_search(romania_problem)
