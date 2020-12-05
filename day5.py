if __name__ == "__main__":
    data = []
    with open("./day5.dat", "r") as infile:
        for line in infile:
            data.append(line.rstrip())
    # data = ["FBFBBFFRLR"]
    #for d in data[0:1]:
    max_seat = 0
    for d in data:
        r = [x for x in range(0, 128)]
        for x in range(0, 7):
            if d[x] == "F":
                r = r[:len(r) // 2]
            if d[x] == "B":
                r = r[len(r) // 2:]
        print(r[0])
        s = [x for x in range(0, 8)]
        for x in range(7, 10):
            if d[x] == "R":
                s = s[len(s) // 2:]
            if d[x] == "L":
                s = s[:len(s) // 2]
        print(s[0])
        if (r[0] * 8 + s[0]) > max_seat:
            max_seat = r[0] * 8 + s[0]
    print(max_seat)



