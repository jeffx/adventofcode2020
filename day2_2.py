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

