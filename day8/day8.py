class Entry():
    def __init__(self, line):
        tmp = line.split('|')
        self.pattern_strs = tmp[0].strip().split()
        self.output_strs = tmp[1].strip().split()

    def decode(self):
        digits = {}     # mapping of digit to pattern that represents it
        patterns = [frozenset(d for d in s) for s in self.pattern_strs]
        outputs = [frozenset(d for d in s) for s in self.output_strs]
        patterns.sort(key=len)
        len_fives = patterns[3:6]
        len_sixes = patterns[6:9]

        # start with digits with unique number of segments
        digits[1], digits[7], digits[4], digits[8] = patterns[0], patterns[1], patterns[2], patterns[9]
    
        top = digits[7] - digits[1] # top seg is diff of 7 and 1
        for p in len_fives:         # 3 is only pattern of length 5 that is a superset of 7
            if p > digits[7]:
                digits[3] = p
                break
        len_fives.remove(digits[3])

        for p in len_sixes:         # 9 is only pattern of length 6 that is a superset of 3
            if p > digits[3]:
                digits[9] = p
                break
        len_sixes.remove(digits[9])
        
        top_left = digits[9] - digits[3]    # top-left seg is diff of 9 and 3

        if top_left < len_fives[0]:     # 5 and 2 are only length == 5 digits left
            digits[5] = len_fives[0]    # 5 contains top-left, 2 does not
            digits[2] = len_fives[1]
        else:
            digits[5] = len_fives[1]
            digits[2] = len_fives[0]

        top_right = digits[9] - digits[5]   # top-right seg is diff of 9 and 5

        if top_right < len_sixes[0]:    # 6 and 0 are only length == 6 digits left
            digits[0] = len_sixes[0]    # 0 contains top-right, 6 does not
            digits[6] = len_sixes[1]
        else:
            digits[0] = len_sixes[1]
            digits[6] = len_sixes[0]

        decoder = { p:d for d,p in digits.items() }     # all digits mapped to patterns
                                                        # flip the map and decode output
        result = 0
        for output in outputs:
            result *= 10
            result += decoder[output]
        
        return result

def solve_part1(entries):
    result = 0
    for entry in entries:
        for output_str in entry.output_strs:
            if len(output_str) in (2,4,3,7): 
                result += 1
    return result
    
def solve_part2(entries):
    return sum(e.decode() for e in entries)
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    for line in input_lines:
        entries = [Entry(line) for line in input_lines]

    part1_solution = solve_part1(entries)
    part2_solution = solve_part2(entries)
    print(part1_solution)
    print(part2_solution)

doit('test.txt')
doit('input.txt')

#26
#61229
#284
#973499

