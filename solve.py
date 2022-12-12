from dataclasses import dataclass
from typing import Callable
from typing import List

@dataclass
class Monkey:
    items: List[int]
    operation: Callable[[int], int]
    throw_to: Callable[[int], int]
    inspections: int = 0

def part1(monkeys: List[Monkey]):
    for round_ in range(1,21):
        print("round", round_)
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                # monkey inpects item
                item = monkey.items.pop(0)
                item = monkey.operation(item)
                monkey.inspections += 1
                item = int(item/3)
                throw_to_monkey = monkey.throw_to(item)
                monkeys[throw_to_monkey].items.append(item)
    top_inspections = sorted([monkey.inspections for monkey in monkeys],reverse=True)[:2]    
    return top_inspections[0]*top_inspections[1]

def part2(monkeys):
    for round_ in range(1,1001):
        print("round", round_)
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                # monkey inpects item
                item = monkey.items.pop(0)
                print(item)
                item = monkey.operation(item)
                monkey.inspections += 1
                throw_to_monkey = monkey.throw_to(item)
                monkeys[throw_to_monkey].items.append(item)
    top_inspections = sorted([monkey.inspections for monkey in monkeys],reverse=True)[:2]    
    return top_inspections[0]*top_inspections[1]

def format_items(items):
    return [int(item) for item in(items.split(": ")[-1]).split(", ")]

def format_operation(operation) -> Callable[[int], int]:
    operation = operation.split("= ")[-1]
    return lambda x: eval(operation.replace("old", str(x)))

def last_digit(s : str) -> int:
    return int(s.split(" ")[-1])

def format_test(test, test_true, test_false) -> Callable[[int], int]:
    divisible_by = last_digit(test)
    true_value = last_digit(test_true)
    test_false = last_digit(test_false)
    assert(type(test_false)) == int
    return lambda x: true_value if x % divisible_by == 0 else test_false

def format_monkey(monkey_data) -> List[Monkey]:
    _, items, operation, test, test_true, test_false = monkey_data.split('\n')
    return Monkey(format_items(items), format_operation(operation), format_test(test, test_true, test_false))

def format_input(filename):
    monkeys = open(filename).read().split("\n\n")
    return [format_monkey(monkey) for monkey in monkeys]

def main():
    data = format_input("input.in")
    print(data)
    print("part1", part1(data))
    print("part2", part2(data))

if __name__ == '__main__':
    main()