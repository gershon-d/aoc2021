def get_minima(grid):
    minima = []
    for x in range(1, len(grid)- 1):
        for y in range(1, len(grid[0])- 1):
            if grid[x][y] < grid[x][y-1] and \
                       grid[x][y] < grid[x][y+1] and \
                       grid[x][y] < grid[x-1][y] and \
                       grid[x][y] < grid[x+1][y]:
                minima.append((x,y))
    return minima

def map_basin(grid, x, y):
    result = 1
    val = grid[x][y]
    grid[x][y] = 10
    if grid[x][y+1] < 9 and grid[x][y+1] > val:
        result += map_basin(grid, x, y+1)
    if grid[x][y-1] < 9 and grid[x][y-1] > val:
        result += map_basin(grid, x, y-1)
    if grid[x+1][y] < 9 and grid[x+1][y] > val:
        result += map_basin(grid, x+1, y)
    if grid[x-1][y] < 9 and grid[x-1][y] > val:
        result += map_basin(grid, x-1, y)
    return result

def solve_part1(grid):
    minima = get_minima(grid)
    return sum(grid[x][y] for x,y in minima) + len(minima)
    
def solve_part2(grid):
    minima = get_minima(grid)
    basins = [map_basin(grid, x, y) for x, y in minima]
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()
    
    grid = [[int(c) for c in line.strip()] for line in input_lines]
    for row in grid:
        row.insert(0, 10)
        row.append(10)
    grid.insert(0, [10] * len(grid[0]))
    grid.append([10] * len(grid[0]))

    part1_solution = solve_part1(grid)
    part2_solution = solve_part2(grid)
    print(part1_solution)
    print(part2_solution)

doit('test.txt')
doit('input.txt')

#15
#1134
#508
#1564640
