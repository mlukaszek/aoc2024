from aoc import parse_args
from collections import defaultdict
from itertools import combinations


def main():
    fileName, part = parse_args()

    map = defaultdict(list)
    with open(fileName, "r") as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                if char != ".":
                    map[char].append((x,y))

    antinodes = set()

    for char, positions in map.items():
        for a, b in combinations(positions, 2):
            x1, y1 = a
            x2, y2 = b

            dx = x2 - x1
            dy = y2 - y1

            n = 1
            while True:
                added = False
                if (0 <= (x2 + n*dx) <= x) and (0 <= (y2 + n*dy) <= y):
                    antinodes.add((x2 + n*dx, y2 + n*dy))
                    added = True
                if (0 <= (x1 - n*dx) <= x) and (0 <= (y1 - n*dy) <= y):
                    antinodes.add((x1 - n*dx, y1 - n*dy))
                    added = True
                if part == 1 or not added:
                    break
                n += 1

    if part == 2:
        for a, b in sum(map.values(), []):
            antinodes.add((a, b))

    print(f"Part {part}: {len(antinodes)}")


if __name__ == "__main__":
    main()