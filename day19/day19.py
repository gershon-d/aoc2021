from functools import reduce
import operator

rotations = [lambda x, y, z: ( x,  y, z), lambda x, y, z: (-z,  y,  x), lambda x, y, z: (-x,  y, -z), lambda x, y, z: (z,  y, -x),    #  y is up, rotate 0, 90, 180, 270
             lambda x, y, z: (-x, -y, z), lambda x, y, z: (-z, -y, -x), lambda x, y, z: ( x, -y, -z), lambda x, y, z: (z, -y,  x),    #  y is down, rotate 0, 90, 180, 270
             lambda x, y, z: ( y,  z, x), lambda x, y, z: (-x,  z,  y), lambda x, y, z: (-y,  z, -x), lambda x, y, z: (x,  z, -y),    #  z is up, rotate 0, 90, 180, 270
             lambda x, y, z: (-y, -z, x), lambda x, y, z: (-x, -z, -y), lambda x, y, z: ( y, -z, -x), lambda x, y, z: (x, -z,  y),    #  z is down, rotate 0, 90, 180, 270
             lambda x, y, z: ( z,  x, y), lambda x, y, z: (-y,  x,  z), lambda x, y, z: (-z,  x, -y), lambda x, y, z: (y,  x, -z),    #  x is up, rotate 0, 90, 180, 270
             lambda x, y, z: (-z, -x, y), lambda x, y, z: (-y, -x, -z), lambda x, y, z: ( z, -x, -y), lambda x, y, z: (y, -x,  z)]    #  x is down, rotate 0, 90, 180, 270

def get_rotations(scanner):
    return [[r(p[0], p[1], p[2]) for p in scanner] for r in rotations]

def find_overlaps(s1, s2):
    for r, rotate in enumerate(rotations):
        poss = dict()
        for i, p1 in enumerate(s1):
            for j, p2 in enumerate(s2):
                p = tuple(map(operator.sub, p1, rotate(p2[0], p2[1], p2[2])))
                if p in poss:
                    poss[p].append((r,i,j,p1,p2,p))
                else:
                    poss[p] = [(r,i,j,p1,p2,p)]

        for k,v in poss.items():
            if len(v) >= 12:
                return v
    return ()

def reorient(scanner, origin, rotation):
    return [tuple(map(operator.add, origin, rotations[rotation](p[0], p[1], p[2]))) for p in scanner]

def map_beacons(scanners):
    all_mappings = [(0, scanners[0], (0,0,0))]
    unmapped = [(i + 1, s) for i, s in enumerate(scanners[1:])]
    new_mappings = all_mappings
    while len(unmapped) > 0:
        mappings = new_mappings
        new_mappings = []
        for s1 in mappings:
            for s2 in unmapped[:]:
                overlaps = find_overlaps(s1[1], s2[1])
                if len(overlaps) > 0:
                    #print(f'overlap found: {s1[0]}, {s2[0]}')
                    # for p in overlaps:
                    #     print(p)
                    new_mappings.append((s2[0], reorient(s2[1], overlaps[0][5], overlaps[0][0]), overlaps[0][5]))
                    unmapped.remove(s2)
        all_mappings += new_mappings

    beacons = list(set(reduce(operator.add, (m[1] for m in all_mappings))))
    return beacons, tuple(m[2] for m in sorted(all_mappings))

all_beacons = []
all_scanners = []

def solve_part1(scanners):
    global all_beacons
    global all_scanners
    all_beacons, all_scanners = map_beacons(scanners)
    return len(all_beacons)

def solve_part2():
    global all_scanners
    best = 0
    for i in range(len(all_scanners)):
        for j in range(i + 1, len(all_scanners)):
            best = max(best, abs(reduce(operator.add, map(operator.sub, all_scanners[i], all_scanners[j]))))
    return best
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = [line.strip() for line in f.readlines() if len(line.strip()) > 0]

    scanners = []
    scanner = []
    for line in input_lines:
        if line[0:3] == '---':
            if len(scanner) > 0:
                scanners.append(scanner)
                scanner = []
        else:
            scanner.append(tuple(int(x) for x in line.split(',')))
    scanners.append(scanner)

    print(solve_part1(scanners))
    print(solve_part2())

doit('test.txt')
doit('input.txt')

"""
79
3621
483
14804
"""
