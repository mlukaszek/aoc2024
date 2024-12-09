from aoc import parse_args

def find_xmas(grid, x, y):
    count = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx == 0 and dy == 0) or \
                (x + 3*dx, y + 3*dy) not in grid:
                continue

            if grid[(x + dx, y + dy)] == "M" and \
               grid[(x + 2*dx, y + 2*dy)] == "A" and \
               grid[(x + 3*dx, y + 3*dy)] == "S":
                count += 1
                continue
    return count

def find_mas(grid, x, y):
    offsets = ((-1,-1), (-1,1), (1,-1), (1,1))
    for (dx, dy) in offsets:
        if (x + dx, y + dy) not in grid:
            return 0
    
    first = (grid[(x-1, y-1)] == "M" and \
            grid[(x+1, y+1)] == "S") or \
            (grid[(x-1, y-1)] == "S" and \
            grid[(x+1, y+1)] == "M")
    
    second = (grid[(x-1, y+1)] == "M" and \
            grid[(x+1, y-1)] == "S") or \
            (grid[(x-1, y+1)] == "S" and \
            grid[(x+1, y-1)] == "M")
    
    return 1 if first and second else 0

def main():
    fileName, part = parse_args()

    grid = {}

    with open(fileName, "r") as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                if char in "XMAS":
                    grid[(x, y)] = char

    total = 0
    for x, y in grid:
        if part == 1 and grid[(x, y)] == "X":
            total += find_xmas(grid, x, y)
        elif part == 2 and grid[(x, y)] == "A":
            total += find_mas(grid, x, y)

    print(f"Part {part}: {total}")

if __name__ == "__main__":
    main()