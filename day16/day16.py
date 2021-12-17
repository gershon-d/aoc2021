from functools import reduce
from math import prod

def bits_to_int(stream, i, n):
    return reduce(lambda n,b: n << 1 | b, stream[i:i + n]), i + n

def hex_to_bitlist(hexstr):
    bitlist = []
    for n in (int(c, 16) for c in hexstr):
        bitlist.append((n >> 3) & 1)
        bitlist.append((n >> 2) & 1)
        bitlist.append((n >> 1) & 1)
        bitlist.append(n & 1)
    return bitlist

class Packet():
    def __init__(self, bits):
        self.len_bits = self._parse(bits)

    def _parse(self, bits):
        self.packets = []
        self.val = None
        i = 0
        self.version, i = bits_to_int(bits, i, 3)
        self.type_id, i = bits_to_int(bits, i, 3)
        if self.type_id == 4:
            self.val, i = self._parse_literal(bits, i)
        else:
            length_type_id, i = bits_to_int(bits, i, 1)
            if length_type_id == 0:
                i = self._parse_subs_by_num_bits(bits, i)
            else:
                i = self._parse_subs_by_num_subs(bits, i)
        return i

    def _parse_literal(self, bits, i):
        n = 0
        while True:
            tmp, i = bits_to_int(bits, i, 5)
            n = (n << 4) + (tmp & 0xF)
            if tmp & 0x10 == 0:
                break
        return n, i
    
    def _parse_subs_by_num_bits(self, bits, i):
        num_bits, i = bits_to_int(bits, i, 15)
        while num_bits > 0:
            p = Packet(bits[i:])
            self.packets.append(p)
            i += p.len_bits
            num_bits -= p.len_bits
        return i
    
    def _parse_subs_by_num_subs(self, bits, i):
        num_sub_packets, i = bits_to_int(bits, i, 11)
        while num_sub_packets > 0:
            p = Packet(bits[i:])
            self.packets.append(p)
            i += p.len_bits
            num_sub_packets -= 1
        return i

    def version_sum(self):
        return self.version + sum(p.version_sum() for p in self.packets)
    
    def evaluate(self):
        match self.type_id:
            case 0:
                ret = sum(p.evaluate() for p in self.packets)
            case 1:
                ret = prod(p.evaluate() for p in self.packets)
            case 2:
                ret = min(p.evaluate() for p in self.packets)
            case 3:
                ret = max(p.evaluate() for p in self.packets)
            case 4: 
                ret = self.val
            case 5:
                ret = 1 if self.packets[0].evaluate() > self.packets[1].evaluate() else 0
            case 6: 
                ret = 1 if self.packets[0].evaluate() < self.packets[1].evaluate() else 0
            case 7:
                ret = 1 if self.packets[0].evaluate() == self.packets[1].evaluate() else 0
            case _:
                ret = 0
        return ret

    def __repr__(self):
        return f'version={self.version}, type_id={self.type_id}, val={self.val}, subs={len(self.packets)}'
    
    def dump(self, depth = 0):
        s = ["    " * depth + repr(self)]
        for p in self.packets:
            s += p.dump(depth=depth+1)
        return s
    

def solve_part1(bits):
    p = Packet(bits)
    #print("\n".join(p.dump()))
    return p.version_sum()

def solve_part2(bits):
    p = Packet(bits)
    #print("\n".join(p.dump()))
    return p.evaluate()
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()
    
    for b in (hex_to_bitlist(line.strip()) for line in input_lines):
        print(solve_part1(b))
        print(solve_part2(b))

#doit('test.txt')
doit('input.txt')

"""
925
342997120375
"""
