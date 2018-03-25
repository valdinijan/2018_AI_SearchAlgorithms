#!/usr/bin/env python3
import sys;

# get command line arguments
gAlg = sys.argv[1];
gInitState = sys.argv[2:];
print("Alg: ", gAlg);
print("InitState: ", gInitState);

#===============================================================================
# Classes
#===============================================================================

class Move:
    UP = 'Up'
    DOWN = 'Down'
    LEFT = 'Left'
    RIGHT = 'Right'

class Fringe:
    def __init__(self):
        pass
    def add(self, item):
        pass
    def remove(self):
        pass

class Queue(Fringe):
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.insert(0,item)
    def remove(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []

class Board:
    GOAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def __init__(self, state):
        # state: list of integers
        self.state = state
    def goalTest(state):
        if len(state) != 9:
            return False
        for idx in state:
            if state[idx] != Board.GOAL_STATE[idx]:
                return False
        return True

class Node:
    def __init__(self, board):
        self.board = board
        self.cost = 0
        self.visited = False
        self.parent = None

class State:
    def __init__(self):
        # fringe: list of Board objects
        self.fringe = Fringe()
        # path: list of Move objects
        self.path = []
        # visited: set of Node objects
        self.explored = {}

class Solver:
    class SolverOutput:
        pass

    def __init__(self, algType, start):
        self.algType = algType
        self.start = start
    
    def run(self):
        slOut = Solver.SolverOutput()
        slOut.pathToGoal = [ 'Bag', 'Wuss' ]
        slOut.costOfGoal = 0
        slOut.nodesExpanded = 0
        slOut.searchDepth = 3
        slOut.maxSearchDepth = 4321
        slOut.runningTime = 12.34;
        slOut.maxRamUsage = 3
        return slOut
        
class PrepareFileParams:
    pass

#===============================================================================
# Functions
#===============================================================================
def DfsSearch(initState):
    print("DFS search")

def BfsSearch(initState):
    print("BFS search")

def AstSearch(initState):
    print("AST search")

def PrepareFile(params):
    fileStr = ""
    fileStr = fileStr + "path_to_goal: " + str(params.pathToGoal) + "\n"
    fileStr = fileStr + "cost_of_path: " + str(params.costOfGoal) + "\n"
    fileStr = fileStr + "nodes_expanded: " + str(params.nodesExpanded) + "\n"
    fileStr = fileStr + "search_depth: " + str(params.searchDepth) + "\n"
    fileStr = fileStr + "max_search_depth: " + str(params.maxSearchDepth) + "\n"
    fileStr = fileStr + "running_time: " +\
              '{0:.8f}'.format(params.runningTime) + "\n"
    fileStr = fileStr + "max_ram_usage: " + str(params.maxRamUsage) + "\n"
    return fileStr

#===============================================================================
# Experimental
#===============================================================================

    
#===============================================================================
# main
#===============================================================================

# execute algorithm
solver = Solver(gAlg, gInitState)
slOut = solver.run()
print("Solver output: ", slOut.pathToGoal)
fileStr = PrepareFile(slOut)

# algSel = { "bfs" : BfsSearch,
           # "dfs" : DfsSearch,
           # "ast" : AstSearch }
# algSel[gAlg](gInitState)

# prepare file
# params = PrepareFileParams()
# params.pathToGoal = [ 'Up', 'Down' ]
# params.costOfGoal = 34
# params.runningTime = 1.234
# fileStr = PrepareFile(params)

# write to file
f = open("output.txt", 'w')
f.write(fileStr)
f.close()
