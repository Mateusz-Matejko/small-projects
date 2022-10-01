import json
from random import choice

start_money = 1
expected_win = 100
chose_to_win = "red"

bet_money = start_money

red_counter = 0
green_counter = 0
black_counter = 0

green = [0]
black = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
red = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
whole_roulette = green + black + red

total_spent = 0


for _ in range(76):
    won_turns = []
    turn = 0
    while True:
        bet_money = 2 * bet_money
        turn += 1
        res = choice(whole_roulette)
        if res in red and bet_money > expected_win and bet_money > (0.5 * total_spent):
            red_counter += 1
            won_turns.append(turn)
            simulation_details = {}
            won_turns = sorted(won_turns)
            simulation_details["red_counter"] = red_counter
            simulation_details["black_counter"] = black_counter
            simulation_details["green_counter"] = green_counter
            simulation_details["final_bet_money"] = bet_money
            simulation_details["bet_turn"] = turn
            simulation_details["total_spent"] = total_spent
            simulation_details["won_amount"] = bet_money * 2 - total_spent
            simulation_details["longest_lose_streak"] = won_turns[-1]
            simulation_details["shortest_lose_streak"] = won_turns[0]
            simulation_details[f"average_games_to_be_on_plus_for_{len(won_turns)}_games"] = sum(won_turns) / len(
                won_turns)
            with open("results-holder.json", "a") as f:
                json.dump(simulation_details, f, indent=2, sort_keys=True)
            break
        elif res in black:
            black_counter += 1
            continue
        elif res in green:
            green_counter += 1
            continue
        total_spent += bet_money
