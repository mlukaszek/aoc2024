import sys

def parse_args(args = sys.argv[1:]):
    fileName = args[0] if len(args) > 1 else "input.txt"
    part = 1 if len(args) == 1 else int(args[1])
    return fileName, part