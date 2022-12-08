def part1(grid):
    total = 0
    SIZE = len(grid)
    for x in range(SIZE):
        for y in range(SIZE):
            if (x == 0 or y == 0 or x == SIZE-1 or y == SIZE-1):
                total += 1
            else:
                row = [grid[x][y_2] for y_2 in range(SIZE)]
                col = [grid[x_2][y] for x_2 in range(SIZE)]
                visible_from_left = len([tree for tree in row[:y] if tree < grid[x][y]]) == len(row[:y])
                visible_from_right = len([tree for tree in row[y+1:] if tree < grid[x][y]]) == len(row[y+1:])
                visible_from_top = len([tree for tree in col[:x] if tree < grid[x][y]]) == len(col[:x])
                visible_from_bottom = len([tree for tree in col[x+1:] if tree < grid[x][y]]) == len(col[x+1:])
                if (visible_from_left or visible_from_right or visible_from_top or visible_from_bottom):
                    total += 1
    return total

def part2(grid):
    scores = []
    SIZE = len(grid)
    for x in range(SIZE):
        for y in range(SIZE):
            row = [grid[x][y_2] for y_2 in range(SIZE)]
            col = [grid[x_2][y] for x_2 in range(SIZE)]
            right_score = score(row[y+1:], grid[x][y])
            down_score = score(col[x+1:], grid[x][y])
            up_score = score(list(reversed(col[:x])), grid[x][y])
            left_score = score(list(reversed(row[:y])), grid[x][y])
            scores.append(up_score*left_score*right_score*down_score)
    return max(scores)

def score(view, current_tree):
    return next((i+1 for i, tree in enumerate(list(view)) if tree >= current_tree), len(view))

def format_input(filename):
    lines = open(filename).read().splitlines()
    return [[int(x) for x in line] for line in lines]

def main():
    data = format_input("08.in")
    print("part1", part1(data))
    print("part2", part2(data))

if __name__ == '__main__':
    main()