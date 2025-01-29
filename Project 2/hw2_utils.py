########################################################
#
# CMPSC 441: Homework 2
#
########################################################


#
# DO NOT CHANGE ANYTHING IN THIS FILE.
# - Your submission will be tested using this file
#   in its original content.
#


class Problem:
    """ Represents the problem specific operations. To solve an actual
        problem, you should subclass this and implement the methods"""
    
    def __init__ (self, init_state, goal_state=None):
        self.init_state = init_state
        self.goal_state = goal_state

    def actions(self, state):
        """Returns the list of legal actions that
           can be executed in the given state"""
        pass

    def result(self, state, action):
        """Returns the state that results from executing
           the given action in the given state"""
        pass

    def goal_test(self, state):
        """Returns True if the given state is a goal state
           and False otherwise"""
        pass
    

    

class Node:
    """Represents a node in a search tree. It contains the current state,
       the pointer to the parent node, and the action that leads to the
       current node from the parent node ."""

    def __init__ (self, state, parent=None, action=None):
        """Creates a search tree node that results from 
           executing the given action from the parent node."""
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        """Returns the list of child nodes, i.e., the list
           of nodes reachable from this node in one step."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Returns the node that results from executing 
           the given action in this node."""
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action)
        return next_node
    
    def solution(self):
        """Returns the sequence of actions that
           leads to this node from the root node."""
        if self.state == None:
            return None
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Returns a list of nodes from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __repr__(self):
        return "<Node {}>".format(self.state)


    


class Graph:
    """
    A graph connects vertices by edges. Each edge can have a length
    associated with it. The edges are represented as a dictionary
    of the following form:
       edges = { 'A' : {'B':1, 'C':2}, 'B' : {'C':2, 'D':2} }

    Creating an instance of Graph as 
         g = Graph(edges)
    instantiates a directed graph with 4 vertices A, B, C, and D with
    the edgew of length 1 from A to B, length 2 from A to C, length 2
    from B to C, and length 2 from B to D.

    Creating an instance of Graph as
         g = Graph(edges, False)
    instantiates an undirected graph by adding the inverse edges, so
    that the edges becomes:
        { 'A' : {'B':1, 'C':2},
          'B' : {'A':1, 'C':2, 'D':2},
          'C' : {'A':2, 'B':2},
          'D' : {'B':2} }
    """
    
    def __init__(self, edges=None, directed=True):
        self.edges = edges or {}
        self.directed = directed
        if not directed:
            for x in list(self.edges.keys()):
                for (y, dist) in self.edges[x].items():
                    self.edges.setdefault(y,{})[x] = dist
    
    def get(self, x):
        """Returns the dictionary of 
           cities and distances reachable from x"""
        edges = self.edges.setdefault(x,{})
        return edges
        
    def __repr__(self):
        return "<Graph {}>".format(self.edges)

    
#    
# Example graph from the textbook
# - romania map
# 

romania_roads = dict(
    Arad      = dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest = dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova   = dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta   = dict(Mehadia=75),
    Eforie    = dict(Hirsova=86),
    Fagaras   = dict(Sibiu=99),
    Hirsova   = dict(Urziceni=98),
    Iasi      = dict(Vaslui=92, Neamt=87),
    Lugoj     = dict(Timisoara=111, Mehadia=70),
    Oradea    = dict(Zerind=71, Sibiu=151),
    Pitesti   = dict(Rimnicu=97),
    Rimnicu   = dict(Sibiu=80),
    Urziceni  = dict(Vaslui=142)
    )
