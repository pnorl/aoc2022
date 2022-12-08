def part1(filesystem):
    return sum([s for s in size(filesystem) if s <= 100000])

def size(filesystem):
    sizes = [] # All sizes of subdirectories, last is size of current node
    current_size = 0
    for key, value in filesystem.items():
        if (key == ".."):
            continue
        if type(value) == dict:
            sub_dir_size = size(value)
            sizes.extend(sub_dir_size)
            current_size += sub_dir_size[-1]
        else:
            current_size += value      
    sizes.append(current_size)
    return sizes

def to_file_system(commands):
    root = {}
    current = None
    for command, output in commands:
        command_name = command[1]
        if command_name == "cd":
            to_go = command[2]
            if to_go == "/":
                current = root
            else:
                current = current[to_go]
        elif command_name == "ls":
            # Add files and folders to curent dir.
            for type, name in output:
                if type == "dir":
                    current[name] = {"..": current}
                else:
                    current[name] = int(type)    
    return root


def part2(filesystem):
    sizes = size(filesystem)
    sizes.sort()
    required_space = 30000000
    total_space = 70000000
    used_space = sizes[-1]
    min_space_to_delete = required_space - (total_space-used_space)
    return [s for s in sizes if s >= min_space_to_delete][0]

def format_input(filename):
    lines = open(filename).read().splitlines()
    lines = [line.split() for line in lines]
    commands = [(i, line) for i, line in enumerate(lines) if line[0] == '$']
    commands_with_output = []
    for i, command in enumerate(commands):
        output_start = command[0]+1
        output_end = None
        if (i+1 < len(commands)):
            output_end = commands[(i+1)%len(commands)][0]
        commands_with_output.append((command[1], lines[output_start:output_end]))
    return to_file_system(commands_with_output)

def main():
    filesystem = format_input("07.in")
    print("part1", part1(filesystem))
    print("part2", part2(filesystem))

if __name__ == '__main__':
    main()