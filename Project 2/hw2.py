########################################################
#
# CMPSC 441: Homework 2
#
########################################################


student_name = 'Rohan Mankame'
student_email = 'rym5387@psu.edu'




########################################################
# Import
########################################################


from hw2_utils import *
from collections import deque





##########################################################
# 1. Uninformed Any-Path Search Algorithms
##########################################################


def depth_first_search(problem):
    node = Node(problem.init_state)
    frontier = deque([node])
    explored = [problem.init_state]

    #while queue
    while frontier: #Last in first out
        node = frontier.pop() #pop last element
        if (problem.goal_test(node.state)):
            return node  # goal_test passed return

        actions = problem.actions(node.state)
        for x in actions:
            childNode = node.child_node(problem,x)
            if (childNode.state not in explored): #add to explored and frontier
                explored.append(childNode.state)
                frontier.append(childNode)
    return None



    
def breadth_first_search(problem):
    node = Node(problem.init_state)
    frontier = deque([node])
    explored = [problem.init_state]

    # while queue
    while frontier: # first in first out
        node = frontier.popleft()  # pop last element
        if (problem.goal_test(node.state)):
            return node  # goal_test passed return
        actions = problem.actions(node.state)
        for x in actions:
            childNode = node.child_node(problem, x)
            if (childNode.state not in explored):  # #add to explored and frontier
                explored.append(childNode.state)
                frontier.append(childNode)
    return None




##########################################################
# 2. Coin Problem
##########################################################


class CoinPuzzle(Problem):


    def __init__(self, init_state, goal_state=0, coins=[]):
        super().__init__(init_state, goal_state)
        self.coins = coins

    
    def actions(self, state):
        ACT_COINS = []
        for x in self.coins: # array of posible coin actions
            if (x <= state):
                ACT_COINS.append(x)
        return ACT_COINS

    
    def result(self, state, action):
        result =  state - action # result after action
        return result

    
    def goal_test(self, state):
        if (state == self.goal_state): # check goal
            return True
        else:
            return False



''' Test Cases:
old_british_coins = [120, 30, 24, 12, 6, 3, 1]
puzzle = CoinPuzzle(48, 0, old_british_coins)
print(puzzle.init_state)

print(puzzle.goal_state)

print(puzzle.coins)

print(puzzle.actions(110))
print(puzzle.actions(12))

print(puzzle.result(107,30))
print(puzzle.result(77,30))

print(puzzle.goal_test(47))
print(puzzle.goal_test(0))
'''
##########################################################
# 3. N-Queens Problem
##########################################################


class NQueensProblem(Problem):
    
    def __init__(self, n):
        super().__init__(tuple([-1] * n))
        self.n = n

    def SafeMove(self, state, row, col):
        # Check for queen when same row/column or dioginal
        for xrow in range(col):
            Queen_Col = state[xrow] #column of current queen
            if ((Queen_Col==row) or (abs(Queen_Col-row)== abs(col - xrow))):
                return False # found another queen that can kill
        return True #safe

    def actions(self, state):
        col = state.index(-1)
        SafeMoves = []
        for x in range(self.n): #for all queens
            if (self.SafeMove(state, x, col)): #check if SafeMove
                SafeMoves.append((x, col)) #add move
        safe_first = [pair[0] for pair in SafeMoves] #only column
        return safe_first
    

    def result(self, state, action):
        ListState = list(state)  # Create a copy of the current state
        POS = -1  # Default if -1 is not found
        #get left most i that is -1
        for i in range(len(ListState)):
            if (ListState[i] == -1):
                POS = i
                break
        ListState[POS] = action # set to left most -1
        newState = tuple(ListState) #convert into tuple
        return newState
    
                        
    def goal_test(self, state):
        #check if safe by checking row/col and diognal queens that can kill, same as safeMove function
        for xcol in range(len(state)):
            for yrow in range(xcol+ 1, len(state)):
                if (state[ xcol]==state[yrow] or abs(state[xcol] - state[yrow])== abs(xcol- yrow)):
                    return False
        return True


        
''' Test Cases:
problem = NQueensProblem(8)
print(problem.init_state)
print(problem.n)

print(problem.actions((-1,-1,-1,-1,-1,-1,-1,-1)))
print(problem.actions((7,2,-1,-1,-1,-1,-1,-1)))
print(problem.actions((7,2,6,3,1,5,-1,-1)))

print(problem.result((-1,-1,-1,-1,-1,-1,-1,-1),7))
print(problem.result((7,2,-1,-1,-1,-1,-1,-1), 6))

print(problem.goal_test((7,3,0,2,5,1,6,4)))
print(problem.goal_test((0,4,7,5,2,6,1,3)))
print(problem.goal_test((7,2,6,3,1,4,0,5)))
print(problem.goal_test((1,4,6,3,0,2,5,7)))
'''

##########################################################
# 4. Graph Problem
##########################################################


class GraphProblem(Problem):

    def __init__(self, init_state, goal_state, graph):
        super().__init__(init_state, goal_state)
        self.graph = graph

    
    def actions(self, state):
        return list(self.graph.get(state).keys()) #from graph map

    
    def result(self, state, action):
        return action

    
    def goal_test(self, state):
        if state == self.goal_state: #goal reached
            return True
        else:
            return False

''' Test Cases:
romania_map = Graph(romania_roads,False)
planner = GraphProblem('Arad','Bucharest',romania_map)
print(planner.init_state)
print(planner.goal_state)
print(planner.graph)

print(planner.actions('Arad'))
print(planner.actions('Sibiu'))
print(planner.actions('Eforie'))

print(planner.result('Arad','Zerind'))
print(planner.result('Sibiu','Fagaras'))
print(planner.result('Eforie','Hirsova'))

print(planner.goal_test('Arad'))
print(planner.goal_test('Timisoara'))
print(planner.goal_test('Bucharest'))
'''