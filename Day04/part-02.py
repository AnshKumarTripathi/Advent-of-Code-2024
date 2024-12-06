from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass

INPUTFILE = "D:/Advent-of-code-2024/Advent-of-Code-2024/Day04/input.txt"

DIRS = {
    "NE": (-1, 1),
    "SE": (1, 1),
    "SW": (1, -1),
    "NW": (-1, -1),
}

@dataclass(order=True, frozen=True)
class Pos():
    row: int
    col: int

    def neighbor(self, dir: str) -> "Pos":
        dr, dc = DIRS[dir]
        return Pos(self.row + dr, self.col + dc)


@dataclass
class Grid:
    grid: dict[Pos, str]

    def __post_init__(self):
        self.nrow = max([pos.row for pos in self.grid.keys()]) + 1
        self.ncol = max([pos.col for pos in self.grid.keys()]) + 1

    def positions(self):
        for row in range(self.nrow):
            for col in range(self.ncol):
                yield Pos(row, col)

    def matches_cross_mas(self, start: Pos) -> bool:
        if self.grid[start] != "A":
            return False

        r0, c0 = start.row, start.col

        dir1 = "NE"
        dr1, dc1 = DIRS[dir1]
        pos1, pos2 = Pos(r0+dr1,c0+dc1), Pos(r0-dr1,c0-dc1)
        if ((self.grid[pos1] == "M" and self.grid[pos2] == "S") or
            (self.grid[pos2] == "M" and self.grid[pos1] == "S")):

            dir2 = "SE"
            dr2, dc2 = DIRS[dir2]
            pos3, pos4 = Pos(r0+dr2,c0+dc2), Pos(r0-dr2,c0-dc2)
            if ((self.grid[pos3] == "M" and self.grid[pos4] == "S") or
                (self.grid[pos4] == "M" and self.grid[pos3] == "S")):

                return True

        return False

    def count_cross_words(self) -> int:
        result = 0
        for pos in self.positions():
            if self.matches_cross_mas(pos):
                result += 1
        return result


def parse_input(lines):
    grid = defaultdict(lambda: ' ')
    for row, line in enumerate(lines):
        for col, ch in enumerate(line.strip()):
            grid[Pos(row, col)] = ch
    return Grid(grid)


def read_word_search_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


def solve2(lines):
    grid = parse_input(lines)
    return grid.count_cross_words()


# Main Execution
if __name__ == "__main__":
    word_search = read_word_search_from_file(INPUTFILE)
    result = solve2(word_search)
    print(f'The number of X-MAS patterns is: {result}')
