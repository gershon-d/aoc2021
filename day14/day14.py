def run_step(pairs, rules):
    new_pairs = dict()
    for p in pairs:
        for n in rules[p]:
            if n in new_pairs:
                new_pairs[n] += pairs[p]
            else:
                new_pairs[n] = pairs[p]
    return new_pairs

def count_elements(pairs, template):
    counter = dict()
    for p in pairs:
        for c in p:
            if c in counter:
                counter[c] += pairs[p]
            else:
                counter[c] = pairs[p]
    for c in counter:
        counter[c] //= 2
    counter[template[0]] += 1
    counter[template[-1]] += 1
    return counter

def solve_it(template, rules, steps):
    pairs = dict()
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1

    for i in range(steps):
        pairs = run_step(pairs, rules)
    
    counter = count_elements(pairs, template)
    vals = sorted(counter.values())
    return vals[-1] - vals[0]

def solve_part1(template, rules):
    return solve_it(template, rules, 10)

def solve_part2(template, rules):
    return solve_it(template, rules, 40)
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()
    
    template = input_lines.pop(0).strip()
    input_lines.pop(0)

    rules = dict()
    for line in input_lines:
        tmp = line.split()
        rules[tmp[0]] = (tmp[0][0] + tmp[2], tmp[2] + tmp[0][1])

    print(solve_part1(template, rules))
    print(solve_part2(template, rules))

doit('test.txt')
doit('input.txt')

"""
1588
2188189693529
3831
5725739914282
"""
