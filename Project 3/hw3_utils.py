########################################################
#
# CMPSC 441: Homework 3
#
########################################################


#
# DO NOT CHANGE ANYTHING IN THIS FILE.
# - Your submission will be tested using this file
#   in its original contents.
#


class Problem:
    def __init__ (self, init_state, goal_state=None):
        self.init_state = init_state
        self.goal_state = goal_state

        
    def actions(self, state):
        """Returns the list of actions that can be
            executed in the given state"""
        pass

    
    def result(self, state, action):
        """Returns the state that results from executing
            the given action in the given state"""
        pass
    

    def goal_test(self, state):
        """Returns True if the given state is a goal state
           and False otherwise"""
        pass
    

    def g(self, cost, from_state, action, to_state):
        """
        Returns the path cost from the root to to_state via from_state.
        The given cost is the path cost from the root to from_state 
        and the given action will lead from from_state to to_state.
        (see page 85 of the textbook, i.e., f(n) = g(n) + h(n) )   
        """
        pass
    

    def h(self, state):
        """Returns the heuristic value at this state.
           (see page 85 of the textbook, i.e., f(n) = g(n) + h(n) )"""
        pass
    
    



class Node:
    """
    Represents a node in a search tree. It contains the current state,
    the pointer to the parent node, and the action that leads to the
    current node from the parent node.
    """

    def __init__ (self, state, parent=None, action=None,
                  path_cost=0, heuristic=0):
        """Creates a search tree node that results from 
           executing the given action from the parent node."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic = heuristic
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
        next_node = Node(next_state, self, action,
                         problem.g(self.path_cost, self.state,
                                   action, next_state),
                         problem.h(next_state))
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
        return "<Node {}(g={}, h={})>".format(self.state, self.path_cost, self.heuristic)


    def __eq__(self, other):
        """
        Used for 'in' operator.
        It treats the nodes with the same state as equal
        (since breadth first graph search and A* search should
        have no duplicated states).
        This might not what you want in other context
        """
        return isinstance(other, Node) and self.state == other.state




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

                    
    def get(self, x, y=None):
        """Returns the distance from x to y, or
           the distances to cities reachable from x"""
        edges = self.edges.setdefault(x,{})
        if y is None:
            return edges
        else:
            return edges.get(y)
        

    def vertices(self):
        """Returns the list of vertices in the graph."""
        s = set([x for x in self.edges.keys()])
        t = set([y for v in self.edges.values() for (y,d) in v.items()])
        v = s.union(t)
        return list(v)

    
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

romania_city_positions = dict(
    Arad    = ( 91, 492),  Bucharest = (400, 327),  Craiova  = (253, 288),
    Drobeta = (165, 299),  Eforie    = (562, 293),  Fagaras  = (305, 449),
    Giurgiu = (375, 270),  Hirsova   = (534, 350),  Iasi     = (473, 506),
    Lugoj   = (165, 379),  Mehadia   = (168, 339),  Neamt    = (406, 537),
    Oradea  = (131, 571),  Pitesti   = (320, 368),  Rimnicu  = (233, 410),
    Sibiu   = (207, 457),  Timisoara = ( 94, 410),  Urziceni = (456, 350),
    Vaslui  = (509, 444),  Zerind    = (108, 531)
    )



#
# Example graphs with heuristicss from the Lectures
#

best_graph_edges = dict(
    S = dict(A=2, B=5),
    A = dict(C=2, D=4),
    B = dict(D=1, G=5),
    D = dict(C=3, G=2)
    )
best_graph_h = dict(S=10, A=2, B=3, C=1, D=4, G=0)


uniform_graph_edges = dict(
    S = dict(A=2, B=5),
    A = dict(C=2, D=4),
    B = dict(D=1, G=5),
    D = dict(C=3, G=2)
    )


a_star_graph_edges = dict(
    S = dict(A=1, B=2),
    A = dict(C=1),
    B = dict(C=2),
    C = dict(G=100)
    )
a_star_graph_admissible_h = dict( S=90, A=100, B=1, C=90, G=0 )
a_star_graph_consistent_h = dict( S=90, A=100, B=88, C=100, G=0 )

