from copy import deepcopy

class Node:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost
        self.neighbours = []
    
    def add_neighbour(self, n):
        self.neighbours.append(n)
    
    def __repr__(self):
        return f'(x = {self.x}, y = {self.y}, cost = {self.cost})'
        #s = ", ".join(f'({n.x}, {n.y})' for n in self.neighbours)
        #return f'(x = {self.x}, y = {self.y}, cost = {self.cost}, neighbours={s})'
        #return f'{self.cost}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def shortest_path(nodes, start, finish):
    front = [start]
    costs = {start : 0}
    while len(front) > 0:
        next_front = []
        for node in front:
            for n in node.neighbours:
                if n not in costs:
                    costs[n] = costs[node] + n.cost
                    if n not in next_front:
                        next_front.append(n)
                else:
                    if costs[n] > costs[node] + n.cost:
                        costs[n] = costs[node] + n.cost
                        if n not in next_front:
                            next_front.append(n)
        front = next_front
    return costs[finish]

def connect_nodes(grid):
    nodes = []
    for y, row in enumerate(grid):
        for x, node in enumerate(row):
            if x > 0:
                node.add_neighbour(grid[y][x-1])
            if x < len(row) - 1:
                node.add_neighbour(grid[y][x+1])
            if y > 0:
                node.add_neighbour(grid[y-1][x])
            if y < len(grid) - 1:
                node.add_neighbour(grid[y+1][x])
            nodes.append(node)
    return nodes

def solve_part1(grid):
    nodes = connect_nodes(grid)
    return shortest_path(nodes, nodes[0], nodes[-1])

def solve_part2(grid):
    for y, row in enumerate(grid):
        new_nodes = []
        for i in range(1,5):
            new_nodes += [Node(x + (i * len(row)), y, n.cost + i if n.cost + i <= 9 else (n.cost + i) % 9) for x,n in enumerate(row)]
        row += new_nodes
    
    new_rows = []
    for i in range(1,5):
        for y, row in enumerate(grid):
            new_rows.append([Node(x, y + (i * len(grid)), n.cost + i if n.cost + i <= 9 else (n.cost + i) % 9) for x,n in enumerate(row)])
    grid += new_rows

    nodes = connect_nodes(grid)
    return shortest_path(nodes, nodes[0], nodes[-1])
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()
    
    grid = [[Node(x, y, int(c)) for x, c in enumerate(line.strip())] for y, line in enumerate(input_lines)]
    grid2 = deepcopy(grid)

    print(solve_part1(grid))
    print(solve_part2(grid2))

doit('test.txt')
doit('input.txt')

"""
40
315
388
2819
"""
