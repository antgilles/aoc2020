from aocd.models import Puzzle

def getdata(lines):
    part = 0
    rules = []
    my = []
    nearby = []
    for line in lines:
        if len(line) == 0:
            part +=1
            continue
        if part == 0:
            rules.append([line.split(': ')[1].split(' or '), line.split(': ')[0]])
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
                for subrule in rule[0]:
                    min, max = subrule.split('-')
                    if int(num) >= int(min) and int(num) <= int(max):
                        flag = 1
            if flag == 0:
                wrong.append(num)
    delete = []
    for i in range(len(nearby)):
        for wrongnum in wrong:
            if wrongnum in nearby[i]:
                delete.append(nearby[i])
    for l in delete:
        if l in nearby:
            nearby.remove(l)
    return nearby


def getposrule(rules,nearby):
    dicopos = {}
    for pos in range(len(nearby[0])):
        dicopos[pos]=[]
        for rule in rules:
            flag = 0
            for ticket in nearby:
                if (int(ticket[pos]) < int(rule[0][0].split('-')[0]) or int(ticket[pos]) > int(rule[0][0].split('-')[1])) and (int(ticket[pos]) < int(rule[0][1].split('-')[0]) or int(ticket[pos]) > int(rule[0][1].split('-')[1])):
                    flag = 1
                    break
            if flag == 0:
                dicopos[pos].append(rule)
    return dicopos

def fixpos(dicopos):
    fixpos = {}
    dejavu = []
    for cnt in range(20):
        for key, value in dicopos.items():
            for dv in dejavu:
                if dv in value:
                    value.remove(dv)
            if len(value) == 1:
                fixpos[value[0][1]] = key
                dejavu.append(value[0])
                break
    return fixpos

def getres(fixpos,my):
    res = 1
    for key, value in fixpos.items():
        if "departure" in key:
            res *= int(my[value])
    print(res)
def main():
    puzzle = Puzzle(year=2020, day=16)
    lines = puzzle.input_data.split('\n')
    rules, my, nearby = getdata(lines)
    nearby = getwrong(rules,nearby)
    dicopos = getposrule(rules,nearby)
    fix = fixpos(dicopos)
    getres(fix,my[0])
if __name__ == "__main__":
    # execute only if run as a script
    main()