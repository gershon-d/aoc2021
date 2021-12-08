def solve_part1(steps):
    x = 0
    d = 0
    for s in steps:
        s = s.split()
        direction = s[0]
        mag = int(s[1])
        if direction == 'forward':
            x += mag
        elif direction == 'down':
            d += mag
        elif direction == 'up':
            d -= mag
    return x * d

def solve_part2(steps):
    x = 0
    d = 0
    aim = 0

    for s in steps:
        s = s.split()
        direction = s[0]
        mag = int(s[1])
        if direction == 'forward':
            x += mag
            d += aim * mag
        elif direction == 'down':
            aim += mag
        elif direction == 'up':
            aim -= mag
    return x * d

def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    part1_solution = solve_part1(input_lines)
    part2_solution = solve_part2(input_lines)
    print(part1_solution)
    print(part2_solution)

doit('test.txt')
doit('input.txt')

#150
#900
#1989265
#2089174012
