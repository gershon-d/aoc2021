from copy import deepcopy

def pretty_print(image):
    for row in image:
        print(''.join('.' if x == 0 else '#' for x in row))
    print()

def pad_image(grid, pad):
    for row in grid:
        row.insert(0, pad)
        row.append(pad)
    grid.insert(0, [pad] * len(grid[0]))
    grid.append([pad] * len(grid[0]))

def process_pixel(image, algorithm, y, x):
    n = (image[y-1][x-1] << 8)   \
        | (image[y-1][x]   << 7) \
        | (image[y-1][x+1] << 6) \
        | (image[y][x-1]   << 5) \
        | (image[y][x]     << 4) \
        | (image[y][x+1]   << 3) \
        | (image[y+1][x-1] << 2) \
        | (image[y+1][x]   << 1)\
        | (image[y+1][x+1] << 0)
    return algorithm[n]

def process_image(image, algorithm):
    pad_image(image, image[0][0])
    new_image = deepcopy(image)
    for y in range(1, len(image) - 1):
        for x in range(1, len(image[0]) - 1):
            new_image[y][x] = process_pixel(image, algorithm, y, x)
    if (algorithm[0] == 1 and new_image[0][0] == 0) or (algorithm[-1] == 0 and new_image[0][0] == 1):
        new_image[0] = [1 - new_image[0][0]] * len(new_image[0])
        for i in range(1, len(new_image) - 1):
            new_image[i][0] = 1 - new_image[i][0]
            new_image[i][-1] = 1 - new_image[i][-1]
        new_image[-1] = [1 - new_image[-1][0]] * len(new_image[0])
    return new_image

def solve_part1(image, algorithm):
    pad_image(image, 0)
    new_image = process_image(image, algorithm)
    new_image = process_image(new_image, algorithm)
    return sum(sum(row) for row in new_image)

def solve_part2(image, algorithm):
    pad_image(image, 0)
    new_image = image
    for i in range(50):
        new_image = process_image(new_image, algorithm)
    return sum(sum(row) for row in new_image)
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = [line.strip() for line in f.readlines()]
    
    algorithm = [1 if x == '#' else 0 for x in input_lines[0]]
    image = [[1 if x == '#' else 0 for x in line] for line in input_lines[2:]]

    print(solve_part1(image, algorithm))
    print(solve_part2(image, algorithm))

doit('test.txt')
doit('input.txt')

"""
35
3351
5057
18502
"""
