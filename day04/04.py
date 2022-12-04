def expand_range(input):
    start, end = input.split("-")
    return [x for x in range(int(start), int(end)+1)]

def part1(pairs):
    return len([1 for elf_1, elf_2 in pairs if fully_contains(elf_1, elf_2)])

def fully_contains(list_1, list_2):
    set_1, set_2 = set(list_1), set(list_2)
    return set_1.issubset(set_2) or set_1.issuperset(set_2)

def intersects(list_1, list_2):
    return len(set(list_1).intersection(set(list_2))) > 0

def part2(pairs):
    return len([1 for elf_1, elf_2 in pairs if intersects(elf_1, elf_2)])

def expand_ranges(line):
    return [expand_range(elf_range) for elf_range in line.split(",")]

def format_input(filename):
    lines = open(filename).read().splitlines()
    return [expand_ranges(line) for line in lines]

def main():
    data = format_input("04.in")
    print("part1", part1(data))
    print("part2", part2(data))

if __name__ == '__main__':
    main()