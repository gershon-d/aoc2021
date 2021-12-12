def traverse(cave_map, cave, current_path, all_paths, doneit):
    current_path.append(cave)
    if cave == 'end':
        all_paths.append(current_path)
    else:
        for neighbour in cave_map[cave]:
            if neighbour == 'start':
                continue
            elif neighbour.islower():
                visits = current_path.count(neighbour)
                if visits == 0:
                    traverse(cave_map, neighbour, current_path, all_paths, doneit)
                elif visits == 1 and not doneit:
                    traverse(cave_map, neighbour, current_path, all_paths, True)
            else:
                traverse(cave_map, neighbour, current_path, all_paths, doneit)
    current_path.pop()
    return all_paths

def solve_part1(cave_map):
    return len(traverse(cave_map, 'start', [], [], True))

def solve_part2(cave_map):
    return len(traverse(cave_map, 'start', [], [], False))

def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    cave_map = {}
    for line in input_lines:
        a,b = line.strip().split('-')
        if a not in cave_map:
            cave_map[a] = [b]
        else:
            cave_map[a].append(b)
        if b not in cave_map:
            cave_map[b] = [a]
        else:
            cave_map[b].append(a)
        
    print(solve_part1(cave_map))
    print(solve_part2(cave_map))


doit('test.txt')
doit('test2.txt')
doit('test3.txt')
doit('input.txt')

#10
#36
#19
#103
#226
#3509
#5228
#131228