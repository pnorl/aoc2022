def part1(data):
    return "not solved"

def part2(data):
    return "not solved"

def format_input(filename):
    lines = open(filename).read().splitlines()
    return lines

def main():
    data = format_input("0.in")
    print("part1", part1(data))
    print("part2", part2(data))

if __name__ == '__main__':
    main()