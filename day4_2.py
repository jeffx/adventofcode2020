import re

PID_MATCH = r"^[0-9]{9}"
HCL_MATCH = r"^#[0-9a-f]{6}"
HGT_MATCH = r"^([0-9]*)(cm|in)"
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
                good = False
                continue
            if f == "byr":
                if 1920 > int(passport[f]) or int(passport[f]) > 2002:
                    good = False
                    continue
            if f == "iyr":
                if 2010 > int(passport[f]) or int(passport[f]) > 2020:
                    good = False
                    continue
            if f == "eyr":
                if 2020 > int(passport[f]) or int(passport[f]) > 2030:
                    good = False
                    continue
            if f == "hgt":
                m = re.match(HGT_MATCH, passport[f])
                if not m:
                    good = False
                    continue
                else:
                    if m.group(2) == "in":
                        if 59 > int(m.group(1)) or int(m.group(1)) > 76:
                            good = False
                            continue
                    else:
                        if 150 > int(m.group(1)) or int(m.group(1)) > 193:
                            good = False
                            continue
            if f == "hcl":
                if not re.match(HCL_MATCH, passport[f]):
                    good = False
                    continue
            if f == "ecl":
                if passport[f] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    good = False
                    continue
            if f == "pid":
                if not re.match(PID_MATCH, passport[f]):
                    good = False
                    continue
        if good:
            valid_passports = valid_passports + 1
            print(passport)
    print(valid_passports)



