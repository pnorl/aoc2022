ROCK, PAPER, SCISSORS = 1,2,3
LOSE, DRAW, WIN = 0, 3, 6

beats = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}
beaten_by = {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK}

# A, X = Rock, B, Y = Paper, C, Z = Scissors
action_map = {"X": ROCK, "Y": PAPER, "Z": SCISSORS, "A": ROCK, "B": PAPER, "C": SCISSORS}
# X = loose, Y = draw, Z = win
outcome_map = {"X": LOSE, "Y": DRAW, "Z": WIN}
            
def score(their, my):
    if beats[my] == their:
        return my + WIN
    elif my == their:
        return my + DRAW
    else:
        return my

def score_with_outcome(their, result):
    if result == LOSE:
        return beats[their]
    elif result == DRAW:
        return their + DRAW
    else:
        return beaten_by[their] + WIN

def part1(data):
    return sum([score(action_map[their], action_map[my]) for their, my in data])

def part2(data):
    return sum([int(score_with_outcome(action_map[their], outcome_map[result])) for their, result in data])

def format_input(filename):
    lines = open(filename).read().splitlines()
    return [line.split(" ") for line in lines]

def main():
    data = format_input("02.in")
    print("part1", part1(data))
    print("part2", part2(data))

if __name__ == '__main__':
    main()