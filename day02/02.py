# A, X = Rock, B, Y = Paper, C, Z = Scissors
# X = loose, Y = draw, Z = win
weapon_scores = {"A": 1, "B": 2, "C" : 3, "X": 1, "Y": 2, "Z" : 3}
beats = {"X": "C", "Y": "A", "Z": "B", "A": "Z", "B": "X", "C": "Y"}
beaten_by = {"A": "Y", "B": "Z", "C": "X"}
def score(his, my):
    weapon_score = weapon_scores[my]
    win_score = 0
    if weapon_scores[my] == weapon_scores[his]:
        win_score = 3
    elif (beats[my] == his):
        win_score = 6
    return weapon_score + win_score

def score_2(his, outcome):
    my = None
    win_score = 0
    if outcome == "X":
        my = beats[his]
        win_score = 0
    elif outcome == "Y":
        my = chr(ord(his) + 23)
        win_score = 3
    else:
        my = beaten_by[his]
        win_score = 6
    return weapon_scores[my] + win_score    

def part1(data):
    return sum([int(score(x[0], x[1])) for x in data])

def part2(data):
    return sum([int(score_2(x[0], x[1])) for x in data])

def format_input(filename):
    lines = open(filename).read().splitlines()
    return [line.split(" ") for line in lines]

def main():
    data = format_input("02.in")
    print("part1", part1(data))
    print("part2", part2(data))

if __name__ == '__main__':
    main()