def priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

def find_duplicates(objects):
    if len(objects) == 1:
        return objects
    # find duplicates among last 2 elements.
    duplicates = [x for x in objects[-2] if x in set(objects[-1])]
    return find_duplicates(objects[:-2] + [duplicates])

def split_into_compartments(list):
    return [list[:int(len(list)/2)], list[int(len(list)/2):]]

def group_rugsacks(rugsacks):
    return [rugsacks[i:i+3] for i in range(0, len(rugsacks), 3)] 

def part1(rugsacks):
    rugsacks = [split_into_compartments(rugsack) for rugsack in rugsacks]
    duplicates = [find_duplicates(compartments)[0][0] for compartments in rugsacks]
    return sum([priority(duplicate) for duplicate in duplicates])

def part2(rugsacks):
    groups = group_rugsacks(rugsacks)
    return sum([priority(find_duplicates(rugsacks)[0][0]) for rugsacks in groups])

def format_input(filename):
    lines = open(filename).read().splitlines()
    return lines

def main():
    data = format_input("03.in")
    print("part1", part1(data))
    print("part2", part2(data))

if __name__ == '__main__':
    main()