import re
from aoc import parse_args


def main():
    fileName, part = parse_args()

    lines = []
    with open(fileName, "r") as f:
        lines = f.readlines()

    expression = re.compile(r'(do\(\)|don\'t\(\)|mul\((\d{1,3})\,(\d{1,3})\))')

    total = 0
    enabled = True

    for line in lines:
        captures = expression.findall(line)
        for match in captures:
            if part == 2:
                if "don't" in match[0]:
                    enabled = False
                elif "do" in match[0]:
                    enabled = True
                elif enabled:
                    total += int(match[1]) * int(match[2])
            else:
                total += int(match[1]) * int(match[2])

    print(f"Part {part}: {total}")

if __name__ == "__main__":
    main()