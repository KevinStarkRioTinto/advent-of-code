## advent of code 2023
## https://adventofcode.com/2023
## day 06

import re
import numpy

def parse_input(lines):
    times = [int(v) for v in re.findall(r'\b\d+\b', lines[0])]
    dists = [int(v) for v in re.findall(r'\b\d+\b', lines[1])]
    return [(t, d) for t, d in zip(times, dists)]

def dists(time: int) -> list[int]:
    assert time > 0
    return [t * (time-t) for t in range(1, time)]

def part1(data):
    ways = []
    for time, record in data:
        # print(time, record)
        attempts = dists(time)
        wins = list(filter(lambda d: d > record, attempts))
        if len(wins):
            ways.append(len(wins))
    return numpy.prod(ways)

def part2(data):
    time = int("".join([str(x[0]) for x in data]))
    record = int("".join([str(x[1]) for x in data]))
    
    attempts = dists(time)
    wins = list(filter(lambda d: d > record, attempts))
    return len(wins)