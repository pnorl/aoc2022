def find_first_distinct(data, n):
    # Marker is 1-indexed
    for i in range(n-1, len(data)):
        if (len(set(data[i-n+1:i+1]))) == n:
            return i+1

def part1(data):
    return find_first_distinct(data, 4)

def part2(data):
    return find_first_distinct(data, 14)

def format_input(filename):
    lines = open(filename).read()
    return lines

def main():
    data = format_input("06.in")
    print("part1", part1(data))
    print("part2", part2(data))

if __name__ == '__main__':
    main()