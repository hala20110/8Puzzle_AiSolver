import heapq
import math
from BFS import*
import itertools
import time


# 1- Manhattan Distance Heuristic
def manhattan(state):
    dist=0
    for i in range(9):
        value = state[i] #tile num at this position
        if value != 0:
            # where the tile should be
            goal_row = value // 3 
            goal_col = value % 3
            # where tile is at
            row = i // 3
            col = i % 3
            dist += abs(row - goal_row) + abs(col - goal_col)

    return dist

# 2- Euclidean Distance Heurisitc
def euclidean(state):
    dist= 0
    for i in range(9):
        value = state[i]
        if value != 0:
            goal_row = value // 3
            goal_col = value % 3
            row = i // 3
            col = i % 3
            dist += math.sqrt((row - goal_row)**2 + (col - goal_col)**2)

    return dist

# 3- A* Function
def astar(initial_state, heuristic):
    counter = itertools.count() # unique counter for tie breaking
    start_time = time.time() #track runtime
    root = Node(initial_state)
    frontier = []
    heapq.heappush(frontier, (0, next(counter), root))
    explored = set()
    nodes_expanded = 0

    while frontier:
        _, _, node = heapq.heappop(frontier) #pop smallest f-cost node
        if node.state in explored: #skip if already explored
            continue

        explored.add(node.state)

        if goal_test(node.state):

            end_time = time.time()

            path = reconstruct_path(node)

            print("Success :)\n")
            # metrics
            print("Path:", path)
            print("Cost:", len(path))
            print("Nodes Expanded:", nodes_expanded)
            print("Search Depth:", node.depth)
            print(f"Running Time:{end_time - start_time:.6f} seconds\n")

            print("Solution Steps:\n")
            print_solution(node)
            states = get_solution_states(node)
            visualize_solution(states)

            return

        nodes_expanded += 1 
        # generate all possible moves from current state
        for move, state in get_neighbors(node.state):
            
            if state not in explored:

                g = node.cost + 1
                h = heuristic(state)
                f = g + h # total estimated cost
                # create child node
                child = Node(
                    state=state,
                    parent=node,
                    move=move,
                    depth=node.depth + 1,
                    cost=g
                )

                heapq.heappush(frontier, (f, next(counter), child))

    print("Failure")