import time
from collections import deque
import random
import tkinter as tk

## visualization
def get_solution_states(node):
    states = []
    while node: # Traverse from goal node back to start
        states.append(node.state)
        node = node.parent
    
    states.reverse() # Reverse to get order from start to goal
    return states

def visualize_solution(states):
    root = tk.Tk()  # create main window
    root.title("8 Puzzle Solver")
    size = 100 # each tile 100*100 pixels
    canvas = tk.Canvas(root, width=3*size, height=3*size) #300*300 canvas
    canvas.pack() # add canvas to window
    
    def draw_state(state):
        canvas.delete("all")
        for i in range(9):
            row = i // 3 # get row
            col = i % 3 # get col
            # calc pixel coordinations
            x1 = col * size # left edge
            y1 = row * size # top 
            x2 = x1 + size #right
            y2 = y1 + size #bottom
            
            value = state[i]  # get num at this position
            
            if value == 0:
                canvas.create_rectangle(x1,y1,x2,y2, fill="wheat1", outline="wheat1")
            else:
                canvas.create_rectangle(x1,y1,x2,y2, fill="maroon", outline="wheat1")
                canvas.create_text(
                    (x1+x2)/2, # center the text
                    (y1+y2)/2,
                    text=str(value),
                    font=("Arial",24,"bold"),
                    fill="white"
                )
    
    step = 0 # to track step 

    def animate():
        nonlocal step  # use the step variable from outer scope
        
        if step < len(states):
            draw_state(states[step])
            step += 1
            root.after(700, animate) 
    
    animate()
    root.mainloop()

# check if the random puzzle is solvable (number of inversions must be even to be solvable)
def is_solvable(state):
    inversions = 0
    state_list = list(state)
    #count inversions
    for i in range(len(state_list)):
        for j in range(i+1, len(state_list)):
            if state_list[i] != 0 and state_list[j] != 0 and state_list[i] > state_list[j]:
                inversions += 1
    
    return inversions % 2 == 0

# Random puzzle Generator
def generate_random_puzzle():
    state = list(range(9))
    while True:
        random.shuffle(state) 
        # Check if solvable and not already goal state
        if is_solvable(state) and tuple(state) != GOAL_STATE:
            return tuple(state)


#the final configuration of the 8-puzzle we want to reach(0 is the blank tile)
GOAL_STATE = (0,1,2,3,4,5,6,7,8)

# node Class
class Node:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state   #current puzzle configuration (tuple for immutability)
        self.parent = parent   #previous Node (to reconstruct the path)
        self.move = move   #the move that led to this state (Up, Down, Left, Right)
        self.depth = depth   #depth of this node in the tree
        self.cost = cost   #cost so far


# print Puzzle (visualization)
def print_puzzle(state):
    for i in range(0,9,3):
        print(state[i], state[i+1], state[i+2])
    print()


# goal Test
def goal_test(state):
    return state == GOAL_STATE


# find Blank tile Position
def find_blank(state):
    return state.index(0)


# swap tiles
def swap(state, i, j):
    new_state = list(state)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return tuple(new_state)


# generate Neighbor States
def get_neighbors(state):
    
    neighbors = []
    blank = find_blank(state)
    
    row = blank // 3
    col = blank % 3
    
    # move Up
    if row > 0:
        new_state = swap(state, blank, blank-3)
        neighbors.append(("Up", new_state))
    
    # move Down
    if row < 2:
        new_state = swap(state, blank, blank+3)
        neighbors.append(("Down", new_state))
    
    # move Left
    if col > 0:
        new_state = swap(state, blank, blank-1)
        neighbors.append(("Left", new_state))
    
    # move Right
    if col < 2:
        new_state = swap(state, blank, blank+1)
        neighbors.append(("Right", new_state))
    
    return neighbors


# reconstruct Path
def reconstruct_path(node):
    
    path = []
    
    while node.parent is not None:
        path.append(node.move)
        node = node.parent
    
    path.reverse()
    return path


# print Solution Path
def print_solution(node):
    
    states = []
    
    while node:
        states.append(node.state)
        node = node.parent
    
    states.reverse()
    
    for s in states:
        print_puzzle(s)


# BFS
def bfs(initial_state):
    
    #to calculate running time
    start_time = time.time()
    root = Node(initial_state)
    frontier = deque([root])
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        
        node = frontier.popleft()
        
        if node.state in explored:
            continue
        
        explored.add(node.state)
        
        if goal_test(node.state):
            
            end_time = time.time()
            path = reconstruct_path(node)
            
            print("Success!\n")
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
        
        for move, state in get_neighbors(node.state):
            
            if state not in explored:
                
                child = Node(
                    state = state,
                    parent = node,
                    move = move,
                    depth = node.depth + 1,
                    cost = node.cost + 1
                )
                frontier.append(child)
    
    print("Failure")