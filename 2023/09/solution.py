## advent of code 2023
## https://adventofcode.com/2023
## day 09

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Sequence():
    vals: list[int]

    def diffs(self) -> Sequence:
        return Sequence([self.vals[i+1] - self.vals[i] for i in range(len(self.vals)-1)])
    
    def extrapolate(self, seq: Sequence, end: bool = True) -> Sequence:
        if end:
            return Sequence([*self.vals, self.vals[-1] + seq.vals[-1]])
        else:
            return Sequence([self.vals[0] - seq.vals[0], *self.vals])

    @property
    def is_zero(self) -> bool:
        return all([v == 0 for v in self.vals])

def parse_input(lines):
    return [Sequence([int(s) for s in line.split()]) for line in lines]

def part1(data):
    lasts = []
    for s in data:        
        stack = [s]
        while not stack[-1].is_zero:
            stack.append(stack[-1].diffs())
        
        # Extend by 1
        seq = Sequence([*stack.pop().vals, 0])
        for i in range(len(stack)):
            # print(seq)
            seq = stack.pop().extrapolate(seq)
            
        lasts.append(seq.vals[-1])

    return sum(lasts)

def part2(data):
    firsts = []
    for s in data:        
        stack = [s]
        while not stack[-1].is_zero:
            stack.append(stack[-1].diffs())
        
        # Extend by 1
        seq = Sequence([0, *stack.pop().vals])
        for i in range(len(stack)):
            # print(seq)
            seq = stack.pop().extrapolate(seq, end=False)
            
        firsts.append(seq.vals[0])

    return sum(firsts)
