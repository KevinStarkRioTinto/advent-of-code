## advent of code 2023
## https://adventofcode.com/2023
## day 08

import re
import numpy
import math


links = {}

def parse_input(lines):
    global links
    steps = list(lines.pop(0))
    for line in lines:
        try:
            src, d0, d1 = re.findall(r"\w{3}", line)
            links[src] = (d0, d1)
        except:
            pass
    return steps
        

def follow(loc, dir) -> str:
    global links
    if dir == "L":
        return links[loc][0]
    else:
        return links[loc][1]

def part1(data):
    global links
    if 'AAA' not in links:
        return -1
    
    loc = "AAA"
    step = 0
    i = 0
    while loc != "ZZZ":
        loc = follow(loc, data[i])
        step += 1
        i += 1

        if i >= len(data):
            i = 0

    return step

def part2(data):
    global links
    locs = [s for s in links.keys() if s.endswith("A")]
    stops = [0 for _ in locs]

    step = 0
    i = 0
    while True:
        locs = [follow(l, data[i]) for l in locs]
        step += 1
        i += 1

        for j, l in enumerate(locs):
            if l.endswith('Z') and stops[j] == 0:
                stops[j] = step
                print(f"{j}: {step}")
                if all([s > 0 for s in stops]):
                    return math.lcm(*stops)

        if i >= len(data):
            i = 0
