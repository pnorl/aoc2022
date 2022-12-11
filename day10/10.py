def get_x_after_cycle(commands):
    X = 1
    cycle = 1
    # Stores the value of x at the beginning of each cycle
    x_after_cycle = {0: 1}
    for command in commands:
        if command[0] == "noop":
            x_after_cycle[cycle] = x_after_cycle[cycle-1]
        elif command[0] == "addx":
            x_after_cycle[cycle] = x_after_cycle[cycle-1]
            cycle += 1
            x_after_cycle[cycle] = x_after_cycle[cycle-1] + int(command[1])
        cycle += 1
    return x_after_cycle    


def part1(commands):
    x_after_cycle = get_x_after_cycle(commands)
    return sum([x_after_cycle[i-1]*i for i in range(20, 221, 40)])

def part2(commands):
    crt = ""
    x_after_cycle = get_x_after_cycle(commands)
    for cycle in range(0, 241):
        x = x_after_cycle[cycle]
        if x in range(cycle%40-1, (cycle%40)+2):
            crt += "#"
        else:
            crt += " "
        if ((cycle+1) % 40) == 0:
            crt += "\n"
    return crt

def format_input(filename):
    lines = open(filename).read().splitlines()
    return [line.split() for line in lines]

def main():
    data = format_input("10.in")
    print("part1", part1(data))
    print("part2")
    print(part2(data))

if __name__ == '__main__':
    main()