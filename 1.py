from aoc import parse_args
from collections import defaultdict

def main():
    fileName, _ = parse_args()

    lines = []
    with open(fileName, "r") as f:
        lines = f.readlines()

    left = []
    right = []
    distances = []
    appearances = defaultdict(int)
    similarity = 0

    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
        appearances[int(r)] += 1

    left.sort()
    right.sort()
    for i in range(len(left)):
        distances.append(abs(int(left[i]) - int(right[i])))
        similarity += left[i] * appearances[left[i]]

    print(f"Part 1: {sum(distances)}")
    print(f"Part 2: {similarity}")

if __name__ == '__main__':
    main()