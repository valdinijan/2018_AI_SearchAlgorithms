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
    List = [ UP, DOWN, LEFT, RIGHT ]

class Fringe:
    def __init__(self):
        self.dict = {}
    def push(self, item):
        pass
    def pop(self):
        pass

class Queue(Fringe):
    def __init__(self):
        super().__init__()
        self.items = []
    def push(self, item):
        self.dict[item.board.key] = True
        self.items.insert(0, item)
        print("Push: ", item.board.key, id(item))
        print("Fringe contents after push: ")
        for x in self.items:
            print(x.board)
    def pop(self):
        print("Fringe contents before pop: ")
        for x in self.items:
            print(x.board.key)
        item = self.items.pop()
        del self.dict[item.board.key]
        print("Pop: ", item.board.key)
        return item
    def isEmpty(self):
        return self.items == []

class Stack(Fringe):
    pass
    
class PrioQueue(Fringe):
    pass

class Board:
    GOAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def makeKey(state):
        key = ""
        for x in state:
            key = key + str(x)
        return key
    def __init__(self, state):
        # state: list of integers
        self.state = state
        self.key = Board.makeKey(state)
    def goalTest(self):
        if len(self.state) != 9:
            return False
        for idx in range(len(self.state)):
            if self.state[idx] != Board.GOAL_STATE[idx]:
                return False
        return True
    def move(self, dir):
        idxZ = self.state.index(0)
        if dir == Move.UP:
            if idxZ >= 3:
                idxNew = idxZ - 3
                tmp = self.state[idxNew]
                self.state[idxNew] = 0
                self.state[idxZ] = tmp
                self.key = Board.makeKey(self.state)
                return True
            else:
                return False
        elif dir == Move.DOWN:
            if idxZ <= 5:
                idxNew = idxZ + 3
                tmp = self.state[idxNew]
                self.state[idxNew] = 0
                self.state[idxZ] = tmp
                self.key = Board.makeKey(self.state)
                return True
            else:
                return False
        elif dir == Move.LEFT:
            if idxZ % 3 == 0:
                idxNew = idxZ - 1
                tmp = self.state[idxNew]
                self.state[idxNew] = 0
                self.state[idxZ] = tmp
                self.key = Board.makeKey(self.state)
                return True
            else:
                return False
        elif dir == Move.RIGHT:
            if idxZ % 3 == 2:
                idxNew = idxZ + 1
                tmp = self.state[idxNew]
                self.state[idxNew] = 0
                self.state[idxZ] = tmp
                self.key = Board.makeKey(self.state)
                return True
            else:
                return False

class Node:
    def __init__(self, board):
        self.board = board
        self.cost = 0
        self.visited = False
        self.parent = None

class State:
    def __init__(self, algType, startBoard):
        self.algType = algType
        # fringe: list of Board objects
        if algType == 'bfs':
            self.fringe = Queue()
        elif algType == 'dfs':
            self.fringe = Stack()
        elif algType == 'ast':
            self.fringe = PrioQueue()

        startNode = Node(startBoard)
        self.fringe.push(startNode)
        
        # path: list of Move objects
        self.path = []
        # visited: set of Node objects
        self.explored = {}

class Solver(State):
    class SolverOutput:
        pass

    def __init__(self, algType, startNode):
        super().__init__(algType, startNode)
    def tryAddToFringe(self, currNode, move):
        newNode = Node(currNode.board)
        if newNode.board.move(move) == True:
            if not (newNode.board.key in self.fringe.dict) and\
               not (newNode.board.key in self.explored):
                print("New node: ", newNode.board.key)
                self.fringe.push(newNode)
                # print(newNode.board.key, "added to fringe")

    def expand(self, currNode):
        if self.algType == 'bfs':
            # push children in UDLR order
            self.tryAddToFringe(currNode, Move.UP)
            self.tryAddToFringe(currNode, Move.DOWN)
            self.tryAddToFringe(currNode, Move.LEFT)
            self.tryAddToFringe(currNode, Move.RIGHT)
        elif self.algType == 'dfs':
            # push children in reverse UDLR order
            self.tryAddToFringe(currNode, Move.RIGHT)
            self.tryAddToFringe(currNode, Move.LEFT)
            self.tryAddToFringe(currNode, Move.DOWN)
            self.tryAddToFringe(currNode, Move.UP)

    def run(self):
        result = False
        cnt = 0
        
        while not self.fringe.isEmpty() and result == False and cnt < 10:
            # print("In a loop")
            cnt = cnt + 1
            print("Step: ", cnt)
            currNode = self.fringe.pop()
            currNode.visited = True
            # print(currNode.board.key, currNode.visited)
            self.explored[currNode.board.key] = currNode
            
            # print(currNode.state)
            
            # check if the goal is reached
            if currNode.board.goalTest():
                print("Success")
                result = True

            # expand and add neighbors to the fringe
            self.expand(currNode)
    
        print("Failure")

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

'''
b = Board([1, 2, 3])
print("b1: ", b.goalTest())
b = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])
print("b1: ", b.goalTest())
b = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("b2: ", b.goalTest())
b = Board([0, 1, 2, 4, 3, 5, 6, 7, 8])
print("b3: ", b.goalTest())
'''

#===============================================================================
# main
#===============================================================================

# execute algorithm
print("==================================================")
initState = Board(list(map(int, gInitState)))
solver = Solver(gAlg, initState)
slOut = solver.run()
print("==================================================")
# print("Solver output: ", slOut.pathToGoal)
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
