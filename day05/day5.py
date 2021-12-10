
class Line():
    def __init__(self, input_line):
        tmp = input_line.split()
        start = tmp[0].split(',')
        stop = tmp[2].split(',')
        self.start = (int(start[0]), int(start[1]))
        self.stop  = (int(stop[0]), int(stop[1]))

    def is_horizontal(self):
        return self.start[1] == self.stop[1]

    def is_vertical(self):
        return self.start[0] == self.stop[0]

    def horizontal_points(self):
        y = self.start[1]
        if self.start[0] <= self.stop[0]:
            return ((x,y) for x in range(self.start[0], self.stop[0] + 1))
        else:
            return ((x,y) for x in range(self.start[0], self.stop[0] - 1, -1))

    def vertical_points(self):
        x = self.start[0]
        if self.start[1] < self.stop[1]:
            return ((x,y) for y in range(self.start[1], self.stop[1] + 1))
        else:
            return ((x,y) for y in range(self.start[1], self.stop[1] - 1, -1))

    def diagonal_points(self):
        if self.start[0] < self.stop[0]:
            run = range(self.start[0], self.stop[0] + 1)
        else:
            run = range(self.start[0], self.stop[0] - 1, -1)
        if self.start[1] < self.stop[1]:
            rise = range(self.start[1], self.stop[1] + 1)
        else:
            rise = range(self.start[1], self.stop[1] - 1, -1)
        return zip(run, rise)

    def points(self, include_diag=False):
        if self.is_horizontal():
            return self.horizontal_points()
        elif self.is_vertical():
            return self.vertical_points()
        elif include_diag:
            return self.diagonal_points()
        else:
            return []

def solve_part1(lines):
    plot = {}
    solution = 0
    for line in lines:
        for p in line.points():
            if p in plot:
                plot[p] += 1
                if plot[p] == 2:
                    solution += 1
            else:
                plot[p] = 1
    return solution

def solve_part2(lines):
    plot = {}
    solution = 0
    for line in lines:
        for p in line.points(include_diag=True):
            if p in plot:
                plot[p] += 1
                if plot[p] == 2:
                    solution += 1
            else:
                plot[p] = 1
    return solution


def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    lines = []
    for input_line in input_lines:
        lines.append(Line(input_line))

    part1_solution = solve_part1(lines)
    part2_solution = solve_part2(lines)
    print(part1_solution)
    print(part2_solution)

doit('test.txt')
doit('input.txt')

#5
#12
#5608
#20299
