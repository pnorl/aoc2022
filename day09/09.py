def flatten(l):
    return [item for sublist in l for item in sublist]

def move(direction, head):
    if direction == "U":
        return (head[0], head[1]+1)
    elif direction == "R":
        return (head[0]+1, head[1])
    elif direction == "D":
        return (head[0], head[1]-1)
    elif direction == 'L':
        return (head[0]-1, head[1])

def adjecant(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2-x1) <= 1 and abs(y2-y1) <= 1

def part1(steps):
    head = (0,0)
    tail = (0,0)
    visited = [tail]
    for direction in steps:
        head = move(direction, head)
        if not adjecant(head, tail):
            hx, hy = head
            tx, ty = tail
            if abs(hx-tx) > 1:
                new_x = int(hx-(hx-tx)/2)
                tail = (new_x, hy)
            elif abs(hy-ty)> 1:
                new_y = int(hy-(hy-ty)/2)
                tail = (hx, new_y)
            visited.append(tail)
    return len(set(visited))

def part2(steps):
    head = (0,0)
    tail = [(0,0)]*9
    visited = [(0,0)]
    for direction in steps:
        head = move(direction, head)
        prev = head
        for i in range(len(tail)):
            if not adjecant(prev, tail[i]):
                hx, hy = prev
                tx, ty = tail[i]
                if abs(hx-tx) > 1 and abs(hy-ty) <= 1:
                    new_x = int(hx-(hx-tx)/2)
                    tail[i] = (new_x, hy)
                elif abs(hy-ty) > 1 and abs(hx-tx) <= 1:
                    new_y = int(hy-(hy-ty)/2)
                    tail[i] = (hx, new_y)
                else:
                    new_x = int(hx-(hx-tx)/2)
                    new_y = int(hy-(hy-ty)/2)
                    tail[i] = (new_x, new_y)
            prev = tail[i]
        if (visited[-1] != tail[-1]):
            visited.append(tail[-1])
    print(visited)        
    return len(set(visited))

def format_input(filename):
    lines = open(filename).read().splitlines()
    lines = [line.split() for line in lines]
    return flatten([[direction]*int(times) for direction, times in lines])

def main():
    data = format_input("09.in")
    print("part1", part1(data))
    print("part2", part2(data))

if __name__ == '__main__':
    main()