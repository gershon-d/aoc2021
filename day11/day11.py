def count_flashes(grid):
    flashes = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] > 9:
                flashes += 1
                grid[x][y] = 0
                for x,y in filter(lambda p: p[0] >= 0 and p[0] < len(grid) and p[1] >= 0 and p[1] < len(grid[0]),   \
                                ((x, y+1), (x, y-1), (x+1, y), (x+1, y+1), (x+1, y-1), (x-1, y), (x-1, y+1), (x-1, y-1))):
                    if grid[x][y] != 0:
                        grid[x][y] += 1
    if flashes > 0:
        flashes += count_flashes(grid)
    return flashes

def run_a_day(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] += 1
    return count_flashes(grid)

def solve_part1(grid):
    result = 0
    for i in range(100):
        result += run_a_day(grid)
    return result

def solve_part2(grid):
    yesterday, today, days = 0, run_a_day(grid), 1
    while today != yesterday + 100:
        yesterday = today
        today = run_a_day(grid)
        days += 1
    return days
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    grid = [[int(c) for c in line.strip()] for line in input_lines]
    print(solve_part1(grid))

    grid = [[int(c) for c in line.strip()] for line in input_lines]
    print(solve_part2(grid))


doit('test.txt')
doit('input.txt')

#1656
#195
#1719
#232
