if __name__ == "__main__":
    valid_passports = 0
    passports = []
    required_fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    pp = {}
    with open("./day4.dat", "r") as infile:
        for line in infile:
            l = line.split()
            if len(l) == 0:
                passports.append(pp)
                pp = {}
                continue
            for pair in l:
                o, t = pair.split(":")
                pp[o] = t
        passports.append(pp)
    for passport in passports:
        good = True
        keys = passport.keys()
        for f in required_fields:
            if f not in keys:
                # print(f"no {f}")
                good = False
                continue
        if good:
            valid_passports = valid_passports + 1
    print(valid_passports)



