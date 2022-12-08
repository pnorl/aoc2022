def part1(grid):
    total = 0
    SIZE = len(grid)
    for x in range(SIZE):
        for y in range(SIZE):
            if (x == 0 or y == 0 or x == SIZE-1 or y == SIZE-1):
                total += 1
            else:
                row = get_row(grid, x)
                col = get_col(grid, y)
                visible_from_left = visible(row[:y], grid[x][y])
                visible_from_right = visible(row[y+1:], grid[x][y])
                visible_from_top = visible(col[:x], grid[x][y])
                visible_from_bottom = visible(col[x+1:], grid[x][y])
                if (visible_from_left or visible_from_right or visible_from_top or visible_from_bottom):
                    total += 1
    return total

def get_row(grid, x):
    return [grid[x][y_2] for y_2 in range(len(grid))]

def get_col(grid, y):
    [grid[x_2][y] for x_2 in range(len(grid))]

def visible(trees, tree):
    return sum([1 for t in trees if t >= tree]) == 0

def part2(grid):
    scores = []
    SIZE = len(grid)
    for x in range(SIZE):
        for y in range(SIZE):
            row = get_row(grid, x)
            col = get_col(grid, y)
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