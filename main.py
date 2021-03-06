from constants import SearchMethods
from board import Board
from inputParser import generateConfigDetails, generateMatrixAndPositions
import dfs

def generateAndRunGame(configFile, matrixFile):

    algorithm = generateConfigDetails(configFile)

    try:
        algorithm = SearchMethods[algorithm]
    except:
        print("Invalid algorithm in the configuration file: ", algorithm)

    matrix, boxes, targets, player = generateMatrixAndPositions(matrixFile)

    board = Board(matrix, boxes, targets, player)
   
    if algorithm == SearchMethods.BFS:
        print("============================")
        print("\n[Starting BFS Algorithm]\n")
        print("============================\n")

        # call BFS
        
        print("\n============================")
        print("\n[Finished BFS Algorithm]\n")
        print("============================")

    elif algorithm == SearchMethods.DFS:
        print("============================")
        print("\n[Starting DFS Algorithm]\n")
        print("============================\n")

        print("Initial Board")

        board.printBoard()

        dfs.solveDFS(board)

        print("\n============================")
        print("\n[Finished DFS Algorithm]\n")
        print("============================")

    elif algorithm == SearchMethods.IDDFS:
        print("============================")
        print("\n[Starting IDDFS Algorithm]\n")
        print("============================\n")

        # call
        
        print("\n============================")
        print("\n[Finished IDDFS Algorithm]\n")
        print("============================")

    elif algorithm == SearchMethods.GREEDY:
        print("============================")
        print("\n[Starting GREEDY Algorithm]\n")
        print("============================\n")

        # call
        
        print("\n============================")
        print("\n[Finished GREEDY Algorithm]\n")
        print("============================")


generateAndRunGame("input/configuration.txt", "examples/boards.txt")