from aocd.models import Puzzle


def getdata(lines):
    part = 0
    rules = []
    my = []
    nearby = []
    for line in lines:
        print(line)
        if len(line) == 0:
            part +=1
            continue
        if part == 0:
            rules.append(line.split(': ')[1].split(' or '))
        if part == 1 and ":" not in line:
            my.append(line.split(','))
        if part == 2 and ":" not in line:
            nearby.append(line.split(','))
    return rules, my, nearby

def getwrong(rules, nearby):
    wrong = []
    for lnum in nearby:
        for num in lnum:
            flag = 0
            for rule in rules:
                for subrule in rule:
                    min, max = subrule.split('-')
                    if int(num) >= int(min) and int(num) <= int(max):
                        flag = 1
            if flag == 0:
                wrong.append(int(num))
    return wrong

def main():
    puzzle = Puzzle(year=2020, day=16)
    lines = puzzle.input_data.split('\n')
    rules, my, nearby = getdata(lines)
    print(rules)
    print(my)
    print(nearby)
    wrong = getwrong(rules,nearby)
    print(wrong)
    print(sum(wrong))


if __name__ == "__main__":
    # execute only if run as a script
    main()