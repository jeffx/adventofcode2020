import re


def part1(d):
    pass


def part2(d):
    pass


if __name__ == "__main__":
    RE_LINE = r"^([0-9]*)-([0-9]*) ([a-zA-Z]): (.*)"
    data = []
    good = 0
    with open("./day2.dat", "r") as data_file:
        for line in data_file:
            m = re.match(RE_LINE, line.rstrip())
            if m:
                start = int(m.group(1))
                stop = int(m.group(2)) + 1
                letter = m.group(3)
                password = m.group(4)
                r = list(range(start, stop))
                print(start)
                print(stop)
                print(r)
                count = password.count(letter)
                if count in r:
                    #print(line)
                    #print(f"count={count}")
                    #print(f"start={start}")
                    #print(f"stop={stop}")
                    good = good + 1
            #data.append(int(line.rstrip()))
    print(good)
    part1(data)
    part2(data)

