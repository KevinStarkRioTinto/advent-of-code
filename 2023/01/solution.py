## advent of code 2023
## https://adventofcode.com/2023
## day 01
import re

def parse_input(lines):
    return lines

def part1(data):
    # Get first and last digit from string as a 2-digit int
    first_last = []
    for line in data:
       nums = [
           int(i) 
           for i in re.findall(
               "(?=([0-9]))", line
            )
       ]
       # May only have one digit
       first_last.append(nums[0] * 10 + nums[-1])
    # Sum of line numbers
    return sum(first_last)

digit_lookup = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}

def to_numeric(s: str) -> int:
  # Convert number from char or text
  if s.isdigit():
    return int(s)
  else:
    return digit_lookup[s.lower()]

def part2(data):
    # Line may now have numeric words
    first_last = []
    for line in data:
        nums = [
            to_numeric(x)
            for x in re.findall(
                rf'(?=([0-9]|{"|".join(digit_lookup.keys())}))',
                line
            )
        ]
        first_last.append(nums[0] * 10 + nums[-1])
    return sum(first_last)
