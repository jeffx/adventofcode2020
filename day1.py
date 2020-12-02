import sys


if __name__ == '__main__':
    data = []
    with open("day1.dat", "r") as f:
        for l in f:
            data.append(int(l.rstrip()))
    for i in data:
        for j in data:
            for x in data:
                if i + j + x == 2020:
                    print(i * j * x)
                    sys.exit(0)

