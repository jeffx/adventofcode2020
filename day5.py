if __name__ == "__main__":
    data = []
    with open("./day5.dat", "r") as infile:
        for line in infile:
            data.append(line.rstrip())
    max_seat = 0
    seats = [None] * 900
    for d in data:
        r = [x for x in range(0, 128)]
        for x in range(0, 7):
            if d[x] == "F":
                r = r[:len(r) // 2]
            if d[x] == "B":
                r = r[len(r) // 2:]
        s = [x for x in range(0, 8)]
        for x in range(7, 10):
            if d[x] == "R":
                s = s[len(s) // 2:]
            if d[x] == "L":
                s = s[:len(s) // 2]
        seat = r[0] * 8 + s[0]
        seats[seat] = "X"
        if seat > max_seat:
            max_seat = seat
    print(max_seat)  # Max Seat is the answer to Part 1
    """I didn't understand the question for part 2.  So I 
       just printed out what sounded right, and hoped the 
       output would be obvious.  It was.
    """
    seats = seats[:max_seat]
    for x in range(0, len(seats)):
        if seats[x] != "X":
            print(x)



