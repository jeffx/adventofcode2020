def part1(d):
    for i in d:
        for j in d:
            if i + j == 2020:
                print(i * j)
                return


def part2(d):
    for i in d:
        for j in d:
            for x in d:
                if i + j + x == 2020:
                    print(i * j * x)
                    return


if __name__ == '__main__':
    data = []
    with open("day1.dat", "r") as data_file:
        for line in data_file:
            data.append(int(line.rstrip()))
    part1(data)
    part2(data)
