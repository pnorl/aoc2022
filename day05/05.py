import re
import copy

def part1(stacks, instructions):
    rearranged_stacks = copy.deepcopy(stacks)
    for n, from_ ,to in instructions:
        for _ in range(n):
            move = rearranged_stacks[from_].pop()
            rearranged_stacks[to].append(move)

    return "".join([stack[-1] for stack in rearranged_stacks.values()])

def part2(stacks, instructions):
    rearranged_stacks = copy.deepcopy(stacks)
    for n, from_ ,to in instructions:
        move = rearranged_stacks[from_][-n:]
        del rearranged_stacks[from_][-n:]
        rearranged_stacks[to].extend(move)

    return "".join([stack[-1] for stack in rearranged_stacks.values()])

def format_input(filename):
    stacks, instructions = open(filename).read().split("\n\n")
    stacks = stacks.split("\n")
    stacks = {int(stack_id):[row[(1 + (int(stack_id)-1)*4)] for row in stacks if row[(1 +(int(stack_id)-1)*4)] != ' '] for stack_id in stacks.pop().split()}

    instructions = [[int(x) for x in re.split("move | from | to ", instruction)[1:]] for instruction in instructions.split("\n")]
    for stack in stacks.values():
        stack.reverse()    
    return stacks, instructions

def main():
    stacks, instructions = format_input("05.in")
    print("part1", part1(stacks, instructions))
    print("part2", part2(stacks, instructions))

if __name__ == '__main__':
    main()