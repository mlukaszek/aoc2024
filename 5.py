from aoc import parse_args

def correct(update, rules):
    for i, value in enumerate(update):
        for rule in rules:
            before, after = rule
            if (i > 0) and any([before == value and update[index] == after for index in range(i)]):
                return False
            lastIndex = len(update) - 1
            if (i < lastIndex) and any([after == value and update[index] == before for index in range(i, lastIndex+1)]):
                return False
    return True

def reorder(update, rules):
    ordered = []
    for value in update:
        ordered.insert(0, value)

        before  = [ before for (before, after) in rules if after == value ]
        after = [ after for (before, after) in rules if before == value ]
        
        while not (
            all([ordered.index(x) < ordered.index(value) for x in before if x in ordered]) and \
            all([ordered.index(x) > ordered.index(value) for x in after if x in ordered])):
            currentIndex = ordered.index(value)
            ordered[currentIndex], ordered[currentIndex + 1] = ordered[currentIndex + 1], ordered[currentIndex]
    return ordered

def main():
    fileName, part = parse_args()

    rules = []
    updates = []
    with open(fileName) as f:
        for line in f:
            if "|" in line:
                rules.append([int(value) for value in line.split("|")])
            elif "," in line:
                updates.append([int(value) for value in line.split(",")])

    part1 = 0
    part2 = 0
    for update in updates:
        if correct(update, rules):
            part1 += update[len(update) // 2]
        else:
            ordered = reorder(update, rules)
            part2 += ordered[len(ordered) // 2]

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()