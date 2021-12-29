from copy import deepcopy
from functools import reduce

class SnailNum():
    def __init__(self, pair, parent=None):
        self.parent = parent
        if type(pair[0]) is int:
            self.left = pair[0]
        elif type(pair[0]) is SnailNum:
            self.left = pair[0]
            pair[0].parent = self
        else:
            self.left = SnailNum(pair[0], parent=self)
        if type(pair[1]) is int:
            self.right = pair[1]
        elif type(pair[1]) is SnailNum:
            self.right = pair[1]
            pair[1].parent = self
        else:
            self.right = SnailNum(pair[1], parent=self)

    def __repr__(self):
        return f'[{self.left}, {self.right}]'

    def add(self, other):
        tmp = SnailNum([deepcopy(self),deepcopy(other)])
        tmp.reduce()
        return tmp
    
    def magnitude(self):
        mag = 0
        if type(self.left) == int:
            mag += 3 * self.left
        else:
            mag += 3 * self.left.magnitude()
        if type(self.right) == int:
            mag += 2 * self.right
        else:
            mag += 2 * self.right.magnitude()
        return mag

    def reduce(self):
        while True:
            if self.explode_step():
                continue
            if self.split_step():
                continue
            break
    
    def explode_step(self, depth=0):
        if depth == 4:
            self.explode()
            return True
        if type(self.left) == SnailNum:
            if self.left.explode_step(depth=depth+1):
                return True
        if type(self.right) == SnailNum:
            if self.right.explode_step(depth=depth+1):
                return True
        return False

    def explode(self):
        p = self.parent
        prev = self
        while p != None:
            if p.right != prev:
                break
            else:
                prev = p
                p = p.parent
        if p != None:
            if type(p.right) == int:
                p.right += self.right
            else:
                p = p.right
                while type(p.left) != int:
                    p = p.left
                p.left += self.right
        
        p = self.parent
        prev = self
        while p != None:
            if p.left != prev:
                break
            else:
                prev = p
                p = p.parent
        if p != None:
            if type(p.left) == int:
                p.left += self.left
            else:
                p = p.left
                while type(p.right) != int:
                    p = p.right
                p.right += self.left
        
        if self.parent.left == self:
            self.parent.left = 0
        else:
            self.parent.right = 0

    def split_step(self):
        if type(self.left) == int:
            if self.left >= 10:
                self.left = SnailNum([self.left//2, (self.left+1)//2], parent=self)
                return True
        elif self.left.split_step():
            return True

        if type(self.right) == int:
            if self.right >= 10:
                self.right = SnailNum([self.right//2, (self.right+1)//2], parent=self)
                return True
        elif self.right.split_step():
            return True

        return False
            
def solve_part1(nums):
    total = reduce(lambda x,y: x.add(y), nums)
    print(total)
    return total.magnitude()

def solve_part2(nums):
    max_mag = 0
    max_pair = None
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j:
                mag = x.add(y).magnitude()
                if mag > max_mag:
                    max_mag = mag
                    max_pair = (x,y)
    print(max_pair[0])
    print(max_pair[1])
    return max_mag
    
def doit(inputfile):
    with open(inputfile,'r') as f:
        input_lines = f.readlines()

    nums = [SnailNum(eval(line.strip())) for line in input_lines]
    print(solve_part1(nums))
    print(solve_part2(nums))

doit('test.txt')
doit('input.txt')

"""
[[[[6, 6], [7, 6]], [[7, 7], [7, 0]]], [[[7, 7], [7, 7]], [[7, 8], [9, 9]]]]
4140
[[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]]
[[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]]
3993
[[[[7, 7], [7, 8]], [[8, 7], [8, 8]]], [[[9, 8], [0, 9]], [[9, 9], [8, 9]]]]
4641
[[[[4, 5], [9, 6]], [7, [8, 0]]], [[2, [9, 9]], [8, [0, 8]]]]
[[4, [[9, 6], [3, 9]]], [[[9, 3], 2], 6]]
4624
"""