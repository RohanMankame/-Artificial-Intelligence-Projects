# Project 4: Genetic Algorithms

This project implements a generic **Genetic Algorithm (GA)**, a search heuristic inspired by the process of natural selection. The algorithm is applied to solve two different kinds of optimization problems: the combinatorial N-Queens problem and a continuous function optimization problem.

---

## 📖 Table of Contents
* [About The Project](#-about-the-project)
* [Core Components](#-core-components)
* [Problem Formulations](#-problem-formulations)
  * [N-Queens Problem](#n-queens-problem)
  * [Function Optimization](#function-optimization)
* [Prerequisites](#-prerequisites)
* [Usage Examples](#-usage-examples)

---

## 🧬 About The Project

Genetic Algorithms are a class of optimization algorithms that belong to the larger family of evolutionary algorithms. They use concepts like **selection**, **crossover**, and **mutation** to evolve a population of potential solutions toward an optimal one. This project demonstrates the flexibility of GAs by applying them to both a classic discrete problem and a continuous mathematical function.

---

## ⚙️ Core Components

### `genetic_algorithm(problem, f_thres, ngen)`
This is the main driver function for the GA. It initializes a population of candidate solutions and evolves it over a specified number of generations (`ngen`). In each generation, it uses the problem-specific methods for creating the next generation. It stops if a solution meeting the fitness threshold (`f_thres`) is found or if the maximum number of generations is reached.

### Genetic Operators
The `GeneticProblem` class for each problem implements the core operators:
-   **Selection:** Methods for choosing which individuals from a population will reproduce. Both **fitness-proportionate selection** (roulette wheel) and **rank-based selection** are implemented.
-   **Crossover:** Methods for combining the genetic information of two parents to generate new offspring. **Single-point crossover** and **arithmetic crossover** are used.
-   **Mutation:** Methods for introducing random variations into an individual's genetic code, which helps maintain diversity and avoid premature convergence.

---

## 🧩 Problem Formulations

### N-Queens Problem
`class NQueensProblem(GeneticProblem)`

This class applies the genetic algorithm to find a valid solution for the N-Queens problem.
-   **Goal:** Find a configuration of N queens on an N×N board where no two queens threaten each other.
-   **Chromosome Representation:** A chromosome is a tuple of length N, where the value at each index `i` represents the row of the queen in column `i`.
-   **Fitness Function:** The fitness of a chromosome is calculated as `(max non-attacking pairs) - (actual attacking pairs)`. A perfect solution has zero attacking pairs and thus the maximum possible fitness score.

### Function Optimization
`class FunctionProblem(GeneticProblem)`

This class uses the genetic algorithm to find the minimum value of the following two-variable function:
$$f(x,y) = x \sin(4x) + 1.1 y \sin(2y)$$
-   **Goal:** Find the `(x, y)` coordinate pair that minimizes the value of the function `f(x, y)`.
-   **Chromosome Representation:** A chromosome is a tuple `(x, y)` containing floating-point numbers representing a point in the function's domain.
-   **Fitness Function:** The fitness of a chromosome is simply the value returned by `f(x, y)`. The algorithm seeks to find the chromosome with the lowest fitness.

---

## ✅ Prerequisites

This project relies on a `Proj4_utils.py` file, which is expected to contain the base `GeneticProblem` class that the specific problem implementations inherit from.

```python
from Proj4_utils import *
```

## 🚀 Usage Examples
To use the framework, instantiate a problem class with its specific parameters and then pass it to the genetic_algorithm function.

### Solving N-Queens
Here is an example of how to set up and solve an 8-Queens problem. We define a population of 100 individuals and run the algorithm for up to 1000 generations, stopping if a perfect fitness score of 28 is achieved.

#### 1. Instantiate the N-Queens problem
```python
 Parameters: population_size, gene_bases, gene_length, mutation_probability
n_queens_problem = NQueensProblem(100, tuple(range(8)), 8, 0.2)
```

#### 2. Run the genetic algorithm
 Parameters: problem, fitness_threshold, max_generations
 ```python
max_fitness = 28  # Max non-attacking pairs for 8 queens is C(8,2) = 28
generation, solution = genetic_algorithm(n_queens_problem, f_thres=max_fitness, ngen=1000)
```

#### 3. Print the results
```python
if n_queens_problem.fitness_fn(solution) >= max_fitness:
    print(f"Solution found in generation {generation}: {solution}")
    print(f"Fitness of solution: {n_queens_problem.fitness_fn(solution)}")
else:
    print(f"No perfect solution found within {generation} generations. Best solution found: {solution}")
```
### Optimizing a Function
This example demonstrates how to find the minimum value for the given mathematical function. It initializes a population of 50 candidate solutions and runs the GA for 1000 generations.

#### 1. Instantiate the function optimization problem
 Parameters: population_size, gene_bases (max_x, max_y), gene_length, mutation_probability
 ```python
function_problem = FunctionProblem(50, (10, 10), 2, 0.2)
```

#### 2. Run the genetic algorithm
 We set f_thres to None because we don't know the minimum value beforehand.
 ```python
generation, solution = genetic_algorithm(function_problem, f_thres=None, ngen=1000)
```

#### 3. Print the results
```python
if solution:
    print(f"Best solution found after {generation} generations: {solution}")
    print(f"Minimum function value (fitness): {function_problem.fitness_fn(solution)}")
else:
    print("Could not find a solution.")
```
