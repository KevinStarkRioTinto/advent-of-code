## advent of code 2023
## https://adventofcode.com/2023
## day 05

import re
import numpy
from tqdm import tqdm
from multiprocessing import Pool

stages = None

def parse_input(lines):
    seeds = [int(s) for s in re.findall(r'\b\d+\b', lines.pop(0))]
    global stages
    stages = []
    for line in lines:
        if len(line) <= 0:
            continue
        maps = [int(s) for s in re.findall(r'\b\d+\b', line)]
        if not len(maps):
            stages.append([])
        else:
            stages[-1].append(maps)
    return seeds
    
def get_location(seed: int) -> int:
    # Walk through stages with seed
    for i, sms in enumerate(stages):
        # print(f"stage {i} ({seed}): {sms}")
        for d0, s0, r in sms:
            if seed >= s0 and seed < (s0 + r):
                seed = d0 + (seed - s0)
                break
    
    return seed

def part1(data):
    # print(data)
    locs = [get_location(s) for s in data]
    return min(locs)

def location_range(input) -> int:
    seed, seed_range = input
    global min_loc
    min_range = 999999999
    for si in range(seed_range):
        if (ml := get_location(seed+si)) < min_range:
            min_range = ml
            if min_range < min_loc:
                min_loc = min_range
                print(ml)
                
    return min_range

def part2(data):
    seed_ranges = numpy.array(data).reshape((-1, 2))
    global min_loc
    min_loc = 999999999999
    with Pool() as pool:
        result = pool.map(location_range, seed_ranges)

    return min(result)
