
from Utils import *
from collections import deque
import math

# Add your imports here if used
from operator import attrgetter





##########################################################
# 1. Best-First, Uniform-Cost
##########################################################


def best_first_search(problem):
    node = Node(problem.init_state, heuristic=problem.h(problem.init_state))
    frontier = deque([node])
    explored = {problem.init_state}

    while frontier:
        minNode = min(frontier,key=attrgetter('heuristic'))  # get node with min heuristic
        frontier.remove(minNode)  # Remove node

        if problem.goal_test(minNode.state): #found goal
            return minNode #return goal if found

        for child in minNode.expand(problem): # visit children
            if child.state not in explored: #if not explored add child to explored and frontier
                explored.add(child.state)
                frontier.append(child)

    return None  # goal not found




def uniform_cost_search(problem):
    node = Node(problem.init_state)
    frontier = deque([node])
    explored = {problem.init_state}

    while frontier:
        minNodeCurr = min(frontier, key=attrgetter('path_cost')) # get node with min heuristic
        frontier.remove(minNodeCurr)  # Remove node

        if problem.goal_test(minNodeCurr.state): #found goal
            return minNodeCurr #return goal if found

        explored.add(minNodeCurr.state)  # add explored

        for child in minNodeCurr.expand(problem): # visit children
            if child.state not in explored and child not in frontier: #check child already visited
                frontier.append(child)  # Add child to frontier
            elif child in frontier:
                # Check which path is shortest if already a path to child exists
                for minPathChildNode in frontier:
                    if minPathChildNode.state ==child.state:
                        if minPathChildNode.path_cost > child.path_cost:
                            frontier.remove(minPathChildNode)
                            frontier.append(child)
                        break  #break after setting new min path for child

    return None  # goal not found







##########################################################
# 2. N-Queens Problem
##########################################################


class NQueensProblem(Problem):
    """
    The implementation of the class NQueensProblem related
    to Homework 2 is given for those students who were not
    able to complete it in Homework 2.
    
    Note that you do not have to use this implementation.
    Instead, you can use your own implementation from
    Homework 2.


    """
    
    def __init__(self, n):
        super().__init__(tuple([-1] * n))
        self.n = n
        

    def actions(self, state):
        if state[-1] != -1:   # if all columns are filled
            return []         # then no valid actions exist
        
        valid_actions = list(range(self.n))
        col = state.index(-1) # index of leftmost unfilled column
        for row in range(self.n):
            for c, r in enumerate(state[:col]):
                if self.conflict(row, col, r, c) and row in valid_actions:
                    valid_actions.remove(row)
                    
        return valid_actions

        
    def result(self, state, action):
        col = state.index(-1) # leftmost empty column
        new = list(state[:])  
        new[col] = action     # queen's location on that column
        return tuple(new)

    
    def goal_test(self, state):
        if state[-1] == -1:   # if there is an empty column
            return False;     # then, state is not a goal state

        for c1, r1 in enumerate(state):
            for c2, r2 in enumerate(state):
                if (r1, c1) != (r2, c2) and self.conflict(r1, c1, r2, c2):
                    return False
        return True

    
    def conflict(self, row1, col1, row2, col2):
        return row1 == row2 or col1 == col2 or abs(row1-row2) == abs(col1-col2)

    
    def g(self, cost, from_state, action, to_state):
        """
        Return path cost from start state to to_state via from_state.
        The path from start_state to from_state costs the given cost
        and the action that leads from from_state to to_state
        costs 1.
        """
        newCost = cost + 1
        return newCost


    def h(self, state):
        """
        Returns the heuristic value for the given state.
        Use the total number of conflicts in the given
        state as a heuristic value for the state.
        """
        conflicts = 0
        #taken form goal_test function to check if there is conflict if so add 1 to conflicts
        for c1, r1 in enumerate(state):
            for c2, r2 in enumerate(state):
                if (r1, c1) != (r2, c2) and self.conflict(r1, c1, r2, c2): #if conflict add 1
                    conflicts = conflicts + 1

        heuristic = conflicts #total huristic val

        return heuristic

'''TEST CASES
eight_queens = NQueensProblem(8)
print(eight_queens.h((-1,-1,-1,-1,-1,-1,-1,-1)))
print(eight_queens.h((7,-1,-1,-1,-1,-1,-1,-1)))
print(eight_queens.h((7,1,-1,-1,-1,-1,-1,-1)))
print(eight_queens.h((7,1,3,-1,-1,-1,-1,-1)))
print(eight_queens.h((7,1,3,0,-1,-1,-1,-1)))
print(eight_queens.h((7,1,3,0,6,-1,-1,-1)))
print(eight_queens.h((7,1,3,0,6,4,-1,-1)))
print(eight_queens.h((7,1,3,0,6,4,2,-1)))
print(eight_queens.h((7,1,3,0,6,4,2,5)))
'''
##########################################################
# 3. Graph Problem
##########################################################



class GraphProblem(Problem):
    """
    The implementation of the class GraphProblem related
    to Homework 2 is given for those students who were
    not able to complete it in Homework 2.
    
    Note that you do not have to use this implementation.
    Instead, you can use your own implementation from
    Homework 2.


    """
    
    
    def __init__(self, init_state, goal_state, graph):
        super().__init__(init_state, goal_state)
        self.graph = graph

        
    def actions(self, state):
        """Returns the list of adjacent states from the given state."""
        return list(self.graph.get(state).keys())

    
    def result(self, state, action):
        """Returns the resulting state by taking the given action.
            (action is the adjacent state to move to from the given state)"""
        return action

    
    def goal_test(self, state):
        return state == self.goal_state

    def get_edge_cost(graph, from_state, to_state):
        edges = graph.edges
        if from_state in edges:
            for neighbor, cost in edges[from_state].items():
                if neighbor == to_state:
                    return cost
        return 1  # Default cost if not found

    def g(self, cost, from_state, action, to_state):
        """
        Returns the path cost from root to to_state.
        Note that the path cost from the root to from_state
        is the give cost and the given action taken at from_state
        will lead you to to_state with the cost associated with
        the action.
        """

        NextCity = self.graph.edges
        CurrCost = cost
        if from_state in NextCity:
            for neighbor, cost in NextCity[from_state].items():
                if neighbor == to_state: #we can travel to the to_state
                    return cost + CurrCost #total cost = cost + new travel cost
        else:       #else just give back current cost
            return cost
    

    def h(self, state):
        """
        Returns the heuristic value for the given state. Heuristic
        value of the state is calculated as follows:
        1. if an attribute called 'heuristics' exists:
           - heuristics must be a dictionary of states as keys
             and corresponding heuristic values as values
           - so, return the heuristic value for the given state
        2. else if an attribute called 'locations' exists:
           - locations must be a dictionary of states as keys
             and corresponding GPS coordinates (x, y) as values
           - so, calculate and return the straight-line distance
             (or Euclidean norm) from the given state to the goal
             state
        3. else
           - cannot find nor calculate heuristic value for given state
           - so, just return a large value (i.e., infinity)
        """

        if hasattr(self.graph, 'heuristics'): #if attribute heuristics exists in graph
            return self.graph.heuristics[state] # value associated with given state

        elif hasattr(self.graph, 'locations'): #if attribute locations exists in graph

            currLocation = self.graph.locations[state] #(x, y) coordinates of current state
            goalLocation = self.graph.locations[self.goal_state] #(x, y) coordinates of goal state

            # Calculate the distance of x and y distances from current to goal state
            x = currLocation[0] - goalLocation[0]
            y = currLocation[1] - goalLocation[1]

            distance = math.sqrt(x ** 2 + y ** 2) # h^2 = x^2 + y^2 get hypotenuse h as shortest distance
            return distance

        else: # no heuristics nor locations
            return math.inf  # return large val


'''TESTCASES
# Create a Graph instance
romania_map = Graph(romania_roads, False)

# Create a GraphProblem instance using the romania_map
romania = GraphProblem('Arad', 'Bucharest', romania_map)

# Now you can use the romania object to call the g method
print(romania.g(0, 'Arad', 'Zerind', 'Zerind'))
print(romania.g(0, 'Arad', 'Sibiu', 'Sibiu'))
print(romania.g(140, 'Sibiu', 'Rimnicu', 'Rimnicu'))
print(romania.g(220, 'Rimnicu', 'Pitesti', 'Pitesti'))
print(romania.g(317, 'Pitesti', 'Bucharest', 'Bucharest'))

print(romania.h('Arad'))
print(romania.h('Sibiu'))
print(romania.h('Rimnicu'))
print(romania.h('Pitesti'))
print(romania.h('Bucharest'))

romania_map.locations = romania_city_positions
romania = GraphProblem('Arad', 'Bucharest', romania_map)
print(romania.h('Arad'))
print(romania.h('Sibiu'))
print(romania.h('Fagaras'))
print(romania.h('Pitesti'))
print(romania.h('Rimnicu'))
print(romania.h('Bucharest'))

roads = dict(S=dict(A=1, B=2), A=dict(C=1),B=dict(C=2),C=dict(G=100))
roads_h = dict(S=90 , A=100, B=88 , C=100 , G=0)
roads_map =Graph(roads, True)
roads_map.heuristics = roads_h

problem = GraphProblem('S','G', roads_map)
print(problem.h('S'))
print(problem.h('A'))
print(problem.h('B'))
print(problem.h('C'))
print(problem.h('G'))
'''
##########################################################
# 4. Eight Puzzle
##########################################################


class EightPuzzle(Problem):
    def __init__(self, init_state, goal_state=(1,2,3,4,5,6,7,8,0)):
        super().__init__(init_state, goal_state)
    

    def actions(self, state):
        i = state.index(0)
        validMoves = []

        if i != 0 and i != 1 and i != 2:  # blank can move up if not in top row
            validMoves.append('UP')

        if i != 6 and i != 7 and i != 8:  # blank can move down if not in bottom row
            validMoves.append('DOWN')

        if i != 0 and i != 3 and i != 6:  # blank can go left if not in left col
            validMoves.append('LEFT')

        if i != 2 and i != 5 and i != 8:  # blank can go right if not in right col
            validMoves.append('RIGHT')

        return validMoves

    
    def result(self, state, action):
        blankIdx = state.index(0)
        puzzleBoard = list(state)  # copy game board

        if action == 'UP':
            newBlankIdx = blankIdx - 3 #moves 3 indexes back to go up

        elif action == 'DOWN':
            newBlankIdx = blankIdx + 3 #moves 3 indexes front to go down

        elif action == 'LEFT':
            newBlankIdx = blankIdx -1 #moves 1 index back to go left

        elif action == 'RIGHT':
            newBlankIdx = blankIdx + 1 #moves 1 index front to go right

        else:
            return None  # Not a possible action

        puzzleBoard[blankIdx] = puzzleBoard[newBlankIdx] #move num to the blank index
        puzzleBoard[newBlankIdx] = 0 #set blank where num was before we moved it

        return tuple(puzzleBoard)  # return tuple of new game board after move

    
    def goal_test(self, state):
        if state == self.goal_state: #if is goal state
            return True
        else:
            return False #else it is not a goal state
    

    def g(self, cost, from_state, action, to_state):
        """
        Return path cost from root to to_state via from_state.
        The path from root to from_state costs the given cost
        and the action that leads from from_state to to_state
        costs 1.
        """
        return cost + 1
    

    def h(self, state):
        """
        Returns the heuristic value for the given state.
        Use the sum of the Manhattan distances of misplaced
        tiles to their final positions.
        """
        manhattanDist = []
        heuristic = 0

        for i in range(9): # for every position on game board
            Pos = state[i]
            if Pos != 0:
                goalIndex = self.goal_state.index(Pos) #goal position
                goal_row = goalIndex // 3  # goal row index
                goal_col = goalIndex % 3  # goal column index
                current_row = i // 3  # current row index
                current_col = i % 3  # current column index

                Dist = abs(goal_row - current_row) + abs(goal_col - current_col) # get distance to goal position
                manhattanDist.append(Dist)

        for i in manhattanDist: # add up all manhatten distances for heuristic val
            heuristic = heuristic + i

        return heuristic


'''TEST CASES
puzzle = EightPuzzle((1,0,6,8,7,5,4,2,3),(0,1,2,3,4,5,6,7,8))
print(puzzle.init_state)
print(puzzle.goal_state)

puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
print(puzzle.init_state)
print(puzzle.goal_state)

puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
print(puzzle.actions((0,1,2,3,4,5,6,7,8)))
print(puzzle.actions((6,3,5,1,8,4,2,0,7)))
print(puzzle.actions((4,8,1,6,0,2,3,5,7)))
print(puzzle.actions((1,0,6,8,7,5,4,2,3)))
print(puzzle.actions((1,2,3,4,5,6,7,8,0)))

puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
print(puzzle.result((0,1,2,3,4,5,6,7,8), 'DOWN'))
print(puzzle.result((6,3,5,1,8,4,2,0,7), 'LEFT'))
print(puzzle.result((3,4,1,7,6,0,2,8,5), 'UP'))
print(puzzle.result((1,8,4,7,2,6,3,0,5), 'RIGHT'))

puzzle=EightPuzzle((1,0,6,8,7,5,4,2,3),(0,1,2,3,4,5,6,7,8))
print(puzzle.goal_test((6,3,5,1,8,4,2,0,7)))
print(puzzle.goal_test((1,2,3,4,5,6,7,8,0)))
print(puzzle.goal_test((0,1,2,3,4,5,6,7,8)))

puzzle=EightPuzzle((1,0,3,4,2,5,7,8,6))
print(puzzle.goal_test((6,3,5,1,8,4,2,0,7)))
print(puzzle.goal_test((0,1,2,3,4,5,6,7,8)))
print(puzzle.goal_test((1,2,3,4,5,6,7,8,0)))

puzzle=EightPuzzle((1,0,3,4,2,5,7,8,6))
print(puzzle.g(0,(4,8,1,6,0,2,3,5,7), 'UP', (4,0,1,6,8,2,3,5,7)))
print(puzzle.g(3,(8,0,1,2,4,5,6,3,7,0), 'DOWN', (8,6,1,4,0,2,3,5,7)))
print(puzzle.g(8,(8,1,2,4,5,6,3,7,0), 'UP', (8,1,2,4,5,0,3,7,6)))
print(puzzle.g(11,(1,2,8,4,5,6,3,0,7), 'RIGHT', (1,2,8,4,5,6,3,7,0)))

puzzle=EightPuzzle((1,0,3,4,2,5,7,8,6))
print(puzzle.goal_state)
print(puzzle.h((1,2,3,4,5,0,7,8,6)))
print(puzzle.h((1,2,0,4,5,3,7,8,6)))
print(puzzle.h((1,0,2,4,5,3,7,8,6)))
print(puzzle.h((4,1,2,0,5,3,7,8,6)))
print(puzzle.h((4,1,2,6,8,0,3,5,7)))
'''


