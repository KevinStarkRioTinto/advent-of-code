## advent of code 2023
## https://adventofcode.com/2023
## day 04

import re

def parse_input(lines):
    data = []
    for line in lines:
        id, draw_str, card_str = re.split(":|\|", line)
        # print({"id": id, "win_str": win_str, "card_str": card_str})
        draw = [int(s.strip()) for s in re.findall(r'\b\d+\b', draw_str)]
        card = [int(s.strip()) for s in re.findall(r'\b\d+\b', card_str)]
        data.append((id, draw, card))
    return data

def evaluate_game(draw: list[int], card: list[int]) -> list[int]:
    return list(set(draw) & set(card))

def part1(data):
    points = 0
    for id, draw, card in data:
        card_wins = evaluate_game(draw, card)
        # print(id, draw,"|", card, "=", card_wins)

        if len(card_wins):
            game_points = 1
            for i in range(len(card_wins)-1):
                game_points *= 2
            points += game_points
    return points

def part2(data):
    games = {id: (draw, card) for id, draw, card in data}
    card_ids = list(games.keys())
    stack = list(games.keys())
    
    i = 0
    while i < len(stack):
        # Find wining copies
        id = stack[i]
        draw, card = games[id]

        card_wins = evaluate_game(draw, card)
        # print(i, id, draw, "|", card, "=", card_wins)

        card_index = card_ids.index(id)
        for j in range(card_index+1, card_index+len(card_wins)+1):
            # print(f"  adding {card_ids[j]}")
            stack.append(card_ids[j])
        i += 1
    return len(stack)