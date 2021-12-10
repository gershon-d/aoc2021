from functools import reduce

matches = {'(':')', '[':']', '{':'}', '<':'>'}
def get_corrupt_char(line):
    stack = []
    for c in line:
        if c in matches:
            stack.append(c)
        else:
            tmp = stack.pop()
            if c != matches[tmp]:
                return c
    return '0'

def get_completion_str(line):
    stack = []
    for c in line:
        if c in matches:
            stack.append(c)
        else:
            tmp = stack.pop()
            if c != matches[tmp]:
                return []
    return [matches[c] for c in reversed(stack)]

def solve_part1(lines):
    values = {'0':0, ')':3, ']':57, '}':1197, '>':25137}
    return sum(values[get_corrupt_char(line.strip())] for line in lines)

def solve_part2(lines):
    values = {')':1, ']':2, '}':3, '>':4}
    scores = []
    for line in lines:
        cs = get_completion_str(line.strip())
        if len(cs) > 0: 
            scores.append(reduce(lambda score, c: score * 5 + values[c], cs, 0))
    return sorted(scores)[len(scores)//2]
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()
    print(solve_part1(input_lines))
    print(solve_part2(input_lines))

doit('test.txt')
doit('input.txt')

#26397
#288957
#369105
#3999363569
