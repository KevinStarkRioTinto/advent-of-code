## advent of code 2023
## https://adventofcode.com/2023
## day 07

import numpy
from functools import total_ordering 

@total_ordering
class Hand:
    _sequence = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    def __init__(self, cards: str, bid: int = None) -> None:
        self.cards = cards
        self.bid = bid
        self.values, self.counts = numpy.unique(list(cards), return_counts=True)
    
    @property
    def strength(self) -> int:
        # print(f"{self.cards} {sorted(self.counts)}")
        if sorted(self.counts) == [5]:          # Five kind
            return 1
        if sorted(self.counts) == [1, 4]:       # Four kind
            return 2
        if sorted(self.counts) == [2, 3]:       # full house
            return 3
        if sorted(self.counts) == [1, 1, 3]:    # three kind
            return 4
        if sorted(self.counts) == [1, 2, 2]:    # two pair
            return 5
        if sorted(self.counts) == [1, 1, 1, 2]: # one pair
            return 6
        # unique
        return 7

    def __repr__(self) -> str:
        return f"[{self.cards}] #{self.strength}"
    
    def __lt__(self, obj):
        if self.strength != obj.strength: 
            return self.strength > obj.strength
        
        for i, j in zip(self.cards, obj.cards):
            if i == j:
                continue
            return self._sequence.index(i) > self._sequence.index(j)
        
        raise NotImplementedError(self, obj)

class JokerHand(Hand):
    _sequence = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    @property
    def strength(self) -> int:
        # print(f"{self.cards} {sorted(self.counts)}")
        if "J" not in self.cards:
            return super().strength
    
        alts = [Hand(self.cards.replace("J", s)) for s in self._sequence]
        # print(f"{self.cards} {[a.cards for a in alts]}")
        return min([a.strength for a in alts])
    

def parse_input(lines):
    result = []
    for line in lines:
        result.append((line[:5], int(line[6:])))
    return result

def part1(data):
    value = 0
    hands = [Hand(cards, bid) for cards, bid in data]
    for i, hand in enumerate(sorted(hands)):
        # print(f"i: {i+1} {hand} ${hand.bid}")
        value += hand.bid * (i+1)
    return value

def part2(data):
    value = 0
    hands = [JokerHand(cards, bid) for cards, bid in data]
    for i, hand in enumerate(sorted(hands)):
        # print(f"i: {i+1} {hand} ${hand.bid}")
        value += hand.bid * (i+1)
    return value
