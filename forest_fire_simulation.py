import random
import time

class ForestFire:
    def __init__(self, size, tree_density):
        self.size = size
        self.tree_density = tree_density
        self.grid = self.initialize_forest()

    def initialize_forest(self):
        # Initialize the forest grid with trees (T) and empty spaces (.)
        grid = []
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                if random.random() < self.tree_density:
                    row.append('T')  # T for tree
                else:
                    row.append('.')  # . for empty space
            grid.append(row)

        # Set a random tree on fire
        self.start_fire(grid)
        return grid

    def start_fire(self, grid):
        # Set a random tree on fire ('F' represents a burning tree)
        while True:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if grid[row][col] == 'T':
                grid[row][col] = 'F'
                break

    def print_forest(self):
        for row in self.grid:
            print(" ".join(row))
        print("\n" + "-" * (self.size * 2))

    def spread_fire(self):
        new_grid = [row.copy() for row in self.grid]
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 'F':  # Spread fire to neighboring trees
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.size and 0 <= nc < self.size and self.grid[nr][nc] == 'T':
                            new_grid[nr][nc] = 'F'
                    new_grid[r][c] = '.'  # Burned out tree
        self.grid = new_grid

    def run_simulation(self):
        while any('F' in row for row in self.grid):
            self.print_forest()
            self.spread_fire()
            time.sleep(1)

if __name__ == "__main__":
    size = int(input("Enter the size of the forest grid: "))
    tree_density = float(input("Enter tree density (0-1): "))

    forest_fire = ForestFire(size, tree_density)
    forest_fire.run_simulation()
