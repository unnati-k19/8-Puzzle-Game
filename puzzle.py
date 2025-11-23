import random
import copy
import sys

# Constants for the game
BOARD_SIZE = 3
WIN_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
EMPTY_TILE = 0 # Represents the empty space (where 0 is used)

class EightPuzzleGame:
    def __init__(self):
        self.board = self._create_solvable_board()

    def _get_inversions(self, flat_board):
        inversions = 0
        # Filter out the empty tile
        tiles = [t for t in flat_board if t != EMPTY_TILE]
        n = len(tiles)

        for i in range(n):
            for j in range(i + 1, n):
                if tiles[i] > tiles[j]:
                    inversions += 1
        return inversions

    def _is_solvable(self, flat_board):
        return self._get_inversions(flat_board) % 2 == 0

    def _create_solvable_board(self):
        flat_list = list(range(BOARD_SIZE * BOARD_SIZE))
        while True:
            random.shuffle(flat_list)
            if self._is_solvable(flat_list):
                break
        board = [flat_list[i*BOARD_SIZE:(i+1)*BOARD_SIZE] for i in range(BOARD_SIZE)]
        return board

    def display_board(self):
        print("\n" + "="*13)
        print("  8-Puzzle Game")
        print("="*13)
        for row in self.board:
            display_row = [' ' if tile == EMPTY_TILE else str(tile) for tile in row]
            print(f"| {' | '.join(display_row)} |")
        print("="*13)

    def find_empty_tile(self):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.board[r][c] == EMPTY_TILE:
                    return r, c
        return -1, -1 

    def move_tile(self, direction):
        r, c = self.find_empty_tile()
        dr, dc = r, c
        
        if direction == 'up':
            dr -= 1
        elif direction == 'down':
            dr += 1
        elif direction == 'left':
            dc -= 1
        elif direction == 'right':
            dc += 1
        else:
            print("Invalid input. Use U, D, L, or R.")
            return False
        
        if 0 <= dr < BOARD_SIZE and 0 <= dc < BOARD_SIZE:
            self.board[r][c], self.board[dr][dc] = self.board[dr][dc], self.board[r][c]
            return True
        else:
            print("That move is not possible (Out of bounds).")
            return False

    def check_win(self):
        return self.board == WIN_STATE

def main():
    game = EightPuzzleGame()
    move_count = 0
    
    print("Welcome to the 8-Puzzle Game!")
    print("Goal: Arrange tiles 1-8 in order, with 0 (blank space) in the bottom-right.")
    print("Input: U(p), D(own), L(eft), R(ight) to move the blank space.")

    while not game.check_win():
        game.display_board()
        print(f"Moves: {move_count}")
        
        user_input = input("Enter move (U/D/L/R) or 'Q' to quit: ").strip().lower()
        if user_input == 'q':
            print("\nGame quit. Final board state:")
            game.display_board()
            sys.exit(0)
        move_map = {'u': 'up', 'd': 'down', 'l': 'left', 'r': 'right'}
        
        direction = move_map.get(user_input, None)
        
        if direction:
            if game.move_tile(direction):
                move_count += 1
        else:
            print("Invalid input. Please try again.")
    game.display_board()
    print(f"\n--- CONGRATULATIONS! ---")
    print(f"You solved the puzzle in {move_count} moves!")

if __name__ == "__main__":
    main()