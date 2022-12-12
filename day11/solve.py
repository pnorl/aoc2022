from dataclasses import dataclass
from typing import Callable
from typing import List
from functools import reduce
import copy

@dataclass
class Monkey:
    items: List[int]
    operation: Callable[[int], int]
    throw_to: List[int]
    inspections: int = 0

def part1(monkeys: List[Monkey]):
    return get_answer(monkeys, 20, lambda x: int(x/3))

def part2(monkeys: List[Monkey]):
    return get_answer(monkeys, 10000, None)

def get_answer(monkeys: List[Monkey], rounds: int, reduce_worry: Callable):
    congruent_to_all = reduce((lambda x, y: x * y), [m.throw_to[0] for m in monkeys])
    for _ in range(rounds):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                # monkey inpects item
                item = monkey.items.pop(0)
                item = monkey.operation(item)
                monkey.inspections += 1
                if reduce_worry:
                    item = reduce_worry(item)
                divisible_by, if_true, if_false  = monkey.throw_to
                throw_to_monkey = None
                if item % divisible_by == 0:
                    throw_to_monkey = if_true
                else:
                    throw_to_monkey = if_false
                item = item % congruent_to_all
                monkeys[throw_to_monkey].items.append(item)
    top_inspecting_monkeys = sorted([monkey.inspections for monkey in monkeys],reverse=True)[:2]    
    return top_inspecting_monkeys[0]*top_inspecting_monkeys[1]

def format_items(items):
    return [int(item) for item in(items.split(": ")[-1]).split(", ")]

def format_operation(operation) -> Callable[[int], int]:
    return lambda x: eval(operation.split("= ")[-1].replace("old", str(x)))

def last_digit(s : str) -> int:
    return int(s.split(" ")[-1])

def format_test(test, test_true, test_false) -> List[int]:
    dividable_by = last_digit(test)
    true_value = last_digit(test_true)
    test_false = last_digit(test_false)
    return [dividable_by, true_value, test_false]

def format_monkey(monkey_data) -> List[Monkey]:
    _, items, operation, test, test_true, test_false = monkey_data.split('\n')
    return Monkey(format_items(items), format_operation(operation), format_test(test, test_true, test_false))

def format_input(filename):
    monkeys = open(filename).read().split("\n\n")
    return [format_monkey(monkey) for monkey in monkeys]

def main():
    print("part1", part1(format_input("input.in")))
    print("part2", part2(format_input("input.in")))

if __name__ == '__main__':
    main()