from collections import defaultdict
with open("day6.dat") as infile:
    groups = [line for line in infile.read()[:-1].split("\n\n")]


    answer = 0
    group_yes = []
    for group in groups:
        group_yes = set(group)
        group_yes.discard("\n")
        answer = answer + len(group_yes)
    # print(answer)

answer = 0
with open("day6.dat") as infile:
    groups = []
    for l in infile.read()[:-1].split("\n\n"):
        groups.append(l.split("\n"))
    for group in groups:
        g = defaultdict(int)
        for member in group:
            for x in member:
                g[x] = g[x] + 1
        for v in g.values():
            if v == len(group):
                answer = answer + 1
    print(answer)


