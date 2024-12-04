from itertools import permutations
import matplotlib.pyplot as plt
import numpy as np

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return grid

def is_xmas_pattern(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    
    # Generate all permutations of "MAS"
    mas_permutations = list(permutations("MAS"))
    
    # Check for the X-MAS pattern
    for p in mas_permutations:
        try:
            if (grid[r][c] == p[0] and grid[r][c + 2] == p[2] and
                grid[r + 1][c + 1] == p[1] and
                grid[r + 2][c] == p[0] and grid[r + 2][c + 2] == p[2]):
                return True
            if (grid[r][c + 2] == p[0] and grid[r][c] == p[2] and
                grid[r + 1][c + 1] == p[1] and
                grid[r + 2][c + 2] == p[0] and grid[r + 2][c] == p[2]):
                return True
        except IndexError:
            pass  # Ignore if we're out of grid bounds

    return False

def count_xmas_patterns(grid):
    count = 0
    patterns = set()
    for r in range(len(grid) - 2):  # Ensuring we do not go out of bounds vertically
        for c in range(len(grid[0]) - 2):  # Ensuring we do not go out of bounds horizontally
            if is_xmas_pattern(grid, r, c):
                count += 1
                patterns.add((r, c))  # Add unique pattern position to the set
    
    return count, patterns

def highlight_patterns(grid, patterns):
    fig, ax = plt.subplots()
    nrows, ncols = len(grid), len(grid[0])
    data = np.zeros((nrows, ncols, 3), dtype=float)

    for r in range(nrows):
        for c in range(ncols):
            data[r, c] = [1, 1, 1]  # Default color: white

    for (r, c) in patterns:
        data[r, c] = [0, 1, 0]  # Top left: green
        data[r, c + 2] = [0, 1, 0]  # Top right: green
        data[r + 1, c + 1] = [0, 1, 0]  # Center: green
        data[r + 2, c] = [0, 1, 0]  # Bottom left: green
        data[r + 2, c + 2] = [0, 1, 0]  # Bottom right: green

    ax.imshow(data, aspect='auto')
    
    for r in range(nrows):
        for c in range(ncols):
            ax.text(c, r, grid[r][c], va='center', ha='center', fontsize=8)

    plt.show()

def main():
    filename = 'D:/Advent-of-code-2024/Advent-of-Code-2024/Day04/input.txt'
    grid = read_grid_from_file(filename)
    
    count, patterns = count_xmas_patterns(grid)
    highlight_patterns(grid, patterns)
    print("Total instances of X-MAS:", count)

main()
