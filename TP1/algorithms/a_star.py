from node import Node
from board import Board
import numpy as np
import constants
from collections import deque
import helpers
import heapq

def solve(board, heuristic):
    # Map of visited nodes
    visited = {}
    
    # Create the root
    root = Node(None, board.getPlayerPosition(), board.getBoxesPositions())
    visited[root] = True

    # Priority queue in the form of a heap
    # being f = h + g
    # Elements are (f, h, node id, Node) to provide uniqueness
    heap = [(0, 0, root.id, root)]
    heapq.heapify(heap) 

    foundSolution = False
    expandedNodes = 0

    # Iterates while not empty
    while heap:
        # Poping the first element, keeping the 
        curr = heapq.heappop(heap)
        g = curr[0] - curr[1]
        curr = curr[3]

        # Check if goal, if goal exit loop
        if board.isComplete(curr):
            foundSolution = True
            break
        else:
            expandedNodes += 1

            # Distance is increased by one
            g += 1

            # Try to move the player to all 4 positions
            # if possible, create the node and push it to queue
            for direction in constants.ALL_DIRECTIONS:
                # Test the movement direction
                newPlayerPosition, newBoxesPosition, isPossible = board.testMovement(
                    np.copy(curr.playerPos), np.copy(curr.boxesPos), direction
                )

                # Create a new node and push it if possible
                if isPossible:
                    newNode = Node(curr, newPlayerPosition, newBoxesPosition)
                    if not newNode in visited:
                        # Calculate heuristic and store it
                        newNode.setHeuristic(heuristic.calculate(newNode, board))
                        # Push item to heap
                        heapq.heappush(heap, ( g + newNode.heuristic, newNode.heuristic, newNode.id, newNode))
                        # Add to visited list
                        visited[newNode] = True

    if foundSolution:
        print("SOLUTION FOUND")
    else:
        print("SOLUTION NOT FOUND")

    helpers.printStats(expandedNodes, heap)

    if foundSolution:
        helpers.printMovesToSolution(board, curr)
        helpers.printBoardsToSolution(board, curr)
