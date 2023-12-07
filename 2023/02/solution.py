## advent of code 2023
## https://adventofcode.com/2023
## day 02

import re

def parse_input(lines):
    games = {}
    for line in lines:
        id = int(re.findall(r"Game (\d+):", line)[0])
        r, g, b = [
            [
                int(n)
                for n in re.findall(rf"(\d+) {color}", line)
            ]
            for color in ['red', 'green', 'blue']
        ]
        games[id] = (r, g, b)
    return games

def part1(data):
    cr,cg,cb = (12, 13, 14)
    result = 0
    for id, rgb in data.items():
        r, g, b = [max(v) for v in rgb]
        if r <= cr and g <= cg and b <= cb:
            result += id
    return result

def part2(data):
    result = 0
    for id, rgb in data.items():
        r, g, b = [max(v) for v in rgb]
        rgb_power = r*g*b
        result += rgb_power
    return result