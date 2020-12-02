import re


RE_LINE = r"^([0-9]*)-([0-9]*) ([a-zA-Z]): (.*)"


def part1(d):
    good = 0
    for l in d:
        m = re.match(RE_LINE, l.rstrip())
        if m:
            start = int(m.group(1))
            stop = int(m.group(2)) + 1
            letter = m.group(3)
            password = m.group(4)
            r = list(range(start, stop))
            count = password.count(letter)
            if count in r:
                good = good + 1
    print(good)


def part2(d):
    good = 0
    for l in d:
        m = re.match(RE_LINE, l.rstrip())
        if m:
            c = 0
            start = int(m.group(1)) - 1
            stop = int(m.group(2)) - 1
            letter = m.group(3)
            password = m.group(4)

            try:
                if password[start] == letter:
                    c = c + 1
                if password[stop] == letter:
                    c = c + 1
                if c == 1:
                    good = good + 1
            except Exception:
                continue
    print(good)


if __name__ == "__main__":
    data = []
    with open("./day2.dat", "r") as data_file:
        for line in data_file:
            data.append(line.rstrip())
    part1(data)
    part2(data)
