import re

def calc_x(v, step):
    if step > v:
        step = v
    return int(step * (v - (step-1)/2))

def run_y(v, target):
    y = 0
    hits = []
    step = 0
    if v >= 0:
        step = 2*v + 1
        v = 0 - v - 1
    while True:
        y += v
        if y < target[0]:
            break
        v -= 1
        step += 1
        if y <= target[1]:
            hits.append(step)
    return hits

def solve_part1(x_target, y_target):
    return (y_target[0] * y_target[0] + y_target[0])//2

def solve_part2(x_target, y_target):
    solutions = set()
    for vy in range(y_target[0], (y_target[0] * -1) + 1):
        hits = run_y(vy, y_target)
        for step in hits:
            for vx in range(x_target[1] + 1):
                x = calc_x(vx, step)
                if x >= x_target[0] and x <= x_target[1]:
                    solutions.add((vx,vy))
    return len(solutions)
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    m = re.search(r'x=(\d+)\.+(\d+).+y=(-?\d+)\.+(-?\d+)', input_lines[0])
    x_range = [int(n) for n in m.group(1,2)]
    y_range = [int(n) for n in m.group(3,4)]

    print(solve_part1(x_range, y_range))
    print(solve_part2(x_range, y_range))

doit('test.txt')
doit('input.txt')

"""
45
112
13203
5644
"""
