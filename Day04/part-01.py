def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return grid

def search_word(grid, word):
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
        (-1, -1)  # diagonal up-left
    ]
    
    count = 0
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if all(0 <= r + k*dr < rows and 0 <= c + k*dc < cols and grid[r + k*dr][c + k*dc] == word[k] for k in range(word_len)):
                    count += 1
    return count

def main():
    filename = 'D:/Advent-of-code-2024/Advent-of-Code-2024/Day04/input.txt'
    
    grid = read_grid_from_file(filename)
    
    word = "XMAS"
    result = search_word(grid, word)
    
    print("Total instances of XMAS:", result)

main()
