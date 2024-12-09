from aoc import parse_args
from itertools import product

def main():
    fileName, part = parse_args()

    lines = []
    with open(fileName, "r") as f:
        lines = f.readlines()

    result = {}
    operators = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y
    }

    if part == 2:
        operators["|"] = lambda x, y: int(str(x) + str(y))

    for line in lines:
        expected, values = line.split(":")
        expected = int(expected)
        values = [ int(value) for value in values.split() ]

        configurations = list(product(operators.keys(), repeat=len(values) - 1))
        for currentConfiguration in configurations:
            configuration = [ operators[value] for value in currentConfiguration ]
            numbers = values.copy()
            stack = [ numbers.pop(0), numbers.pop(0) ]
            while len(stack) == 2:
                op = configuration.pop(0)
                value = op(*stack)
                stack = [value]
                if len(numbers) == 0 and stack[0] == expected:
                    print(f"expected {expected}, values {values}, currentConfiguration {currentConfiguration}")
                    result[line] = expected
                elif len(numbers) > 0:
                    stack.append(numbers.pop(0))

    print(f"Part {part}: {sum(result.values())}")

if __name__ == "__main__":
    main()