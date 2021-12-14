def fold_em(points, folds):
    for f in folds:
        points_to_fold = [p for p in points if p[f['dim']] > f['pos']]
        for p in points_to_fold:
            points.remove(p)
            p[f['dim']] -= (2 * (p[f['dim']] - f['pos']))
            if p not in points:
                points.append(p)

        #print(sorted([p for p in points], key=lambda p: (p['x'], p['y'])))
        #print()
    return points

def plot_em(points):
    max_x = max(p['x'] for p in points) + 1
    max_y = max(p['y'] for p in points) + 1
    plot = [[' ' for i in range(max_x)] for j in range(max_y)]
    for p in points:
        plot[p['y']][p['x']] = '#'
    return "\n".join(''.join(r) for r in plot) + '\n'

def solve_part1(points, folds):
    return len(fold_em(points, folds[0:1]))

def solve_part2(points, folds):
    return plot_em(fold_em(points, folds))
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    points = []
    folds = []
    for line in input_lines:
        line.strip()
        if len(line) > 1:
            if line[0] == 'f':
                d,p = line.split('=')
                folds.append({'dim': d[-1], 'pos': int(p)})
            else:
                x,y = line.split(',')
                points.append({'x':int(x),'y':int(y)})

    print(solve_part1(points[:], folds))
    print(solve_part2(points[:], folds))

doit('test.txt')
doit('input.txt')

"""
17
#####
#   #
#   #
#   #
#####

847
###   ##  #### ###   ##  ####  ##  ### 
#  # #  #    # #  # #  # #    #  # #  #
###  #      #  #  # #    ###  #  # ###
#  # #     #   ###  #    #    #### #  #
#  # #  # #    # #  #  # #    #  # #  #
###   ##  #### #  #  ##  #### #  # ###

"""
