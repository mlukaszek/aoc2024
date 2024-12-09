from aoc import parse_args


def find_matching(container, predicate):
    return ( index for (index, item) in enumerate(container) if predicate(item) )

def find_first_of(container, predicate):
    return next(find_matching(container, predicate))

def find_last_of(container, predicate):
    return len(container) - find_first_of(reversed(container), predicate) - 1

def get_blocks(line):
    blocks = []
    isFile = True
    n = 0
    for c in line:
        size = int(c)
        for _ in range(size):
            blocks.append(n if isFile else None)

        if isFile:
            n += 1

        isFile = not isFile
    return blocks


def main():
    fileName, part = parse_args()

    blocks = []
    with open(fileName, "r") as f:
        blocks = get_blocks(f.readline().strip())

    gaps = lambda block: block is None
    files = lambda block: block is not None
    
    if part == 1:
        while True:
            firstGap = find_first_of(blocks, gaps)
            lastBlock = find_last_of(blocks, files)
            blocks[firstGap], blocks[lastBlock] = blocks[lastBlock], blocks[firstGap]
            if find_last_of(blocks, files) < find_first_of(blocks, gaps):
                break

    elif part == 2:
        lessThan = len(blocks)
        allGaps = list(find_matching(blocks, gaps))

        while True:
            try:
                lastBlock = find_last_of(blocks, lambda value: value is not None and value < lessThan)
            except StopIteration:
                break

            blockSize = 1
            while lastBlock - blockSize >= 0 and blocks[lastBlock - blockSize] == blocks[lastBlock]:
                blockSize += 1
            
            fittingGap = None
            for gap in allGaps:
                gapSize = 0
                while (gap + gapSize) < (lastBlock - blockSize + 1) and blocks[gap + gapSize] is None:
                    gapSize += 1
                if gapSize >= blockSize:
                    fittingGap = gap
                    break
            
            if fittingGap is None:
                lessThan = blocks[lastBlock]
                continue

            blocks[fittingGap:fittingGap + blockSize] = blocks[lastBlock - blockSize + 1:lastBlock + 1]
            blocks[lastBlock - blockSize + 1:lastBlock + 1] = [None] * blockSize

            allGaps = list(find_matching(blocks, gaps))


    result = sum([ index * value for index, value in enumerate(blocks) if value is not None ])
    print(f"Part {part}:", result)


if __name__ == "__main__":
    main()