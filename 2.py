from aoc import parse_args

def all_safe(levels = []):
    return all(levels[i] < levels[i + 1] and 1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1)) \
        or all(levels[i] > levels[i + 1] and 1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

def main():
    fileName, part = parse_args()

    lines = []
    with open(fileName, "r") as f:
        lines = f.readlines()

    safe = 0
    for line in lines:
        levels = [ int(value) for value in line.split() ]
        
        is_safe = all_safe(levels)

        if part == 2 and not is_safe:
            for i in range(len(levels)):
                if all_safe(levels[:i] + levels[i+1:]):
                    is_safe = True
                    break

        if is_safe:
            safe += 1
    
    print(f"Part {part}: {safe}")

if __name__ == '__main__':
    main()