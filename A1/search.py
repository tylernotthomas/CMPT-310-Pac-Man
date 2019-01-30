# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
num_hours_i_spent_on_this_assignment = 50
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
This was pretty time consuming. IDK if I'm super dumb, but the time investment for me
was pretty high given I had to meet with the TA several times and work late into the night (to accomidate other classes).
I'm scared that if the following assignments continue at this level, that my other commitments will
prevent me from scoring well :(. However, the topic and theme were fun and, given the difficulty, it felt rewarding to
finish.

"""
#####################################################
#####################################################



"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Question 1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    print (problem.isGoalState(problem.getStartState()) )
    print ( problem.getSuccessors(problem.getStartState()) )

    """
    "*** YOUR CODE HERE ***"

    #import stack data structure
    from util import Stack
    
    #test predefined functions
    print("Hi, Tyler here!")
    print ( problem.getStartState() )
    print (problem.isGoalState(problem.getStartState()) )
    print ( problem.getSuccessors(problem.getStartState()) )
    
    #initialize candidates stack with first set of successors
    candidates = Stack()
    initialCandidates = problem.getSuccessors(problem.getStartState())
    for x in initialCandidates:
        candidates.push(x)

    #initialize searched nodes list to empty list
    searched = []
    searched.append(problem.getStartState())

    while True:
        if candidates.isEmpty():
            #if candidates is empty return failure (empty set)
            print("candidates is empty")
            return []
        else:
            #else pop one node off the candidates stack
            print("candidates is NOT empty")
            node = candidates.pop()
        
        if node[0] in searched:
            #if successor node has been searched, try another node
            continue
        
        #print the value of new node to operate on
        print("node value:")
        print(node)
        print(node[0])
        
        #add node to searched list
        searched.append(node[0])
        print("searched: ")
        print(searched)
        
        #check if node is the goal
        if problem.isGoalState(node[0]):
            print("goal state achieved!")
            path = node[1].split(", ")
            return path
            return path
            break
        else:
            #if not the goal node push its successors onto the candidates stack
            toAdd = problem.getSuccessors(node[0])
            for x in toAdd:
                print("x:")
                print(x)
                print(list(x))
                listNode = list(node)
                listX = list(x)
                listX[1] = listNode[1] + ", " + listX[1]
                x = tuple(listX)
                print("after:")
                print(listX)
                #x[1].extend(node[1])
                candidates.push(x)

    print("end reached!!!")


def breadthFirstSearch(problem):
    """Question 1.2
     Search the shallowest nodes in the search tree first.
     """
    #import stack data structure
    from util import PriorityQueue
    
    #test predefined functions
    print("Hi, Tyler here!")
    print ( problem.getStartState() )
    print (problem.isGoalState(problem.getStartState()) )
    print ( problem.getSuccessors(problem.getStartState()) )
    
    #initialize candidates stack with first set of successors
    candidates = PriorityQueue()
    intialCandidates = problem.getSuccessors(problem.getStartState())
    for x in intialCandidates:
        candidates.push(x, 1)
    
    #initialize searched nodes list to empty list
    searched = []

    while True:
        if candidates.isEmpty():
            #if candidates is empty return failure (empty set)
            print("candidates is empty")
            return []
        else:
            #else pop one node off the candidates stack
            print("candidates is NOT empty")
            node = candidates.pop()
        
        if node[0] in searched:
            #if successor node has been searched, try another node
            continue
        
        #print the value of new node to operate on
        print("node value:")
        #print(node)
        #print(node[0])
        
        #add node to searched list
        searched.append(node[0])
        print("searched: ")
        #print(searched)
        
        #check if node is the goal
        if problem.isGoalState(node[0]):
            print("goal state achieved!")
            #print(node)
            path = node[1].split(", ")
            return path
            break
        else:
            #if not the goal node push its successors onto the candidates stack
            toAdd = problem.getSuccessors(node[0])
            for x in toAdd:
                listNode = list(node)
                listX = list(x)
                listX[1] = listNode[1] + ", " + listX[1]
                x = tuple(listX)
                #note that this is a PriorityQueue push() meaning that it requires a priority to be specified
                #assigning all nodes the same priority ensures that the queue becomes a FIFO queue
                candidates.push(x, 1)

    print("end reached!!!")



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Question 1.3
    Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    #import stack data structure
    from util import PriorityQueue
    
    #test predefined functions
    print("Hi, Tyler here!")
    print ( problem.getStartState() )
    print (problem.isGoalState(problem.getStartState()) )
    print ( problem.getSuccessors(problem.getStartState()) )
    
    #initialize candidates stack with first set of successors
    candidates = PriorityQueue()
    intialCandidates = problem.getSuccessors(problem.getStartState())
    for x in intialCandidates:
        priority = x[2] + heuristic(x[0], problem)
        candidates.push(x, priority)

    #initialize searched nodes list to empty list
    searched = []

    while True:
        if candidates.isEmpty():
            #if candidates is empty return failure (empty set)
            print("candidates is empty")
            return []
        else:
            #else pop one node off the candidates stack
            print("candidates is NOT empty")
            node = candidates.pop()
            
        if node[0] in searched:
                #if successor node has been searched, try another node
                continue

        #print the value of new node to operate on
        print("node value:")
        #print(node)
        #print(node[0])
        
        #add node to searched list
        searched.append(node[0])
        print("searched: ")
        print(searched)
        
        #check if node is the goal
        if problem.isGoalState(node[0]):
            print("goal state achieved!")
            #print(node)
            path = node[1].split(", ")
            return path
            break
        else:
            #if not the goal node push its successors onto the candidates stack
            toAdd = problem.getSuccessors(node[0])
            for x in toAdd:
                listNode = list(node)
                print(list(x))
                listX = list(x)
                #add cost of to travel to parent to child
                listX[2] = listX[2] + listNode[2]
                #append directions of travel to parent to child
                listX[1] = listNode[1] + ", " + listX[1]
                x = tuple(listX)
                print("after")
                print(listX)
                
                #note that this is a PriorityQueue push() meaning that it requires a priority to be specified
                #assigning nodes with priority based on the sum of their cost to reach and heuristic est. cost to goal node
                priority = x[2] + heuristic(x[0], problem)
                candidates.push(x, priority)

    print("end reached!!!")



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
