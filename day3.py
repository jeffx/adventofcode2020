data = []
with open("./day3.dat", "r") as data_file:
    for line in data_file:
        data.append(line.rstrip())
grid = []
for l in data:
    r = []
    for c in l:
        r.append(c)
    grid.append(r)
    max_r = len(r) - 1
max_d = len(grid) - 1


def part1(d):
    tree_count = 0
    grid = []
    for l in d:
        r = []
        for c in l:
            r.append(c)
        grid.append(r)
        max_r = len(r) - 1
    max_d = len(grid) - 1
    d = 0
    r = 0
    while d < max_d:
        d = d + 1
        r = r + 3
        if r > max_r:
            r = r - (max_r + 1)
        if grid[d][r] == "#":
            tree_count = tree_count + 1
    return tree_count

def part2(ds, rs):
    tree_count = 0
    d = 0
    r = 0
    while d < max_d:
        d = d + ds
        r = r + rs
        if r > max_r:
            r = r - (max_r + 1)
        if grid[d][r] == "#":
            tree_count = tree_count + 1
    return tree_count

if __name__ == "__main__":
    data = []
    with open("./day3.dat", "r") as data_file:
        for line in data_file:
            data.append(line.rstrip())
    print(part1(data))
    one = part2(1, 1)
    two = part2(1, 3)
    three = part2(1, 5)
    four = part2(1, 7)
    five = part2(2, 1)
    print(one * two * three * four * five)
