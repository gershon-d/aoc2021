
def solve_part1(lines):
    samples = [ int(line,2) for line in lines ]

    num_samples = len(samples)
    num_bits = len(lines[0].strip())

    gamma = 0
    for i in range(0, num_bits):
        mask = 1 << i
        bit_sum = sum([(s & mask) >> i for s in samples])
        if bit_sum > num_samples/2:
            gamma |= mask
    epsilon = (~gamma) & ((1 << num_bits) - 1)
    return epsilon * gamma


def solve_part2(lines):
    samples = [ int(line,2) for line in lines ]

    num_samples = len(samples)
    num_bits = len(lines[0].strip())

    curr_samples = samples
    shift = num_bits - 1
    for i in range(0, num_bits):
        bit_sum = sum([(s >> shift) & 1 for s in curr_samples])
        if bit_sum >= len(curr_samples)/2:
            next_samples = list(filter(lambda x: (x >> shift) & 1, curr_samples))
        else:
            next_samples = list(filter(lambda x: ((~x) >> shift) & 1, curr_samples))
        curr_samples = next_samples
        if len(curr_samples) == 1:
            break;
        shift -= 1
    o2_gen = curr_samples[0]

    curr_samples = samples
    shift = num_bits - 1
    for i in range(0, num_bits):
        bit_sum = sum([(s >> shift) & 1 for s in curr_samples])
        if bit_sum >= len(curr_samples)/2:
            next_samples = list(filter(lambda x: ((~x) >> shift) & 1, curr_samples))
        else:
            next_samples = list(filter(lambda x: (x >> shift) & 1, curr_samples))
        curr_samples = next_samples
        if len(curr_samples) == 1:
            break;
        shift -= 1

    co2_scrub = curr_samples[0]
    return o2_gen * co2_scrub


def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    part1_solution = solve_part1(input_lines)
    part2_solution = solve_part2(input_lines)
    print(part1_solution)
    print(part2_solution)

doit('test.txt')
doit('input.txt')

#198
#230
#1458194
#2829354
