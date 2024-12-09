from aoc import parse_args
from itertools import cycle
from dataclasses import dataclass
from collections import defaultdict
from copy import copy

@dataclass(frozen=True)
class Position:
    x: int
    y: int

@dataclass(frozen=True)
class Vector:
    x: int
    y: int

@dataclass
class Guard:
    position: Position
    direction: Vector

    def move(self, forward=True):
        self.position = Position(
            self.position.x + self.direction.x * (1 if forward else -1),
            self.position.y + self.direction.y * (1 if forward else -1)
        )

def simulate(map, guard, x, y, wall_position=None):
    directions = cycle(((0, -1), (1, 0), (0, 1), (-1, 0)))
    guard.direction = Vector(*next(directions))
    visited = set()
    if wall_position is not None:
        map[wall_position] = "#"

    while True:
        map[guard.position] = "X"

        # check for loops
        state = (guard.position, guard.direction)
        if state in visited:
            return True
        visited.add(state)
        
        guard.move()
        if map[guard.position] == "#":
            guard.move(False)
            guard.direction = Vector(*next(directions))
        elif not (0 <= guard.position.x <= x and 0 <= guard.position.y <= y):
            return len([ position for position, value in map.items() if value == "X"])


def main():
    fileName, part = parse_args()

    map = defaultdict(lambda: '.')
    guard = None

    with open(fileName, "r") as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                if char in ".#":
                    map[Position(x, y)] = char
                elif char == "^":
                    guard = Guard(Position(x, y), Vector(0, -1))


    part1 = simulate(copy(map), copy(guard), x, y)
    print(f"Part 1: {part1}")

    obstacles = 0
    for position, value in map.items():
        if value == ".":
            if simulate(copy(map), copy(guard), x, y, position) is True:
                obstacles += 1
    print(f"Part 2:", obstacles)

if __name__ == "__main__":
    main()