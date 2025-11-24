# 8-Puzzle-Game
This is a Python command-line version of the traditional 8-Puzzle game, also called the 3x3 Sliding Tile Puzzle. 

The objective of the game is to arrange the eight numbered tiles in a 3 × 3 grid into a target configuration by sliding the 
tiles into the empty space.

~ FEATURES ~

Solvable Boards Only : By counting the number of inversions, the game ensures that each initial board generated is solvable.

Command Line Interface: A straightforward text-based gaming interface.

Move Counter: Counts how many moves are needed to complete the puzzle.

~ HOW TO PLAY ~

Your system must have Python 3.x installed.

~ RUNNING THE GAME ~

* Save the code : The supplied Python code should be saved as a file, such as eight_puzzle.py.

* Run from the terminal: Locate the directory in which you saved the file, open your terminal or command prompt, and execute.
                                                                                      
      python eight_puzzle.py

~ INSTRUCTIONS FOR GAME ~

A randomly generated, solvable board will be shown at the beginning of the game.

The intended state is:

    | 1 | 2 | 3 |
 
    | 4 | 5 | 6 |
 
    | 7 | 8 | _ |

The bottom-right corner should contain the empty space, denoted by 0 in the code.

* Input Commands: Type your move's single letter.

 U: In the empty space, move the tile up (i.e., move the empty space down).

 D: Move the empty space up by moving the tile down into it.

 L: Move the empty space to the right, or move the tile to the left.

 R: Move the empty space to the left (i.e., move the tile to the right).

 Q: Stop playing the game.

When the board matches the WIN_STATE, the game is over.

~ VERIFICATION OF SOLVABILITY ~

The Inversion RuleMaking sure the puzzles are solvable is a critical component of this project.
 
Only when the configuration of the 8-Puzzle has an even number of inversions can it be solved.
 
* Inversion: An inversion happens when a tile A comes before a tile B in the board's one-dimensional sequence (reading row-by-
 row),but value of A > value of B . In this count, the empty tile (0) is ignored in this count.

~ IMPROVEMENTS AND FUTURE WORK ~

Use A* search or another intelligent search algorithm to solve the puzzle automatically.

Replace the command-line interface with a graphical user interface (GUI) using libraries like Tkinter or Pygame.

Track and show the best solution path; and support larger tile puzzles (such as the $4 \times 4$ grid or the 15-Puzzle).

If you discover any bugs or have ideas for enhancements, please feel free to open issues, submit pull requests, or fork this repository!
