from statistics import median

def triangular_number(n):
    return n * (n + 1) // 2

def solve_part1(crabs):
    m = median(crabs)
    return int(sum(abs(c - m) for c in crabs))

def solve_part2(crabs):
    best = 0
    for i in range(min(crabs), max(crabs) + 1):
        fuel = sum(triangular_number(abs(c-i)) for c in crabs)
        if fuel < best or best == 0:
            best = fuel
    return best

def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    crabs = [int(n) for n in input_lines[0].split(',')]

    part1_solution = solve_part1(crabs)
    part2_solution = solve_part2(crabs)
    print(part1_solution)
    print(part2_solution)

doit('test.txt')
doit('input.txt')

#37.0
#168
#355764.0
#99634572
