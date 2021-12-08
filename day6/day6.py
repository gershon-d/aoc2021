
# recursive solution, solved part2 in about 12 hours...
def next_day(days_til_split, days_remaining):
    if days_remaining == 0:
        return 1
    days_remaining -= 1
    if days_til_split == 0:
        return next_day(6, days_remaining) + next_day(8, days_remaining)
    else:
        return next_day(days_til_split - 1, days_remaining)


# much faster:
def solve_it(fish, days):
    hist = [0] * 9
    for f in fish:
        hist[f] += 1

    while days > 0:
        new_fish = hist[0]
        for i in range(0, 8):
            hist[i] = hist[i+1]
        hist[8] = new_fish
        hist[6] += new_fish
        days -= 1

    return sum(hist)

def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    fish = [int(n) for n in input_lines[0].split(',')]

    part1_solution = solve_it(fish, 80)
    part2_solution = solve_it(fish, 256)
    print(part1_solution)
    print(part2_solution)

doit('test.txt')
doit('input.txt')

#5934
#26984457539
#375482
#1689540415957
