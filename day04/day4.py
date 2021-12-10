
class Board():
    def __init__(self, lines):
        self.cells = []
        for line in lines:
            self.cells += [int(n) for n in line.split()]
        self.called = [False] * 25

    def check_cols(self):
        for i in range(5):
            if all(self.called[i::5]):
                return True
        return False

    def check_rows(self):
        for i in range(0,25,5):
            if all(self.called[i:i+5]):
                return True
        return False
    
    def check_win(self):
        return self.check_cols() or self.check_rows()

    def score(self):
        return sum(n[0] for n in zip(self.cells, self.called) if not n[1])

    def add_call(self, n):
        if n in self.cells:
            self.called[self.cells.index(n)] = True
            return self.check_win()
        return False

def solve_part1(calls, boards):
    for call in calls:
        for board in boards:
            if board.add_call(call):
                return board.score() * call
    return 0

def solve_part2(calls, boards):
    for call in calls:
        active_boards = []
        for board in boards:
            if board.add_call(call):
                last_winner = board
                last_winning_call = call
            else:
                active_boards.append(board)
        boards = active_boards
    return last_winner.score() * last_winning_call


def doit(inputfile):
    with open(inputfile,'r') as f:
        lines = (line.strip() for line in f.readlines())
        lines = list(filter(lambda x: len(x) > 0, lines))

    calls = [int(n) for n in lines[0].split(',')]

    boards = []
    for n in range(1, len(lines), 5):
        boards.append(Board(lines[n:n+5]))

    part1_solution = solve_part1(calls, boards)
    part2_solution = solve_part2(calls, boards)
    print(part1_solution)
    print(part2_solution)

doit('test.txt')
doit('input.txt')

#4512
#1924
#27027
#36975
