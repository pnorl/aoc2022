def part1(data):
    return max([sum(x) for x in data])

def part2(data):
    sums = [sum(x) for x in data]
    sums.sort()
    return sum(sums[-3:])

def format_input(filename):
    with open(filename) as file:
        lines = file.read()
        return [[int(y) for y in x.split('\n')] for x in lines.split('\n\n')]

def main():
    data = format_input("01.in")
    print("part1", part1(data))
    print("part2", part2(data))

if __name__ == '__main__':
    main()