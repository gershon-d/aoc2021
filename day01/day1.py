def solve_part1(lines):
    prev = int(lines[0])
    count = 0
    for line in lines[1:]:
        n = int(line)
        if n > prev:
            count += 1
        prev = n
    return count

def solve_part2(lines):
    samples = [int(line) for line in lines]
    prev = 10000000
    count = 0
    for i in range(0, len(samples) - 2):
        n = sum(samples[i:i+3])
        if n > prev:
            count += 1
        prev = n
    return count

def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    part1_solution = solve_part1(input_lines)
    part2_solution = solve_part2(input_lines)
    print(part1_solution)
    print(part2_solution)

doit('test.txt')
doit('input.txt')
#7
#5
#1521
#1543
