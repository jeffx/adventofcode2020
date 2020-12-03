def load_grid():
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
    return grid


def part2(grid, ds, rs):
    tree_count = 0
    d = 0
    r = 0
    while d < (len(grid) - 1):
        d = d + ds
        r = r + rs
        if grid[d][r % len(grid[d])] == "#":
            tree_count = tree_count + 1
    return tree_count

if __name__ == "__main__":
    g = load_grid()
    # Part 1
    print(part2(g, 1, 3))
    # Part 2
    one = part2(g, 1, 1)
    two = part2(g, 1, 3)
    three = part2(g, 1, 5)
    four = part2(g, 1, 7)
    five = part2(g, 2, 1)
    print(one * two * three * four * five)
