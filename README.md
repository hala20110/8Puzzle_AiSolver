#  8-Puzzle AI Solver

An intelligent agent that solves the **8-puzzle game** using both **informed** and **uninformed** search algorithms. Built as part of the ColumbiaX AI course (CSMM.101x).

##  Problem Description

The 8-puzzle consists of a 3x3 grid with 8 numbered tiles and one empty space (represented as `0`). The goal is to arrange the tiles in ascending order from left to right, top to bottom:

**Legal moves:** Swap the empty space with an adjacent tile (Up, Down, Left, Right)

**Cost per move:** 1 (uniform)

---

##  Algorithms Implemented

| Algorithm | Type | Complete? | Optimal? |
|-----------|------|-----------|----------|
| **BFS** | Uninformed (Breadth-First) | ✅ | ✅ |
| **DFS** | Uninformed (Depth-First) | ❌ | ❌ |
| **IDDFS** | Uninformed (Iterative Deepening) | ✅ | ✅ |
| **A*** | Informed (with heuristics) | ✅ | ✅ |

### Heuristics for A*
- **Manhattan Distance** |dx| + |dy|
- **Euclidean Distance** √(dx² + dy²)

---

##  Features

-  Random solvable puzzle generator
-  Solvability checker (inversion count)
-  GUI visualization with step-by-step animation
-  Performance metrics tracking:
  - Path to goal
  - Cost of path
  - Nodes expanded
  - Search depth
  - Running time
  - Max frontier size

---

##  Tech Stack

- **Language:** Python 3.x
- **Libraries:** 
  - `tkinter` - GUI visualization
  - `heapq` - Priority queue for A*
  - `itertools` - Counter tie-breaking
  - `time` - Performance measurement
  - `random` - Puzzle generation
  - `math` - Euclidean heuristic
  - `termcolor` - Colored terminal output
